"""Keysight oscilloscope drivers."""

from tm_devices.drivers.scopes.keysight.keysight_scope import KeysightScope

# Model prefix to class name mapping for reference/documentation purposes.
# The authoritative driver resolution is handled by the regex-based
# get_model_series() in tm_devices.helpers.functions.
KEYSIGHT_SCOPE_MODEL_MAP = {
    # Infiniium S Series
    "MSOS": "InfiniiumS",
    "DSOS": "InfiniiumS",
    # Infiniium V Series
    "MSOV": "InfiniiumV",
    "DSOV": "InfiniiumV",
    # Infiniium MXR Series
    "MXR": "InfiniiumMXR",
    # Infiniium EXR Series
    "EXR": "InfiniiumEXR",
    # Infiniium UXR Series
    "UXR": "InfiniiumUXR",
}

__all__ = [
    "KEYSIGHT_SCOPE_MODEL_MAP",
    "KeysightScope",
]
