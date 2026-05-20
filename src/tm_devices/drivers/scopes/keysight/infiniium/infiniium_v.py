"""Infiniium V Series oscilloscope driver module."""

from __future__ import annotations

import logging

from typing import Any

from tm_devices.drivers.device import family_base_class
from tm_devices.drivers.scopes.keysight.infiniium.infiniium import Infiniium
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

_logger: logging.Logger = logging.getLogger(__name__)


@family_base_class
class InfiniiumV(Infiniium):
    """Infiniium V Series oscilloscope driver.

    V Series features:
    - High-performance oscilloscope
    - Bandwidth: 8 GHz to 33 GHz
    - Sample rate: 16 GSa/s
    - Memory: Up to 2 Gpts
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the Infiniium V Series device."""
        super().__init__(*args, **kwargs)
        _logger.debug("Infiniium V Series device initialized")

    @cached_property
    def series(self) -> str:
        """Return the series name."""
        return "V"
