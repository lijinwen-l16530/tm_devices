"""Infiniium EXR Series oscilloscope driver module."""

from __future__ import annotations

import logging

from typing import Any

from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.scopes.keysight.infiniium.infiniium import Infiniium
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

_logger: logging.Logger = logging.getLogger(__name__)


@family_base_class
class InfiniiumEXR(Infiniium):
    """Infiniium EXR Series oscilloscope driver.

    EXR Series features:
    - Cost-effective multi-channel oscilloscope
    - 4 or 8 analog channels
    - Bandwidth: 500 MHz to 2.5 GHz
    - Sample rate: 16 GSa/s
    - Memory: Up to 1.6 Gpts
    - 7-in-1 instrument integration
    """

    # Number of analog channels (4 or 8 depending on model)
    NUM_CHANNELS: int = 8

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the Infiniium EXR Series device."""
        super().__init__(*args, **kwargs)
        _logger.debug("Infiniium EXR Series device initialized")

    @cached_property
    def series(self) -> str:
        """Return the series name."""
        return "EXR"

    @property
    def max_channels(self) -> int:
        """Return the maximum number of analog channels.

        EXR Series supports up to 8 analog channels.
        """
        return 8
