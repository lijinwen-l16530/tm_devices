"""Base Keysight scope device driver module."""

from __future__ import annotations

import logging

from abc import ABC

import pyvisa as visa

from tm_devices.driver_mixins.device_control import PIControl
from tm_devices.drivers.scopes.scope import Scope
from tm_devices.helpers import DeviceConfigEntry
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

_logger: logging.Logger = logging.getLogger(__name__)


class KeysightScope(PIControl, Scope, ABC):
    """Base Keysight scope device driver.

    This class contains shared functionality between all Keysight oscilloscope devices.
    """

    def __init__(
        self,
        config_entry: DeviceConfigEntry,
        verbose: bool,
        visa_resource: visa.resources.MessageBasedResource,
        default_visa_timeout: int,
    ) -> None:
        """Create a Keysight scope device.

        Args:
            config_entry: A config entry object parsed by the DMConfigParser.
            verbose: A boolean indicating if verbose output should be printed.
            visa_resource: The VISA resource object.
            default_visa_timeout: The default VISA timeout value in milliseconds.
        """
        super().__init__(config_entry, verbose, visa_resource, default_visa_timeout)
        # Turn off response headers to simplify parsing
        self.write("SYSTem:HEADer OFF", verbose=False)

    @cached_property
    def hostname(self) -> str:
        """Return the hostname of the device."""
        return self.query("SYSTem:COMMunicate:LAN:HOSTname?", verbose=False, remove_quotes=True)

    @property
    def license_list(self) -> tuple[str, ...]:
        """Return the list of licenses installed on the scope."""
        try:
            license_str = self.query("LICense:LIST?", verbose=False, remove_quotes=True)
            licenses = [lic.strip() for lic in license_str.split(",") if lic.strip()]
            return tuple(licenses)
        except Exception:
            _logger.warning("Unable to retrieve license list from %s", self.model)
            return ()

    def clear_status(self) -> None:
        """Clear the device status."""
        self.write("*CLS", verbose=False)

    def wait_for_operation_complete(self) -> None:
        """Wait for operation complete."""
        self.query("*OPC?", verbose=False)
