"""Infiniium S Series oscilloscope driver module."""

from __future__ import annotations

import logging

from typing import Any

from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.scopes.keysight.infiniium.infiniium import Infiniium
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

_logger: logging.Logger = logging.getLogger(__name__)


@family_base_class
class InfiniiumS(Infiniium):
    """Infiniium S Series oscilloscope driver.

    S Series features:
    - 10-bit ADC for high-definition measurements
    - Bandwidth: 500 MHz to 6 GHz
    - Sample rate: 16 GSa/s
    - Memory: Up to 1.6 Gpts
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the Infiniium S Series device."""
        super().__init__(*args, **kwargs)
        _logger.debug("Infiniium S Series device initialized")

    @cached_property
    def series(self) -> str:
        """Return the series name."""
        return "S"

    def get_adc_resolution(self) -> int:
        """Return the ADC resolution in bits.

        S Series features a 10-bit ADC.
        """
        return 10
