"""Scopes package init file."""

from tm_devices.drivers.scopes.keysight import (
    KeysightScope,
    KEYSIGHT_SCOPE_MODEL_MAP,
)
from tm_devices.drivers.scopes.keysight.infiniium import (
    Infiniium,
    InfiniiumS,
    InfiniiumV,
    InfiniiumMXR,
    InfiniiumEXR,
    InfiniiumUXR,
)

__all__ = [
    # Keysight classes
    "KeysightScope",
    "Infiniium",
    "InfiniiumS",
    "InfiniiumV",
    "InfiniiumMXR",
    "InfiniiumEXR",
    "InfiniiumUXR",
    # Model maps
    "KEYSIGHT_SCOPE_MODEL_MAP",
]
