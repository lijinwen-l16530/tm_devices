"""Infiniium MXR Series oscilloscope driver module."""

from __future__ import annotations

import logging

from typing import Any

from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.scopes.keysight.infiniium.infiniium import Infiniium
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

_logger: logging.Logger = logging.getLogger(__name__)


@family_base_class
class InfiniiumMXR(Infiniium):
    """Infiniium MXR Series oscilloscope driver.

    MXR Series features:
    - 8-in-1 instrument integration
    - 4 or 8 analog channels
    - Bandwidth: 500 MHz to 6 GHz
    - Sample rate: 16 GSa/s on all channels
    - Memory: Up to 1.6 Gpts
    - Real-time spectrum analyzer
    """

    # Number of analog channels (4 or 8 depending on model)
    NUM_CHANNELS: int = 8

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the Infiniium MXR Series device."""
        super().__init__(*args, **kwargs)
        _logger.debug("Infiniium MXR Series device initialized")

    @cached_property
    def series(self) -> str:
        """Return the series name."""
        return "MXR"

    @property
    def max_channels(self) -> int:
        """Return the maximum number of analog channels.

        MXR Series supports up to 8 analog channels.
        """
        return 8
