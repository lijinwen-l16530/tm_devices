"""Base Infiniium scope device driver module."""

from __future__ import annotations

import logging
import os

from abc import ABC
from pathlib import Path
from types import MappingProxyType
from typing import Any, TYPE_CHECKING

import pyvisa as visa

# Import Infiniium command classes (consistent with Tektronix pattern)
from tm_devices.commands.infiniium_commands import (
    InfiniiumAcquireCommands,
    InfiniiumChannelCommands,
    InfiniiumDisplayCommands,
    InfiniiumMarkerCommands,
    InfiniiumMeasureCommands,
    InfiniiumTimebaseCommands,
    InfiniiumTriggerCommands,
    InfiniiumWaveformCommands,
)
from tm_devices.driver_mixins.abstract_device_functionality import (
    BusMixin,
    ChannelControlMixin,
    HistogramMixin,
    LicensedMixin,
    MathMixin,
    MeasurementsMixin,
    PlotMixin,
    PowerMixin,
    ReferenceMixin,
    ScreenCaptureMixin,
    SearchMixin,
    USBDrivesMixin,
)
from tm_devices.drivers.scopes.keysight.keysight_scope import KeysightScope
from tm_devices.helpers import DeviceConfigEntry
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl

_logger: logging.Logger = logging.getLogger(__name__)


class InfiniiumChannel:
    """Class to hold Infiniium channel information."""

    def __init__(self, name: str, probe_type: str = "ANALOG") -> None:
        """Initialize the channel.

        Args:
            name: The channel name (e.g., "CHANnel1", "DIGital1").
            probe_type: The probe type ("ANALOG" or "DIGITAL").
        """
        self.name = name
        self.probe_type = probe_type


class InfiniiumChannelCollection:
    """A collection class for Infiniium channel commands."""

    def __init__(self, device: PIControl, num_channels: int) -> None:
        """Initialize the channel collection.

        Args:
            device: The PIControl device instance.
            num_channels: The number of channels.
        """
        self._device = device
        self._num_channels = num_channels
        self._channels: dict[int, InfiniiumChannelCommands] = {}

    def __getitem__(self, key: int) -> InfiniiumChannelCommands:
        """Get a channel by number.

        Args:
            key: The channel number (1-based).

        Returns:
            The channel commands object.
        """
        if not 1 <= key <= self._num_channels:
            raise IndexError(f"Channel number must be between 1 and {self._num_channels}")
        if key not in self._channels:
            self._channels[key] = InfiniiumChannelCommands(self._device, key)
        return self._channels[key]


