"""Example usage of Keysight Infiniium oscilloscope with tm_devices.

This example demonstrates the .commands API for Infiniium oscilloscopes,
similar to the Tektronix tm_devices API.
"""

from tm_devices import DeviceManager


def main():
    """Demonstrate basic usage of Keysight Infiniium oscilloscope."""

    # Use DeviceManager to connect to the oscilloscope
    with DeviceManager(verbose=True) as dm:
        # Connect to Infiniium oscilloscope via IP address
        scope = dm.add_scope("TCPIP::192.168.1.100::INSTR")

        # Print device information
        print(f"Connected to: {scope.model}")
        print(f"Series: {scope.series}")

        # =============================================
        # Example 1: Using .commands API
        # =============================================

        # Acquire settings
        scope.commands.acquire.mode.write("RTIME")  # Real-time mode
        scope.commands.acquire.average_count.write(16)  # 16 averages

        # Timebase settings
        scope.commands.timebase.scale.write(1e-3)  # 1 ms/div
        scope.commands.timebase.position.write(0)  # Center position

        # Channel 1 settings
        scope.commands.channel[1].scale.write(0.5)  # 0.5 V/div
        scope.commands.channel[1].offset.write(0)  # 0 V offset
        scope.commands.channel[1].coupling.write("DC")  # DC coupling

        # Trigger settings
        scope.commands.trigger.mode.write("NORMal")  # Normal mode
        scope.commands.trigger.sweep.write("AUTO")  # Auto sweep
        scope.commands.trigger.edge.source.write("CHANnel1")  # Trigger on CH1
        scope.commands.trigger.edge.slope.write("POSitive")  # Rising edge
        scope.commands.trigger.level.write(0)  # 0 V trigger level

        # Waveform settings
        scope.commands.waveform.source.write("CHANnel1")
        scope.commands.waveform.format.write("BYTE")

        # Single acquisition
        scope.commands.acquire.mode.write("SEGMented")  # Switch to segmented
        scope.commands.acquire.segmented.count.write(1)  # Single acquisition

        # Get waveform data using curve_query
        waveform = scope.curve_query(1)
        print(f"Captured {len(waveform)} waveform points")

        # =============================================
        # Example 2: Using .commands API for measurements
        # =============================================

        # Configure measurement
        scope.commands.measure.source.ch1.write("CHANnel1")
        scope.commands.measure.frequency.write("CHANnel1")  # Measure frequency
        scope.commands.measure.vrms.write("CHANnel1")  # Measure RMS voltage
        scope.commands.measure.risetime.write("CHANnel1")  # Measure rise time

        # =============================================
        # Example 3: Using .commands API for markers
        # =============================================

        # Set markers
        scope.commands.marker.mode.write("MANUAL")
        scope.commands.marker.source.write("CHANnel1")
        scope.commands.marker.x1.position.write(0)  # First marker at center

        # =============================================
        # Example 4: Display settings
        # =============================================

        # Control display
        scope.commands.display.intensity.write(50)  # 50% intensity
        scope.commands.display.persist.enable.write("ON")

        # Save screenshot
        scope.save_screenshot("screenshot.png")
        print("Screenshot saved to screenshot.png")

        # =============================================
        # Example 5: Convenience .ch property
        # =============================================

        # Quick channel access using .ch property
        scope.ch[1].scale.write(1.0)  # Set CH1 to 1 V/div
        scope.ch[2].scale.write(0.5)  # Set CH2 to 0.5 V/div
        scope.ch[3].scale.write(0.2)  # Set CH3 to 0.2 V/div
        scope.ch[4].scale.write(0.1)  # Set CH4 to 0.1 V/div

        print("\\nAll examples completed successfully!")


if __name__ == "__main__":
    main()
