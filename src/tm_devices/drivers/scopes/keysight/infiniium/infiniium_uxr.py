"""Infiniium UXR Series oscilloscope driver module."""

from __future__ import annotations

import logging

from typing import Any

from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.scopes.keysight.infiniium.infiniium import Infiniium
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

_logger: logging.Logger = logging.getLogger(__name__)


@family_base_class
class InfiniiumUXR(Infiniium):
    """Infiniium UXR Series oscilloscope driver.

    UXR Series features:
    - Ultra-high bandwidth real-time oscilloscope
    - Bandwidth: 5 GHz to 110 GHz
    - Sample rate: Up to 256 GSa/s
    - Memory: Up to 2 Gpts
    - 10-bit or 12-bit ADC (depending on model)
    - 1.0 mm, 1.85 mm, or 3.5 mm connectors
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the Infiniium UXR Series device."""
        super().__init__(*args, **kwargs)
        _logger.debug("Infiniium UXR Series device initialized")

    @cached_property
    def series(self) -> str:
        """Return the series name."""
        return "UXR"

    def get_max_sample_rate(self) -> float:
        """Return the maximum sample rate in GSa/s.

        UXR Series supports up to 256 GSa/s on some models.
        """
        # Return different max sample rate based on model
        model = self.model
        # 3.5 mm connector models: 128 GSa/s
        # 1.85 mm or 1.0 mm connector models: 256 GSa/s
        if any(x in model for x in ["UXR01", "UXR013", "UXR016", "UXR02", "UXR025", "UXR033"]):
            return 128.0
        return 256.0
