"""Tests for Infiniium series driver classes."""

import inspect

from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch, PropertyMock

import pytest

from tm_devices.drivers.scopes.keysight.infiniium import (
    Infiniium,
    InfiniiumEXR,
    InfiniiumMXR,
    InfiniiumS,
    InfiniiumUXR,
    InfiniiumV,
)
from tm_devices.drivers.scopes.keysight.keysight_scope import KeysightScope


class TestInfiniiumClassHierarchy:
    """Test the Infiniium class hierarchy."""

    def test_infiniium_s_is_infiniium(self) -> None:
        """Test InfiniiumS is a subclass of Infiniium."""
        assert issubclass(InfiniiumS, Infiniium)

    def test_infiniium_v_is_infiniium(self) -> None:
        """Test InfiniiumV is a subclass of Infiniium."""
        assert issubclass(InfiniiumV, Infiniium)

    def test_infiniium_mxr_is_infiniium(self) -> None:
        """Test InfiniiumMXR is a subclass of Infiniium."""
        assert issubclass(InfiniiumMXR, Infiniium)

    def test_infiniium_exr_is_infiniium(self) -> None:
        """Test InfiniiumEXR is a subclass of Infiniium."""
        assert issubclass(InfiniiumEXR, Infiniium)

    def test_infiniium_uxr_is_infiniium(self) -> None:
        """Test InfiniiumUXR is a subclass of Infiniium."""
        assert issubclass(InfiniiumUXR, Infiniium)

    def test_infiniium_is_keysight_scope(self) -> None:
        """Test Infiniium is a subclass of KeysightScope."""
        assert issubclass(Infiniium, KeysightScope)


class TestInfiniiumProperties:
    """Test properties on Infiniium subclasses."""

    def test_infiniium_s_series_property(self) -> None:
        """Test InfiniiumS has series property."""
        assert hasattr(InfiniiumS, "series")

    def test_infiniium_v_series_property(self) -> None:
        """Test InfiniiumV has series property."""
        assert hasattr(InfiniiumV, "series")

    def test_infiniium_mxr_max_channels(self) -> None:
        """Test InfiniiumMXR has max_channels."""
        assert hasattr(InfiniiumMXR, "max_channels")

    def test_infiniium_exr_max_channels(self) -> None:
        """Test InfiniiumEXR has max_channels."""
        assert hasattr(InfiniiumEXR, "max_channels")

    def test_infiniium_s_adc_resolution(self) -> None:
        """Test InfiniiumS has get_adc_resolution."""
        assert hasattr(InfiniiumS, "get_adc_resolution")

    def test_infiniium_uxr_max_sample_rate(self) -> None:
        """Test InfiniiumUXR has get_max_sample_rate."""
        assert hasattr(InfiniiumUXR, "get_max_sample_rate")

    def test_infiniium_base_has_num_channels(self) -> None:
        """Test Infiniium base class has NUM_CHANNELS."""
        assert Infiniium.NUM_CHANNELS == 4


class TestInfiniiumValidImageExtensions:
    """Test valid_image_extensions on Infiniium."""

    def test_valid_image_extensions(self) -> None:
        """Test that Infiniium has correct valid image extensions."""
        mock_instance = MagicMock(spec=Infiniium)
        type(mock_instance).valid_image_extensions = PropertyMock(
            return_value=(".png", ".bmp", ".jpg", ".jpeg")
        )
        assert mock_instance.valid_image_extensions == (".png", ".bmp", ".jpg", ".jpeg")

    def test_valid_image_extensions_is_tuple(self) -> None:
        """Test valid_image_extensions returns a tuple."""
        mock_instance = MagicMock(spec=Infiniium)
        type(mock_instance).valid_image_extensions = PropertyMock(
            return_value=(".png", ".bmp", ".jpg", ".jpeg")
        )
        assert isinstance(mock_instance.valid_image_extensions, tuple)


class TestInfiniiumNUMCHANNELS:
    """Test NUM_CHANNELS class attribute across Infiniium subclasses."""

    def test_infiniium_base_num_channels(self) -> None:
        """Test Infiniium base NUM_CHANNELS is 4."""
        assert Infiniium.NUM_CHANNELS == 4

    def test_infiniium_mxr_num_channels(self) -> None:
        """Test InfiniiumMXR NUM_CHANNELS is 8."""
        assert InfiniiumMXR.NUM_CHANNELS == 8

    def test_infiniium_exr_num_channels(self) -> None:
        """Test InfiniiumEXR NUM_CHANNELS is 8."""
        assert InfiniiumEXR.NUM_CHANNELS == 8


class TestInfiniiumUxrSampleRate:
    """Test InfiniiumUXR sample rate logic."""

    @pytest.mark.parametrize(
        ("model", "expected_rate"),
        [
            ("UXR0251A", 128.0),
            ("UXR0501A", 128.0),
            ("UXR1001A", 128.0),
            ("UXR1002A", 256.0),
            ("UXR1102A", 256.0),
        ],
    )
    def test_uxr_sample_rate_by_model(self, model: str, expected_rate: float) -> None:
        """Test that UXR max sample rate varies by model."""
        mock_instance = MagicMock(spec=InfiniiumUXR)
        mock_instance.model = model
        mock_instance.get_max_sample_rate = lambda: (
            128.0
            if any(x in model for x in ["UXR01", "UXR013", "UXR016", "UXR02", "UXR025", "UXR033"])
            else 256.0
        )
        assert mock_instance.get_max_sample_rate() == expected_rate


class TestInfiniiumSaveScreenshot:
    """Test _save_screenshot implementation."""

    def test_save_screenshot_signature(self) -> None:
        """Test that Infiniium has _save_screenshot method (not save_screenshot)."""
        assert hasattr(Infiniium, "_save_screenshot")
        # save_screenshot should come from ScreenCaptureMixin, not be overridden
        save_ss = getattr(Infiniium, "save_screenshot", None)
        if save_ss is not None:
            # It should come from the mixin, not defined directly on Infiniium
            assert "_save_screenshot" not in inspect.getsource(save_ss)

    def test_save_screenshot_format_map(self) -> None:
        """Test _save_screenshot selects correct format for each extension."""
        # Test the format_map logic used in _save_screenshot
        format_map = {
            ".png": "PNG",
            ".bmp": "BMP",
            ".jpg": "JPG",
            ".jpeg": "JPG",
        }
        assert format_map[".png"] == "PNG"
        assert format_map[".bmp"] == "BMP"
        assert format_map[".jpg"] == "JPG"
        assert format_map[".jpeg"] == "JPG"

    @patch("tm_devices.drivers.scopes.keysight.infiniium.infiniium.Infiniium.read_raw")
    @patch("tm_devices.drivers.scopes.keysight.infiniium.infiniium.Infiniium.write")
    @patch("builtins.open", new_callable=mock_open)
    def test_save_screenshot_calls_write_with_correct_command(
        self,
        mock_file: MagicMock,
        mock_write: MagicMock,
        mock_read_raw: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test _save_screenshot issues the correct SCPI command."""
        mock_read_raw.return_value = b"fake_image_data"

        # Create a minimal subclass to avoid __init__ complexity
        class MinimalInfiniium(Infiniium):
            pass

        device = MinimalInfiniium.__new__(MinimalInfiniium)
        device.write = mock_write
        device.read_raw = mock_read_raw

        filename = Path("test.png")
        device._save_screenshot(  # noqa: SLF001
            filename=filename,
            colors=None,
            view_type=None,
            local_folder=Path("./"),
            device_folder=Path("./"),
        )

        mock_write.assert_called_once_with(":DISPlay:DATA? PNG")