class InfiniiumCommands:
    """Container for all Infiniium SCPI commands.

    This class provides access to all SCPI command trees in a structured manner,
    similar to the Tektronix tm_devices .commands API.
    """

    def __init__(self, device: PIControl) -> None:
        """Initialize the commands container.

        Args:
            device: The PIControl device instance.
        """
        self._device = device
        # Initialize command trees
        self._acquire: InfiniiumAcquireCommands | None = None
        self._timebase: InfiniiumTimebaseCommands | None = None
        self._trigger: InfiniiumTriggerCommands | None = None
        self._waveform: InfiniiumWaveformCommands | None = None
        self._measure: InfiniiumMeasureCommands | None = None
        self._display: InfiniiumDisplayCommands | None = None
        self._marker: InfiniiumMarkerCommands | None = None
        self._channel: InfiniiumChannelCollection | None = None

    @property
    def acquire(self) -> InfiniiumAcquireCommands:
        """Return the :ACQuire command tree."""
        if self._acquire is None:
            self._acquire = InfiniiumAcquireCommands(self._device)
        return self._acquire

    @property
    def timebase(self) -> InfiniiumTimebaseCommands:
        """Return the :TIMebase command tree."""
        if self._timebase is None:
            self._timebase = InfiniiumTimebaseCommands(self._device)
        return self._timebase

    @property
    def trigger(self) -> InfiniiumTriggerCommands:
        """Return the :TRIGger command tree."""
        if self._trigger is None:
            self._trigger = InfiniiumTriggerCommands(self._device)
        return self._trigger

    @property
    def waveform(self) -> InfiniiumWaveformCommands:
        """Return the :WAVeform command tree."""
        if self._waveform is None:
            self._waveform = InfiniiumWaveformCommands(self._device)
        return self._waveform

    @property
    def measure(self) -> InfiniiumMeasureCommands:
        """Return the :MEASure command tree."""
        if self._measure is None:
            self._measure = InfiniiumMeasureCommands(self._device)
        return self._measure

    @property
    def display(self) -> InfiniiumDisplayCommands:
        """Return the :DISPlay command tree."""
        if self._display is None:
            self._display = InfiniiumDisplayCommands(self._device)
        return self._display

    @property
    def marker(self) -> InfiniiumMarkerCommands:
        """Return the :MARKer command tree."""
        if self._marker is None:
            self._marker = InfiniiumMarkerCommands(self._device)
        return self._marker

    @property
    def channel(self) -> InfiniiumChannelCollection:
        """Return the :CHANnel<N> command collection."""
        if self._channel is None:
            # Default to 4 channels, can be overridden by subclass
            self._channel = InfiniiumChannelCollection(self._device, 4)
        return self._channel

    @property
    def ch(self) -> InfiniiumChannelCollection:
        """Return the :CHANnel<N> command collection (shortcut alias for .channel).

        This provides a concise API consistent with Tektronix usage::

            scope.commands.ch[1].scale.write(0.5)
        """
        return self.channel

    # ==========================================================================================
    # Tektronix-compatible aliases
    # ==========================================================================================
    # These properties provide Tektronix-compatible naming so that the same code can run on
    # both Tektronix and Keysight scopes without modification.

    @property
    def horizontal(self) -> InfiniiumTimebaseCommands:
        """Tektronix-compatible alias for :TIMebase (:HORizontal in Tektronix).

        Usage::

            scope.commands.horizontal.scale.write(1e-3)  # works on both Tek & Keysight
        """
        return self.timebase

    @property
    def measurement(self) -> InfiniiumMeasureCommands:
        """Tektronix-compatible alias for :MEASure (:MEASUrement in Tektronix).

        Usage::

            scope.commands.measurement.frequency.write("CHANnel1")
        """
        return self.measure

    @property
    def data(self) -> InfiniiumWaveformCommands:
        """Tektronix-compatible alias for :WAVeform (:DATa in Tektronix).

        Usage::

            preamble = scope.commands.data.preamble_query.query()
        """
        return self.waveform

    @property
    def curve(self) -> InfiniiumWaveformCommands:
        """Tektronix-compatible alias for :WAVeform (:CURVe in Tektronix).

        Usage::

            scope.commands.curve.source.write("CHANnel1")
        """
        return self.waveform

    @property
    def vertical(self) -> InfiniiumChannelCollection:
        """Tektronix-compatible alias for channel collection (:VERTical in Tektronix).

        Usage::

            scope.commands.vertical[1].scale.write(0.5)
        """
        return self.channel


