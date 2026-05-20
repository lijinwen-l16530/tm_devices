"""Tests for Keysight Infiniium scope drivers."""

from unittest.mock import MagicMock, PropertyMock

import pytest

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
from tm_devices.drivers.scopes.keysight import KEYSIGHT_SCOPE_MODEL_MAP, KeysightScope
from tm_devices.drivers.scopes.keysight.infiniium import (
    InfiniiumEXR,
    InfiniiumMXR,
    InfiniiumS,
    InfiniiumUXR,
    InfiniiumV,
)
from tm_devices.helpers.functions import get_model_series


class TestKeysightScope:
    """Test class for KeysightScope."""

    def test_keysight_scope_exists(self) -> None:
        """Test KeysightScope class exists."""
        assert KeysightScope is not None

    def test_model_map_keys(self) -> None:
        """Test that model map has all expected entries."""
        expected_keys = ["MSOS", "DSOS", "MSOV", "DSOV", "MXR", "EXR", "UXR"]
        for key in expected_keys:
            assert key in KEYSIGHT_SCOPE_MODEL_MAP, f"Missing key: {key}"

    def test_model_map_values(self) -> None:
        """Test that model map maps to correct class names."""
        assert KEYSIGHT_SCOPE_MODEL_MAP["MSOS"] == "InfiniiumS"
        assert KEYSIGHT_SCOPE_MODEL_MAP["DSOS"] == "InfiniiumS"
        assert KEYSIGHT_SCOPE_MODEL_MAP["MSOV"] == "InfiniiumV"
        assert KEYSIGHT_SCOPE_MODEL_MAP["DSOV"] == "InfiniiumV"
        assert KEYSIGHT_SCOPE_MODEL_MAP["MXR"] == "InfiniiumMXR"
        assert KEYSIGHT_SCOPE_MODEL_MAP["EXR"] == "InfiniiumEXR"
        assert KEYSIGHT_SCOPE_MODEL_MAP["UXR"] == "InfiniiumUXR"

    def test_model_map_size(self) -> None:
        """Test model map has exactly 7 entries."""
        assert len(KEYSIGHT_SCOPE_MODEL_MAP) == 7


class TestInfiniiumSeriesProperties:
    """Test class for Infiniium series-level properties."""

    def test_infiniium_s_series(self) -> None:
        """Test InfiniiumS series property exists."""
        assert hasattr(InfiniiumS, "series")

    def test_infiniium_v_series(self) -> None:
        """Test InfiniiumV has series property."""
        assert hasattr(InfiniiumV, "series")

    def test_infiniium_mxr_max_channels(self) -> None:
        """Test InfiniiumMXR max_channels returns 8."""
        mock_instance = MagicMock(spec=InfiniiumMXR)
        type(mock_instance).max_channels = PropertyMock(return_value=8)
        assert mock_instance.max_channels == 8

    def test_infiniium_exr_max_channels(self) -> None:
        """Test InfiniiumEXR max_channels returns 8."""
        mock_instance = MagicMock(spec=InfiniiumEXR)
        type(mock_instance).max_channels = PropertyMock(return_value=8)
        assert mock_instance.max_channels == 8

    def test_infiniium_s_adc_resolution(self) -> None:
        """Test InfiniiumS get_adc_resolution returns 10."""
        mock_instance = MagicMock(spec=InfiniiumS)
        mock_instance.get_adc_resolution = MagicMock(return_value=10)
        assert mock_instance.get_adc_resolution() == 10

    def test_infiniium_uxr_max_sample_rate(self) -> None:
        """Test InfiniiumUXR get_max_sample_rate exists."""
        assert hasattr(InfiniiumUXR, "get_max_sample_rate")


class TestInfiniiumCommands:
    """Test class for Infiniium command classes."""

    def test_acquire_commands_exist(self) -> None:
        """Test Acquire command classes can be created."""
        cmd = InfiniiumAcquireCommands()
        assert cmd is not None
        assert hasattr(cmd, "mode")
        assert hasattr(cmd, "adc")
        assert hasattr(cmd, "average")
        assert hasattr(cmd, "segmented")
        assert hasattr(cmd, "points")
        assert hasattr(cmd, "srate")

    def test_channel_commands_exist(self) -> None:
        """Test Channel command classes can be created."""
        cmd = InfiniiumChannelCommands(None, 1)
        assert cmd is not None

    def test_display_commands_exist(self) -> None:
        """Test Display command classes can be created."""
        cmd = InfiniiumDisplayCommands()
        assert cmd is not None

    def test_timebase_commands_exist(self) -> None:
        """Test Timebase command classes can be created."""
        cmd = InfiniiumTimebaseCommands()
        assert cmd is not None

    def test_trigger_commands_exist(self) -> None:
        """Test Trigger command classes can be created."""
        cmd = InfiniiumTriggerCommands()
        assert cmd is not None

    def test_waveform_commands_exist(self) -> None:
        """Test Waveform command classes can be created."""
        cmd = InfiniiumWaveformCommands()
        assert cmd is not None

    def test_measure_commands_exist(self) -> None:
        """Test Measure command classes can be created."""
        cmd = InfiniiumMeasureCommands()
        assert cmd is not None

    def test_marker_commands_exist(self) -> None:
        """Test Marker command classes can be created."""
        cmd = InfiniiumMarkerCommands()
        assert cmd is not None


class TestInfiniiumRegexMatching:
    """Test regex matching for Infiniium model names."""

    @pytest.mark.parametrize(
        ("model", "expected"),
        [
            ("DSOS804A", "InfiniiumS"),
            ("MSOS804A", "InfiniiumS"),
            ("DSOS204A", "InfiniiumS"),
            ("MSOS254A", "InfiniiumS"),
            ("DSOV134A", "InfiniiumV"),
            ("MSOV134A", "InfiniiumV"),
            ("DSOV334A", "InfiniiumV"),
            ("MSOV164A", "InfiniiumV"),
            ("MXR104A", "InfiniiumMXR"),
            ("MXR254A", "InfiniiumMXR"),
            ("MXR604A", "InfiniiumMXR"),
            ("MXR058A", "InfiniiumMXR"),
            ("MXR108A", "InfiniiumMXR"),
            ("MXR608A", "InfiniiumMXR"),
            ("EXR204A", "InfiniiumEXR"),
            ("EXR254A", "InfiniiumEXR"),
            ("EXR054A", "InfiniiumEXR"),
            ("EXR108A", "InfiniiumEXR"),
            ("EXR208A", "InfiniiumEXR"),
            ("EXR058A", "InfiniiumEXR"),
            ("UXR0251A", "InfiniiumUXR"),
            ("UXR0501A", "InfiniiumUXR"),
            ("UXR1001A", "InfiniiumUXR"),
            ("UXR1102A", "InfiniiumUXR"),
        ],
    )
    def test_infiniium_model_regex(self, model: str, expected: str) -> None:
        """Test that Infiniium model names are correctly matched."""
        parsed_model = get_model_series(model)
        assert parsed_model == expected, (
            f"Expected {expected} for model {model}, got {parsed_model}"
        )

    @pytest.mark.parametrize(
        "model",
        [
            "DSO4014A",  # Non-Infiniium DSO
            "MSO54",  # Tektronix scope
            "UNKNOWN",  # Unknown model
        ],
    )
    def test_non_infiniium_models(self, model: str) -> None:
        """Test that non-Infiniium models are NOT matched as Infiniium."""
        parsed_model = get_model_series(model)
        assert parsed_model not in KEYSIGHT_SCOPE_MODEL_MAP.values(), (
            f"Model {model} should not match Infiniium"
        )