class Infiniium(
    KeysightScope,
    BusMixin,
    HistogramMixin,
    LicensedMixin,
    MathMixin,
    MeasurementsMixin,
    ReferenceMixin,
    SearchMixin,
    PlotMixin,
    PowerMixin,
    USBDrivesMixin,
    ChannelControlMixin,
    ScreenCaptureMixin,
    ABC,
):
    """Base Infiniium scope device driver.

    This class contains shared functionality between all Infiniium series devices.

    Example usage::

        # Connect to Infiniium oscilloscope
        scope = device_manager.add_scope("TCPIP::192.168.1.100::INSTR")

        # Use .commands API similar to Tektronix
        scope.commands.acquire.mode.write("RTIME")
        scope.commands.timebase.scale.write(1e-3)
        scope.commands.channel[1].scale.write(0.5)
        scope.commands.trigger.edge.source.write("CHANnel1")
        scope.commands.trigger.edge.slope.write("POSitive")
    """

    # Number of analog channels (can be overridden by subclasses)
    NUM_CHANNELS: int = 4

    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
        default_visa_timeout: int,
    ) -> None:
        """Create an Infiniium device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
            default_visa_timeout: The default VISA timeout value in milliseconds.
        """
        super().__init__(config_entry, verbose, visa_resource, default_visa_timeout)
        self._num_dig_bits_in_ch: int = 8
        self._commands: InfiniiumCommands | None = None

    @property
    def commands(self) -> InfiniiumCommands:
        """Return the commands object for SCPI command access.

        This provides access to all SCPI command trees in a structured manner,
        similar to the Tektronix tm_devices .commands API.

        Returns:
            InfiniiumCommands: The commands container object.
        """
        if self._commands is None:
            self._commands = InfiniiumCommands(self)
        return self._commands

    @property
    def ch(self) -> InfiniiumChannelCollection:
        """Return the channel commands collection.

        This is a convenience property for quick channel access.

        Returns:
            InfiniiumChannelCollection: The channel commands collection.
        """
        if self._commands is None:
            self._commands = InfiniiumCommands(self)
        # Only recreate the channel collection if the number of channels has changed
        chan = self._commands._channel
        if chan is None or chan._num_channels != self.NUM_CHANNELS:
            self._commands._channel = InfiniiumChannelCollection(self, self.NUM_CHANNELS)
        return self._commands.channel

    @cached_property
    def channel(self) -> MappingProxyType[str, InfiniiumChannel]:
        """Mapping of channel names to channel objects."""
        channel_map: dict[str, InfiniiumChannel] = {}

        # Get analog channel count
        num_analog = self.total_channels
        for i in range(1, num_analog + 1):
            ch_name = f"CHANnel{i}"
            channel_map[ch_name] = InfiniiumChannel(name=ch_name, probe_type="ANALOG")

        return MappingProxyType(channel_map)

    @property
    def num_dig_bits_in_ch(self) -> int:
        """Return the number of digital bits expected in a digital channel."""
        return self._num_dig_bits_in_ch

    @cached_property
    def total_channels(self) -> int:
        """Return the total number of analog channels."""
        return self.NUM_CHANNELS

    @property
    def valid_image_extensions(self) -> tuple[str, ...]:
        """Return valid image extensions for this device."""
        return ".png", ".bmp", ".jpg", ".jpeg"

    def curve_query(
        self,
        channel_num: int,
        wfm_type: str = "TimeDomain",
        output_csv_file: str | os.PathLike[str] | None = None,
    ) -> list[Any]:
        """Perform a curve query on a specific channel.

        Args:
            channel_num: The channel number to query.
            wfm_type: The waveform type (default: "TimeDomain").
            output_csv_file: Optional CSV file path to save data.

        Returns:
            List of waveform data.
        """
        # Set data source
        source = f"CHANnel{channel_num}"
        self.set_and_check(":WAVeform:SOURce", source)

        # Set waveform type
        self.set_and_check(":WAVeform:TYPE", wfm_type)

        # Set data format to binary
        self.set_and_check(":WAVeform:FORMat", "BYTE")

        # Get waveform data
        raw_data = self.query_binary_values(
            ":WAVeform:DATA?",
            datatype="B",
            is_big_endian=True,
        )

        # Get vertical scale info for conversion
        y_increment = float(self.query(":WAVeform:YINCrement?"))
        y_origin = float(self.query(":WAVeform:YORigin?"))
        y_reference = float(self.query(":WAVeform:YREFerence?"))

        # Convert to voltage values
        voltage_data = [(y - y_reference) * y_increment + y_origin for y in raw_data]

        if output_csv_file:
            with Path(output_csv_file).open("w", encoding="UTF-8") as csv_file:
                csv_file.write(",".join(str(v) for v in voltage_data))

        return voltage_data

    def _save_screenshot(
        self,
        filename: Path,
        *,
        colors: str | None,
        view_type: str | None,
        local_folder: Path,
        device_folder: Path,
        keep_device_file: bool = False,
    ) -> None:
        """Capture a screenshot from the device and save it locally.

        Args:
            filename: The name of the file to save the screenshot as.
            colors: The color scheme to use for the screenshot (not used by Infiniium).
            view_type: The type of view to capture (not used by Infiniium).
            local_folder: The local folder to save the screenshot in.
            device_folder: The folder on the device to save the screenshot in (not used).
            keep_device_file: Whether to keep the file on the device after downloading it
                (not used by Infiniium).
        """
        ext = filename.suffix.lower()

        format_map = {
            ".png": "PNG",
            ".bmp": "BMP",
            ".jpg": "JPG",
            ".jpeg": "JPG",
        }
        img_format = format_map[ext]

        self.write(f":DISPlay:DATA? {img_format}")

        img_data = self.read_raw()

        (local_folder / filename).write_bytes(img_data)
