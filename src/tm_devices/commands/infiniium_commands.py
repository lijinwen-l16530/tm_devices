"""The Infiniium series commands module.

Based on Keysight Infiniium SCPI Programmer's Guides (S/V, MXR/EXR, UXR series).
Provides structured access to SCPI command trees via the .commands API,
consistent with the Tektronix tm_devices command pattern.
"""

from typing import TYPE_CHECKING

from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

from .helpers.scpi_commands import BaseSCPICmd, SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


####################################################################################################
# Infiniium Command Tree Classes
####################################################################################################


class InfiniiumAcquireCommands(BaseSCPICmd):
    """The :ACQuire command tree."""

    def __init__(self, device: "PIControl | None" = None) -> None:
        """Initialize the Acquire commands."""
        super().__init__(device, ":ACQuire")
        self._adc = InfiniiumAcquireADCCommands(device, f"{self._cmd_syntax}:ADC")
        self._average = InfiniiumAcquireAverageCommands(device, f"{self._cmd_syntax}:AVERage")
        self._bandwidth = InfiniiumAcquireBandwidthCommands(device, f"{self._cmd_syntax}:BANDwidth")
        self._complete = InfiniiumAcquireCompleteCommands(device, f"{self._cmd_syntax}:COMPlete")
        self._differential = InfiniiumAcquireDifferentialCommands(
            device, f"{self._cmd_syntax}:DIFFerential"
        )
        self._history = InfiniiumAcquireHistoryCommands(device, f"{self._cmd_syntax}:HISTory")
        self._points = InfiniiumAcquirePointsCommands(device, f"{self._cmd_syntax}:POINts")
        self._segmented = InfiniiumAcquireSegmentedCommands(device, f"{self._cmd_syntax}:SEGMented")
        self._srate = InfiniiumAcquireSrateCommands(device, f"{self._cmd_syntax}:SRATe")

    @property
    def adc(self) -> "InfiniiumAcquireADCCommands":
        """Return the :ACQuire:ADC commands."""
        return self._adc

    @property
    def average(self) -> "InfiniiumAcquireAverageCommands":
        """Return the :ACQuire:AVERage commands."""
        return self._average

    @property
    def bandwidth(self) -> "InfiniiumAcquireBandwidthCommands":
        """Return the :ACQuire:BANDwidth commands."""
        return self._bandwidth

    @property
    def complete(self) -> "InfiniiumAcquireCompleteCommands":
        """Return the :ACQuire:COMPlete commands."""
        return self._complete

    @property
    def differential(self) -> "InfiniiumAcquireDifferentialCommands":
        """Return the :ACQuire:DIFFerential commands."""
        return self._differential

    @property
    def history(self) -> "InfiniiumAcquireHistoryCommands":
        """Return the :ACQuire:HISTory commands."""
        return self._history

    @property
    def points(self) -> "InfiniiumAcquirePointsCommands":
        """Return the :ACQuire:POINts commands."""
        return self._points

    @property
    def segmented(self) -> "InfiniiumAcquireSegmentedCommands":
        """Return the :ACQuire:SEGMented commands."""
        return self._segmented

    @property
    def srate(self) -> "InfiniiumAcquireSrateCommands":
        """Return the :ACQuire:SRATe commands."""
        return self._srate

    # Direct commands
    @property
    def adcrest(self) -> SCPICmdWrite:
        """Return the :ACQuire:ADCRes command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:ADCRes")

    @property
    def average_count(self) -> SCPICmdWrite:
        """Return the :ACQuire:AVERage:COUNt command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:AVERage:COUNt")

    @property
    def mode(self) -> SCPICmdWrite:
        """Return the :ACQuire:MODE command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:MODE")

    @property
    def interpolate(self) -> SCPICmdWrite:
        """Return the :ACQuire:INTerpolate command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:INTerpolate")


class InfiniiumAcquireADCCommands(BaseSCPICmd):
    """The :ACQuire:ADC command tree."""

    @property
    def clipped_clear(self) -> SCPICmdWrite:
        """Return the :ACQuire:ADC:CLIPped:CLEar command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:CLIPped:CLEar")


class InfiniiumAcquireAverageCommands(BaseSCPICmd):
    """The :ACQuire:AVERage command tree."""

    @property
    def count(self) -> SCPICmdWrite:
        """Return the :ACQuire:AVERage:COUNt command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:COUNt")


class InfiniiumAcquireBandwidthCommands(BaseSCPICmd):
    """The :ACQuire:BANDwidth command tree."""

    @property
    def frame_query(self) -> SCPICmdRead:
        """Return the :ACQuire:BANDwidth:FRAMe? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:FRAMe")


class InfiniiumAcquireCompleteCommands(BaseSCPICmd):
    """The :ACQuire:COMPlete command tree."""

    @property
    def state(self) -> SCPICmdWrite:
        """Return the :ACQuire:COMPlete:STATe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:STATe")


class InfiniiumAcquireDifferentialCommands(BaseSCPICmd):
    """The :ACQuire:DIFFerential command tree."""

    @property
    def partner(self) -> SCPICmdWrite:
        """Return the :ACQuire:DIFFerential:PARTner command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:PARTner")


class InfiniiumAcquireHistoryCommands(BaseSCPICmd):
    """The :ACQuire:HISTory command tree."""

    @property
    def count(self) -> SCPICmdWrite:
        """Return the :ACQuire:HISTory:COUNt command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:COUNt")

    @property
    def index(self) -> SCPICmdWrite:
        """Return the :ACQuire:HISTory:INDex command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:INDex")


class InfiniiumAcquirePointsCommands(BaseSCPICmd):
    """The :ACQuire:POINts command tree."""

    @property
    def analog(self) -> SCPICmdWrite:
        """Return the :ACQuire:POINts[:ANALog] command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}[:ANALog]")

    @property
    def auto(self) -> SCPICmdWrite:
        """Return the :ACQuire:POINts:AUTO command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:AUTO")

    @property
    def digital_query(self) -> SCPICmdRead:
        """Return the :ACQuire:POINts:DIGital? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:DIGital")


class InfiniiumAcquireSegmentedCommands(BaseSCPICmd):
    """The :ACQuire:SEGMented command tree."""

    @property
    def count(self) -> SCPICmdWrite:
        """Return the :ACQuire:SEGMented:COUNt command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:COUNt")

    @property
    def index(self) -> SCPICmdWrite:
        """Return the :ACQuire:SEGMented:INDex command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:INDex")


class InfiniiumAcquireSrateCommands(BaseSCPICmd):
    """The :ACQuire:SRATe command tree."""

    @property
    def analog(self) -> SCPICmdWrite:
        """Return the :ACQuire:SRATe[:ANALog] command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}[:ANALog]")


####################################################################################################


class InfiniiumChannelCommands(BaseSCPICmd):
    """The :CHANnel<N> command tree for a specific channel."""

    def __init__(self, device: "PIControl | None", channel_number: int) -> None:
        """Initialize the Channel commands.

        Args:
            device: The PIControl device instance.
            channel_number: The channel number (1-8).
        """
        super().__init__(device, f":CHANnel{channel_number}")
        self._channel_number = channel_number
        self._adc = InfiniiumChannelADCCommands(device, f"{self._cmd_syntax}:ADC")
        self._probe = InfiniiumChannelProbeCommands(device, f"{self._cmd_syntax}:PROBe")

    @property
    def adc(self) -> "InfiniiumChannelADCCommands":
        """Return the :CHANnel<N>:ADC commands."""
        return self._adc

    @property
    def probe(self) -> "InfiniiumChannelProbeCommands":
        """Return the :CHANnel<N>:PROBe commands."""
        return self._probe

    # Direct commands
    @property
    def bwlimit(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:BWLimit command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:BWLimit")

    @property
    def display(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:DISPlay command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:DISPlay")

    @property
    def display_auto(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:DISPlay:AUTO command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:DISPlay:AUTO")

    @property
    def display_offset(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:DISPlay:OFFSet command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:DISPlay:OFFSet")

    @property
    def display_range(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:DISPlay:RANGe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:DISPlay:RANGe")

    @property
    def display_scale(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:DISPlay:SCALe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:DISPlay:SCALe")

    @property
    def input(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:INPut command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:INPut")

    @property
    def invert(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:INVert command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:INVert")

    @property
    def offset(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:OFFSet command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:OFFSet")

    @property
    def range(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:RANGe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:RANGe")

    @property
    def scale(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:SCALe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SCALe")

    @property
    def units(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:UNITs command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:UNITs")

    @property
    def label(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:LABel command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:LABel")

    @property
    def coupling(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:PROBe:COUPling command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:PROBe:COUPling")


class InfiniiumChannelADCCommands(BaseSCPICmd):
    """The :CHANnel<N>:ADC command tree."""

    @property
    def clipped(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:ADC:CLIPped command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:CLIPped")


class InfiniiumChannelProbeCommands(BaseSCPICmd):
    """The :CHANnel<N>:PROBe command tree."""

    @property
    def attenuation(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:PROBe:ATTenuation command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:ATTenuation")

    @property
    def coupling(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:PROBe:COUPling command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:COUPling")

    @property
    def id_query(self) -> SCPICmdRead:
        """Return the :CHANnel<N>:PROBe:ID? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:ID")

    @property
    def mode(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:PROBe:MODE command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:MODE")

    @property
    def skew(self) -> SCPICmdWrite:
        """Return the :CHANnel<N>:PROBe:SKEW command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SKEW")

    @property
    def status_query(self) -> SCPICmdRead:
        """Return the :CHANnel<N>:PROBe:STATus? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:STATus")


####################################################################################################


class InfiniiumTimebaseCommands(BaseSCPICmd):
    """The :TIMebase command tree."""

    def __init__(self, device: "PIControl | None" = None) -> None:
        """Initialize the Timebase commands."""
        super().__init__(device, ":TIMebase")
        self._window = InfiniiumTimebaseWindowCommands(device, f"{self._cmd_syntax}:WINDow")

    @property
    def window(self) -> "InfiniiumTimebaseWindowCommands":
        """Return the :TIMebase:WINDow commands."""
        return self._window

    # Direct commands
    @property
    def position(self) -> SCPICmdWrite:
        """Return the :TIMebase:POSition command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:POSition")

    @property
    def range(self) -> SCPICmdWrite:
        """Return the :TIMebase:RANGe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:RANGe")

    @property
    def refclock(self) -> SCPICmdWrite:
        """Return the :TIMebase:REFClock command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:REFClock")

    @property
    def reference(self) -> SCPICmdWrite:
        """Return the :TIMebase:REFerence command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:REFerence")

    @property
    def roll_enable(self) -> SCPICmdWrite:
        """Return the :TIMebase:ROLL:ENABle command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:ROLL:ENABle")

    @property
    def scale(self) -> SCPICmdWrite:
        """Return the :TIMebase:SCALe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SCALe")

    @property
    def view(self) -> SCPICmdWrite:
        """Return the :TIMebase:VIEW command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:VIEW")


class InfiniiumTimebaseWindowCommands(BaseSCPICmd):
    """The :TIMebase:WINDow command tree."""

    @property
    def delay(self) -> SCPICmdWrite:
        """Return the :TIMebase:WINDow:DELay command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:DELay")

    @property
    def position(self) -> SCPICmdWrite:
        """Return the :TIMebase:WINDow:POSition command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:POSition")

    @property
    def range(self) -> SCPICmdWrite:
        """Return the :TIMebase:WINDow:RANGe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:RANGe")

    @property
    def scale(self) -> SCPICmdWrite:
        """Return the :TIMebase:WINDow:SCALe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SCALe")


####################################################################################################


class InfiniiumTriggerCommands(BaseSCPICmd):
    """The :TRIGger command tree."""

    def __init__(self, device: "PIControl | None" = None) -> None:
        """Initialize the Trigger commands."""
        super().__init__(device, ":TRIGger")
        self._and = InfiniiumTriggerAndCommands(device, f"{self._cmd_syntax}:AND")
        self._delay = InfiniiumTriggerDelayCommands(device, f"{self._cmd_syntax}:DELay")
        self._eburst = InfiniiumTriggerEburstCommands(device, f"{self._cmd_syntax}:EBURst")
        self._edge = InfiniiumTriggerEdgeCommands(device, f"{self._cmd_syntax}:EDGE")
        self._glitch = InfiniiumTriggerGlitchCommands(device, f"{self._cmd_syntax}:GLITch")
        self._pwidth = InfiniiumTriggerPwidthCommands(device, f"{self._cmd_syntax}:PWIDth")
        self._runt = InfiniiumTriggerRuntCommands(device, f"{self._cmd_syntax}:RUNT")
        self._timeout = InfiniiumTriggerTimeoutCommands(device, f"{self._cmd_syntax}:TIMeout")
        self._transition = InfiniiumTriggerTransitionCommands(
            device, f"{self._cmd_syntax}:TRANsition"
        )
        self._window = InfiniiumTriggerWindowCommands(device, f"{self._cmd_syntax}:WINDow")

    @property
    def and_cmd(self) -> "InfiniiumTriggerAndCommands":
        """Return the :TRIGger:AND commands."""
        return self._and

    @property
    def delay(self) -> "InfiniiumTriggerDelayCommands":
        """Return the :TRIGger:DELay commands."""
        return self._delay

    @property
    def eburst(self) -> "InfiniiumTriggerEburstCommands":
        """Return the :TRIGger:EBURst commands."""
        return self._eburst

    @property
    def edge(self) -> "InfiniiumTriggerEdgeCommands":
        """Return the :TRIGger:EDGE commands."""
        return self._edge

    @property
    def glitch(self) -> "InfiniiumTriggerGlitchCommands":
        """Return the :TRIGger:GLITch commands."""
        return self._glitch

    @property
    def pwidth(self) -> "InfiniiumTriggerPwidthCommands":
        """Return the :TRIGger:PWIDth commands."""
        return self._pwidth

    @property
    def runt(self) -> "InfiniiumTriggerRuntCommands":
        """Return the :TRIGger:RUNT commands."""
        return self._runt

    @property
    def timeout(self) -> "InfiniiumTriggerTimeoutCommands":
        """Return the :TRIGger:TIMeout commands."""
        return self._timeout

    @property
    def transition(self) -> "InfiniiumTriggerTransitionCommands":
        """Return the :TRIGger:TRANsition commands."""
        return self._transition

    @property
    def window(self) -> "InfiniiumTriggerWindowCommands":
        """Return the :TRIGger:WINDow commands."""
        return self._window

    # Direct commands
    @property
    def force(self) -> SCPICmdWrite:
        """Return the :TRIGger:FORCe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:FORCe")

    @property
    def high(self) -> SCPICmdWrite:
        """Return the :TRIGger:HIGH command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:HIGH")

    @property
    def holdoff(self) -> SCPICmdWrite:
        """Return the :TRIGger:HOLDoff command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:HOLDoff")

    @property
    def hysteresis(self) -> SCPICmdWrite:
        """Return the :TRIGger:HYSTeresis command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:HYSTeresis")

    @property
    def level(self) -> SCPICmdWrite:
        """Return the :TRIGger:LEVel command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:LEVel")

    @property
    def level_fifty(self) -> SCPICmdWrite:
        """Return the :TRIGger:LEVel:FIFTy command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:LEVel:FIFTy")

    @property
    def low(self) -> SCPICmdWrite:
        """Return the :TRIGger:LOW command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:LOW")

    @property
    def mode(self) -> SCPICmdWrite:
        """Return the :TRIGger:MODE command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:MODE")

    @property
    def sweep(self) -> SCPICmdWrite:
        """Return the :TRIGger:SWEep command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SWEep")


class InfiniiumTriggerAndCommands(BaseSCPICmd):
    """The :TRIGger:AND command tree."""

    @property
    def enable(self) -> SCPICmdWrite:
        """Return the :TRIGger:AND:ENABle command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:ENABle")

    @property
    def source(self) -> SCPICmdWrite:
        """Return the :TRIGger:AND:SOURce command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SOURce")


class InfiniiumTriggerDelayCommands(BaseSCPICmd):
    """The :TRIGger:DELay command tree."""

    @property
    def mode(self) -> SCPICmdWrite:
        """Return the :TRIGger:DELay:MODE command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:MODE")

    @property
    def time(self) -> SCPICmdWrite:
        """Return the :TRIGger:DELay:TDELay:TIME command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:TDELay:TIME")


class InfiniiumTriggerEburstCommands(BaseSCPICmd):
    """The :TRIGger:EBURst command tree."""

    @property
    def count(self) -> SCPICmdWrite:
        """Return the :TRIGger:EBURst:COUNt command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:COUNt")

    @property
    def idle(self) -> SCPICmdWrite:
        """Return the :TRIGger:EBURst:IDLE command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:IDLE")

    @property
    def slope(self) -> SCPICmdWrite:
        """Return the :TRIGger:EBURst:SLOPe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SLOPe")

    @property
    def source(self) -> SCPICmdWrite:
        """Return the :TRIGger:EBURst:SOURce command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SOURce")


class InfiniiumTriggerEdgeCommands(BaseSCPICmd):
    """The :TRIGger:EDGE command tree."""

    @property
    def coupling(self) -> SCPICmdWrite:
        """Return the :TRIGger:EDGE:COUPling command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:COUPling")

    @property
    def slope(self) -> SCPICmdWrite:
        """Return the :TRIGger:EDGE:SLOPe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SLOPe")

    @property
    def source(self) -> SCPICmdWrite:
        """Return the :TRIGger:EDGE:SOURce command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SOURce")


class InfiniiumTriggerGlitchCommands(BaseSCPICmd):
    """The :TRIGger:GLITch command tree."""

    @property
    def polarity(self) -> SCPICmdWrite:
        """Return the :TRIGger:GLITch:POLarity command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:POLarity")

    @property
    def source(self) -> SCPICmdWrite:
        """Return the :TRIGger:GLITch:SOURce command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SOURce")

    @property
    def width(self) -> SCPICmdWrite:
        """Return the :TRIGger:GLITch:WIDTh command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:WIDTh")


class InfiniiumTriggerPwidthCommands(BaseSCPICmd):
    """The :TRIGger:PWIDth command tree."""

    @property
    def polarity(self) -> SCPICmdWrite:
        """Return the :TRIGger:PWIDth:POLarity command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:POLarity")

    @property
    def range(self) -> SCPICmdWrite:
        """Return the :TRIGger:PWIDth:RANGe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:RANGe")

    @property
    def source(self) -> SCPICmdWrite:
        """Return the :TRIGger:PWIDth:SOURce command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SOURce")

    @property
    def width(self) -> SCPICmdWrite:
        """Return the :TRIGger:PWIDth:WIDTh command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:WIDTh")


class InfiniiumTriggerRuntCommands(BaseSCPICmd):
    """The :TRIGger:RUNT command tree."""

    @property
    def polarity(self) -> SCPICmdWrite:
        """Return the :TRIGger:RUNT:POLarity command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:POLarity")

    @property
    def qualified(self) -> SCPICmdWrite:
        """Return the :TRIGger:RUNT:QUALified command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:QUALified")

    @property
    def source(self) -> SCPICmdWrite:
        """Return the :TRIGger:RUNT:SOURce command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SOURce")

    @property
    def time(self) -> SCPICmdWrite:
        """Return the :TRIGger:RUNT:TIME command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:TIME")


class InfiniiumTriggerTimeoutCommands(BaseSCPICmd):
    """The :TRIGger:TIMeout command tree."""

    @property
    def condition(self) -> SCPICmdWrite:
        """Return the :TRIGger:TIMeout:CONDition command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:CONDition")

    @property
    def source(self) -> SCPICmdWrite:
        """Return the :TRIGger:TIMeout:SOURce command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SOURce")

    @property
    def time(self) -> SCPICmdWrite:
        """Return the :TRIGger:TIMeout:TIME command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:TIME")


class InfiniiumTriggerTransitionCommands(BaseSCPICmd):
    """The :TRIGger:TRANsition command tree."""

    @property
    def mode(self) -> SCPICmdWrite:
        """Return the :TRIGger:TRANsition:MODE command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:MODE")

    @property
    def range(self) -> SCPICmdWrite:
        """Return the :TRIGger:TRANsition:RANGe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:RANGe")

    @property
    def source(self) -> SCPICmdWrite:
        """Return the :TRIGger:TRANsition:SOURce command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SOURce")

    @property
    def time(self) -> SCPICmdWrite:
        """Return the :TRIGger:TRANsition:TIME command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:TIME")


class InfiniiumTriggerWindowCommands(BaseSCPICmd):
    """The :TRIGger:WINDow command tree."""

    @property
    def condition(self) -> SCPICmdWrite:
        """Return the :TRIGger:WINDow:CONDition command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:CONDition")

    @property
    def source(self) -> SCPICmdWrite:
        """Return the :TRIGger:WINDow:SOURce command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SOURce")

    @property
    def time(self) -> SCPICmdWrite:
        """Return the :TRIGger:WINDow:TIME command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:TIME")


####################################################################################################


class InfiniiumWaveformCommands(BaseSCPICmd):
    """The :WAVeform command tree."""

    def __init__(self, device: "PIControl | None" = None) -> None:
        """Initialize the Waveform commands."""
        super().__init__(device, ":WAVeform")
        self._stream = InfiniiumWaveformStreamCommands(device, f"{self._cmd_syntax}:STReam")

    @property
    def stream(self) -> "InfiniiumWaveformStreamCommands":
        """Return the :WAVeform:STReam commands."""
        return self._stream

    # Direct commands
    @property
    def auto(self) -> SCPICmdWrite:
        """Return the :WAVeform:AUTO command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:AUTO")

    @property
    def bchannel(self) -> SCPICmdWrite:
        """Return the :WAVeform:BCHannel command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:BCHannel")

    @property
    def bps(self) -> SCPICmdWrite:
        """Return the :WAVeform:BPS command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:BPS")

    @property
    def byteorder(self) -> SCPICmdWrite:
        """Return the :WAVeform:BYTEOrder command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:BYTEOrder")

    @property
    def columns(self) -> SCPICmdWrite:
        """Return the :WAVeform:COLumns command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:COLumns")

    @property
    def count_query(self) -> SCPICmdRead:
        """Return the :WAVeform:COUNt? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:COUNt")

    @property
    def data(self) -> SCPICmdRead:
        """Return the :WAVeform:DATA? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:DATA")

    @property
    def decimfilter(self) -> SCPICmdWrite:
        """Return the :WAVeform:DECimfilter command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:DECimfilter")

    @property
    def encdading(self) -> SCPICmdWrite:
        """Return the :WAVeform:ENCDading command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:ENCDading")

    @property
    def format(self) -> SCPICmdWrite:
        """Return the :WAVeform:FORMat command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:FORMat")

    @property
    def frame_count(self) -> SCPICmdRead:
        """Return the :WAVeform:FRAMe:COUNt? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:FRAMe:COUNt")

    @property
    def frame_current(self) -> SCPICmdWrite:
        """Return the :WAVeform:FRAMe:CURRent command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:FRAMe:CURRent")

    @property
    def frame_index(self) -> SCPICmdWrite:
        """Return the :WAVeform:FRAMe:INDex command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:FRAMe:INDex")

    @property
    def frame_stride(self) -> SCPICmdWrite:
        """Return the :WAVeform:FRAMe:STRide command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:FRAMe:STRide")

    @property
    def header(self) -> SCPICmdWrite:
        """Return the :WAVeform:HEADer command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:HEADer")

    @property
    def point_format(self) -> SCPICmdWrite:
        """Return the :WAVeform:POINts:FORMat command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:POINts:FORMat")

    @property
    def points_mode(self) -> SCPICmdWrite:
        """Return the :WAVeform:POINts:MODE command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:POINts:MODE")

    @property
    def points_total(self) -> SCPICmdRead:
        """Return the :WAVeform:POINts? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:POINts")

    @property
    def preamble_query(self) -> SCPICmdRead:
        """Return the :WAVeform:PREamble? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:PREamble")

    @property
    def rows(self) -> SCPICmdWrite:
        """Return the :WAVeform:ROWS command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:ROWS")

    @property
    def segment(self) -> SCPICmdWrite:
        """Return the :WAVeform:SEGMented:INDex command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SEGMented:INDex")

    @property
    def source(self) -> SCPICmdWrite:
        """Return the :WAVeform:SOURce command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SOURce")

    @property
    def sparse(self) -> SCPICmdWrite:
        """Return the :WAVeform:SPARse command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SPARse")

    @property
    def type(self) -> SCPICmdWrite:
        """Return the :WAVeform:TYPE command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:TYPE")

    @property
    def units(self) -> SCPICmdRead:
        """Return the :WAVeform:UNITs? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:UNITs")

    @property
    def view(self) -> SCPICmdWrite:
        """Return the :WAVeform:VIEW command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:VIEW")

    @property
    def xincreament(self) -> SCPICmdRead:
        """Return the :WAVeform:XINCrement? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:XINCrement")

    @property
    def xorigin(self) -> SCPICmdRead:
        """Return the :WAVeform:XORigin? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:XORigin")

    @property
    def xreference(self) -> SCPICmdRead:
        """Return the :WAVeform:XREFerence? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:XREFerence")

    @property
    def yincreament(self) -> SCPICmdRead:
        """Return the :WAVeform:YINCrement? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:YINCrement")

    @property
    def yorigin(self) -> SCPICmdRead:
        """Return the :WAVeform:YORigin? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:YORigin")

    @property
    def yreference(self) -> SCPICmdRead:
        """Return the :WAVeform:YREFerence? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:YREFerence")


class InfiniiumWaveformStreamCommands(BaseSCPICmd):
    """The :WAVeform:STReam command tree."""

    @property
    def enable(self) -> SCPICmdWrite:
        """Return the :WAVeform:STReam:ENABle command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:ENABle")

    @property
    def format(self) -> SCPICmdWrite:
        """Return the :WAVeform:STReam:FORMat command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:FORMat")

    @property
    def mode(self) -> SCPICmdWrite:
        """Return the :WAVeform:STReam:MODE command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:MODE")

    @property
    def protocol(self) -> SCPICmdWrite:
        """Return the :WAVeform:STReam:PROTocol command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:PROTocol")


####################################################################################################


class InfiniiumMeasureCommands(BaseSCPICmd):
    """The :MEASure command tree."""

    def __init__(self, device: "PIControl | None" = None) -> None:
        """Initialize the Measure commands."""
        super().__init__(device, ":MEASure")
        self._clear = InfiniiumMeasureClearCommands(device, f"{self._cmd_syntax}:CLEar")
        self._delay = InfiniiumMeasureDelayCommands(device, f"{self._cmd_syntax}:DELay")
        self._filter = InfiniiumMeasureFilterCommands(device, f"{self._cmd_syntax}:FILTer")
        self._histogram = InfiniiumMeasureHistogramCommands(device, f"{self._cmd_syntax}:HISTogram")
        self._noise = InfiniiumMeasureNoiseCommands(device, f"{self._cmd_syntax}:NOISe")
        self._result = InfiniiumMeasureResultCommands(device, f"{self._cmd_syntax}:RESult")
        self._scope = InfiniiumMeasureScopeCommands(device, f"{self._cmd_syntax}:SCOPe")
        self._setup = InfiniiumMeasureSetupCommands(device, f"{self._cmd_syntax}:SETup")
        self._source = InfiniiumMeasureSourceCommands(device, f"{self._cmd_syntax}:SOURce")

    @property
    def clear(self) -> "InfiniiumMeasureClearCommands":
        """Return the :MEASure:CLEar commands."""
        return self._clear

    @property
    def delay(self) -> "InfiniiumMeasureDelayCommands":
        """Return the :MEASure:DELay commands."""
        return self._delay

    @property
    def filter(self) -> "InfiniiumMeasureFilterCommands":
        """Return the :MEASure:FILTer commands."""
        return self._filter

    @property
    def histogram(self) -> "InfiniiumMeasureHistogramCommands":
        """Return the :MEASure:HISTogram commands."""
        return self._histogram

    @property
    def noise(self) -> "InfiniiumMeasureNoiseCommands":
        """Return the :MEASure:NOISe commands."""
        return self._noise

    @property
    def result(self) -> "InfiniiumMeasureResultCommands":
        """Return the :MEASure:RESult commands."""
        return self._result

    @property
    def scope(self) -> "InfiniiumMeasureScopeCommands":
        """Return the :MEASure:SCOPe commands."""
        return self._scope

    @property
    def setup(self) -> "InfiniiumMeasureSetupCommands":
        """Return the :MEASure:SETup commands."""
        return self._setup

    @property
    def source(self) -> "InfiniiumMeasureSourceCommands":
        """Return the :MEASure:SOURce commands."""
        return self._source

    # Direct commands
    @property
    def area(self) -> SCPICmdWrite:
        """Return the :MEASure:AREA command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:AREA")

    @property
    def dutycycle(self) -> SCPICmdWrite:
        """Return the :MEASure:DUTYcycle command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:DUTYcycle")

    @property
    def envelope(self) -> SCPICmdWrite:
        """Return the :MEASure:ENVelope command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:ENVelope")

    @property
    def falltime(self) -> SCPICmdWrite:
        """Return the :MEASure:FALLtime command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:FALLtime")

    @property
    def frequency(self) -> SCPICmdWrite:
        """Return the :MEASure:FREQuency command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:FREQuency")

    @property
    def fwidth(self) -> SCPICmdWrite:
        """Return the :MEASure:FWIDth command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:FWIDth")

    @property
    def lascatter(self) -> SCPICmdWrite:
        """Return the :MEASure:LAScatter command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:LAScatter")

    @property
    def lowpass(self) -> SCPICmdWrite:
        """Return the :MEASure:LOWPass command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:LOWPass")

    @property
    def narrowband(self) -> SCPICmdWrite:
        """Return the :MEASure:NARRowband command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:NARRowband")

    @property
    def npwidth(self) -> SCPICmdWrite:
        """Return the :MEASure:NPWIdth command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:NPWIdth")

    @property
    def nwidth(self) -> SCPICmdWrite:
        """Return the :MEASure:NWIDth command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:NWIDth")

    @property
    def overshoot(self) -> SCPICmdWrite:
        """Return the :MEASure:OVERshoot command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:OVERshoot")

    @property
    def period(self) -> SCPICmdWrite:
        """Return the :MEASure:PERiod command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:PERiod")

    @property
    def phase(self) -> SCPICmdWrite:
        """Return the :MEASure:PHASe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:PHASe")

    @property
    def pkpk(self) -> SCPICmdWrite:
        """Return the :MEASure:PK2Pk command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:PK2Pk")

    @property
    def powerma(self) -> SCPICmdWrite:
        """Return the :MEASure:POWerma command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:POWerma")

    @property
    def powerrms(self) -> SCPICmdWrite:
        """Return the :MEASure:POWERrms command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:POWERrms")

    @property
    def preshoot(self) -> SCPICmdWrite:
        """Return the :MEASure:PREShoot command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:PREShoot")

    @property
    def pwidth(self) -> SCPICmdWrite:
        """Return the :MEASure:PWIDth command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:PWIDth")

    @property
    def qfactor(self) -> SCPICmdWrite:
        """Return the :MEASure:QFACtor command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:QFACtor")

    @property
    def risetime(self) -> SCPICmdWrite:
        """Return the :MEASure:RISetime command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:RISetime")

    @property
    def rms(self) -> SCPICmdWrite:
        """Return the :MEASure:RMS command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:RMS")

    @property
    def rmsj(self) -> SCPICmdWrite:
        """Return the :MEASure:RMSJ command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:RMSJ")

    @property
    def rmsu(self) -> SCPICmdWrite:
        """Return the :MEASure:RMSU command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:RMSU")

    @property
    def snrratio(self) -> SCPICmdWrite:
        """Return the :MEASure:SNR command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SNR")

    @property
    def sourcetype(self) -> SCPICmdWrite:
        """Return the :MEASure:SOURcetype command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SOURcetype")

    @property
    def statistic_result(self) -> SCPICmdRead:
        """Return the :MEASure:STATistic:RESult? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:STATistic:RESult")

    @property
    def statistic_summary(self) -> SCPICmdWrite:
        """Return the :MEASure:STATistic:SUMMary command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:STATistic:SUMMary")

    @property
    def vaverage(self) -> SCPICmdWrite:
        """Return the :MEASure:VAVerage command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:VAVerage")

    @property
    def vbas(self) -> SCPICmdWrite:
        """Return the :MEASure:VBAS command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:VBAS")

    @property
    def vmax(self) -> SCPICmdWrite:
        """Return the :MEASure:VMAX command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:VMAX")

    @property
    def vmid(self) -> SCPICmdWrite:
        """Return the :MEASure:VMID command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:VMID")

    @property
    def vmin(self) -> SCPICmdWrite:
        """Return the :MEASure:VMIN command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:VMIN")

    @property
    def vpp(self) -> SCPICmdWrite:
        """Return the :MEASure:VPP command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:VPP")

    @property
    def vrms(self) -> SCPICmdWrite:
        """Return the :MEASure:VRMS command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:VRMS")

    @property
    def vtop(self) -> SCPICmdWrite:
        """Return the :MEASure:VTOP command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:VTOP")


class InfiniiumMeasureClearCommands(BaseSCPICmd):
    """The :MEASure:CLEar command tree."""

    @property
    def all(self) -> SCPICmdWrite:
        """Return the :MEASure:CLEar:ALL command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:ALL")


class InfiniiumMeasureDelayCommands(BaseSCPICmd):
    """The :MEASure:DELay command tree."""

    @property
    def deflection(self) -> SCPICmdWrite:
        """Return the :MEASure:DELay:DEFlection command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:DEFlection")

    @property
    def direction(self) -> SCPICmdWrite:
        """Return the :MEASure:DELay:DIRection command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:DIRection")

    @property
    def edge1(self) -> SCPICmdWrite:
        """Return the :MEASure:DELay:EDGE1 command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:EDGE1")

    @property
    def edge2(self) -> SCPICmdWrite:
        """Return the :MEASure:DELay:EDGE2 command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:EDGE2")

    @property
    def hold(self) -> SCPICmdWrite:
        """Return the :MEASure:DELay:HOLD command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:HOLD")


class InfiniiumMeasureFilterCommands(BaseSCPICmd):
    """The :MEASure:FILTer command tree."""

    @property
    def bwidth(self) -> SCPICmdWrite:
        """Return the :MEASure:FILTer:BWIDth command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:BWIDth")

    @property
    def lpass(self) -> SCPICmdWrite:
        """Return the :MEASure:FILTer:LPASs command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:LPASs")

    @property
    def type(self) -> SCPICmdWrite:
        """Return the :MEASure:FILTer:TYPE command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:TYPE")


class InfiniiumMeasureHistogramCommands(BaseSCPICmd):
    """The :MEASure:HISTogram command tree."""

    @property
    def clippedsource(self) -> SCPICmdWrite:
        """Return the :MEASure:HISTogram:CLIPped:SOURce command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:CLIPped:SOURce")


class InfiniiumMeasureNoiseCommands(BaseSCPICmd):
    """The :MEASure:NOISe command tree."""

    @property
    def bandwidth(self) -> SCPICmdWrite:
        """Return the :MEASure:NOISe:BANDwidth command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:BANDwidth")

    @property
    def erj(self) -> SCPICmdWrite:
        """Return the :MEASure:NOISe:ERJ command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:ERJ")

    @property
    def method(self) -> SCPICmdWrite:
        """Return the :MEASure:NOISe:METHod command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:METHod")


class InfiniiumMeasureResultCommands(BaseSCPICmd):
    """The :MEASure:RESult command tree."""

    @property
    def area(self) -> SCPICmdRead:
        """Return the :MEASure:RESult:AREA? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:AREA")

    @property
    def mean(self) -> SCPICmdRead:
        """Return the :MEASure:RESult:MEAN? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:MEAN")


class InfiniiumMeasureScopeCommands(BaseSCPICmd):
    """The :MEASure:SCOPe command tree."""

    @property
    def mode(self) -> SCPICmdWrite:
        """Return the :MEASure:SCOPe:MODE command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:MODE")


class InfiniiumMeasureSetupCommands(BaseSCPICmd):
    """The :MEASure:SETup command tree."""

    @property
    def ampedge(self) -> SCPICmdWrite:
        """Return the :MEASure:SETup:AMPedge command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:AMPedge")

    @property
    def delay(self) -> SCPICmdWrite:
        """Return the :MEASure:SETup:DELay command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:DELay")

    @property
    def direction(self) -> SCPICmdWrite:
        """Return the :MEASure:SETup:DIRection command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:DIRection")

    @property
    def edgenumber(self) -> SCPICmdWrite:
        """Return the :MEASure:SETup:EDGENumber command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:EDGENumber")

    @property
    def holdoff(self) -> SCPICmdWrite:
        """Return the :MEASure:SETup:HOLDoff command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:HOLDoff")

    @property
    def polarity(self) -> SCPICmdWrite:
        """Return the :MEASure:SETup:POLarity command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:POLarity")

    @property
    def qualifier(self) -> SCPICmdWrite:
        """Return the :MEASure:SETup:QUALifier command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:QUALifier")

    @property
    def sourcetype(self) -> SCPICmdWrite:
        """Return the :MEASure:SETup:SOURcetype command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SOURcetype")

    @property
    def threshold(self) -> SCPICmdWrite:
        """Return the :MEASure:SETup:THReshold command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:THReshold")

    @property
    def width(self) -> SCPICmdWrite:
        """Return the :MEASure:SETup:WIDTh command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:WIDTh")


class InfiniiumMeasureSourceCommands(BaseSCPICmd):
    """The :MEASure:SOURce command tree."""

    @property
    def ch1(self) -> SCPICmdWrite:
        """Return the :MEASure:SOURce:CH1 command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:CH1")

    @property
    def ch2(self) -> SCPICmdWrite:
        """Return the :MEASure:SOURce:CH2 command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:CH2")


####################################################################################################


class InfiniiumDisplayCommands(BaseSCPICmd):
    """The :DISPlay command tree."""

    def __init__(self, device: "PIControl | None" = None) -> None:
        """Initialize the Display commands."""
        super().__init__(device, ":DISPlay")
        self._annotation = InfiniiumDisplayAnnotationCommands(device, f"{self._cmd_syntax}:ANN")
        self._grid = InfiniiumDisplayGridCommands(device, f"{self._cmd_syntax}:GRID")
        self._label = InfiniiumDisplayLabelCommands(device, f"{self._cmd_syntax}:LABel")
        self._menubar = InfiniiumDisplayMenubarCommands(device, f"{self._cmd_syntax}:MENUBar")
        self._persist = InfiniiumDisplayPersistCommands(device, f"{self._cmd_syntax}:PERSist")
        self._setup = InfiniiumDisplaySetupCommands(device, f"{self._cmd_syntax}:SETup")
        self._style = InfiniiumDisplayStyleCommands(device, f"{self._cmd_syntax}:STYLe")
        self._toolbar = InfiniiumDisplayToolbarCommands(device, f"{self._cmd_syntax}:TOOLbar")
        self._vector = InfiniiumDisplayVectorCommands(device, f"{self._cmd_syntax}:VECTor")

    @property
    def annotation(self) -> "InfiniiumDisplayAnnotationCommands":
        """Return the :DISPlay:ANN commands."""
        return self._annotation

    @property
    def grid(self) -> "InfiniiumDisplayGridCommands":
        """Return the :DISPlay:GRID commands."""
        return self._grid

    @property
    def label(self) -> "InfiniiumDisplayLabelCommands":
        """Return the :DISPlay:LABel commands."""
        return self._label

    @property
    def menubar(self) -> "InfiniiumDisplayMenubarCommands":
        """Return the :DISPlay:MENUBar commands."""
        return self._menubar

    @property
    def persist(self) -> "InfiniiumDisplayPersistCommands":
        """Return the :DISPlay:PERSist commands."""
        return self._persist

    @property
    def setup(self) -> "InfiniiumDisplaySetupCommands":
        """Return the :DISPlay:SETup commands."""
        return self._setup

    @property
    def style(self) -> "InfiniiumDisplayStyleCommands":
        """Return the :DISPlay:STYLe commands."""
        return self._style

    @property
    def toolbar(self) -> "InfiniiumDisplayToolbarCommands":
        """Return the :DISPlay:TOOLbar commands."""
        return self._toolbar

    @property
    def vector(self) -> "InfiniiumDisplayVectorCommands":
        """Return the :DISPlay:VECTor commands."""
        return self._vector

    # Direct commands
    @property
    def clear(self) -> SCPICmdWrite:
        """Return the :DISPlay:CLEar command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:CLEar")

    @property
    def data(self) -> SCPICmdRead:
        """Return the :DISPlay:DATA? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:DATA")

    @property
    def intensity(self) -> SCPICmdWrite:
        """Return the :DISPlay:INTensity command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:INTensity")

    @property
    def message(self) -> SCPICmdWrite:
        """Return the :DISPlay:MESSage command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:MESSage")

    @property
    def name(self) -> SCPICmdWrite:
        """Return the :DISPlay:NAME command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:NAME")


class InfiniiumDisplayAnnotationCommands(BaseSCPICmd):
    """The :DISPlay:ANN command tree."""

    @property
    def amplitude(self) -> SCPICmdWrite:
        """Return the :DISPlay:ANN:AMPLitude command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:AMPLitude")

    @property
    def cartesian(self) -> SCPICmdWrite:
        """Return the :DISPlay:ANN:CARTesian command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:CARTesian")

    @property
    def clear(self) -> SCPICmdWrite:
        """Return the :DISPlay:ANN:CLEar command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:CLEar")

    @property
    def frequency(self) -> SCPICmdWrite:
        """Return the :DISPlay:ANN:FREQuency command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:FREQuency")


class InfiniiumDisplayGridCommands(BaseSCPICmd):
    """The :DISPlay:GRID command tree."""

    @property
    def align(self) -> SCPICmdWrite:
        """Return the :DISPlay:GRID:ALIGn command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:ALIGn")

    @property
    def division(self) -> SCPICmdWrite:
        """Return the :DISPlay:GRID:DIVision command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:DIVision")

    @property
    def frame(self) -> SCPICmdWrite:
        """Return the :DISPlay:GRID:FRAMe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:FRAMe")

    @property
    def layout(self) -> SCPICmdWrite:
        """Return the :DISPlay:GRID:LAYout command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:LAYout")

    @property
    def style(self) -> SCPICmdWrite:
        """Return the :DISPlay:GRID:STYLe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:STYLe")


class InfiniiumDisplayLabelCommands(BaseSCPICmd):
    """The :DISPlay:LABel command tree."""

    @property
    def add(self) -> SCPICmdWrite:
        """Return the :DISPlay:LABel:ADD command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:ADD")

    @property
    def background(self) -> SCPICmdWrite:
        """Return the :DISPlay:LABel:BACKground command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:BACKground")

    @property
    def box(self) -> SCPICmdWrite:
        """Return the :DISPlay:LABel:BOX command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:BOX")

    @property
    def boxcolor(self) -> SCPICmdWrite:
        """Return the :DISPlay:LABel:BOXColor command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:BOXColor")

    @property
    def delete(self) -> SCPICmdWrite:
        """Return the :DISPlay:LABel:DELEte command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:DELEte")

    @property
    def font(self) -> SCPICmdWrite:
        """Return the :DISPlay:LABel:FONT command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:FONT")

    @property
    def list(self) -> SCPICmdRead:
        """Return the :DISPlay:LABel:LIST? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:LIST")

    @property
    def name(self) -> SCPICmdWrite:
        """Return the :DISPlay:LABel:NAME command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:NAME")

    @property
    def show(self) -> SCPICmdWrite:
        """Return the :DISPlay:LABel:SHOW command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SHOW")

    @property
    def textcolor(self) -> SCPICmdWrite:
        """Return the :DISPlay:LABel:TEXtcolor command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:TEXtcolor")


class InfiniiumDisplayMenubarCommands(BaseSCPICmd):
    """The :DISPlay:MENUBar command tree."""

    @property
    def enable(self) -> SCPICmdWrite:
        """Return the :DISPlay:MENUBar:ENABle command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:ENABle")


class InfiniiumDisplayPersistCommands(BaseSCPICmd):
    """The :DISPlay:PERSist command tree."""

    @property
    def clear(self) -> SCPICmdWrite:
        """Return the :DISPlay:PERSist:CLEar command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:CLEar")

    @property
    def enable(self) -> SCPICmdWrite:
        """Return the :DISPlay:PERSist:ENABle command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:ENABle")

    @property
    def time(self) -> SCPICmdWrite:
        """Return the :DISPlay:PERSist:TIME command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:TIME")


class InfiniiumDisplaySetupCommands(BaseSCPICmd):
    """The :DISPlay:SETup command tree."""

    @property
    def background(self) -> SCPICmdWrite:
        """Return the :DISPlay:SETup:BACKground command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:BACKground")

    @property
    def clear(self) -> SCPICmdWrite:
        """Return the :DISPlay:SETup:CLEar command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:CLEar")

    @property
    def connect(self) -> SCPICmdWrite:
        """Return the :DISPlay:SETup:CONNect command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:CONNect")

    @property
    def detail(self) -> SCPICmdWrite:
        """Return the :DISPlay:SETup:DETail command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:DETail")

    @property
    def gridintensity(self) -> SCPICmdWrite:
        """Return the :DISPlay:SETup:GRIDintensity command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:GRIDintensity")

    @property
    def show(self) -> SCPICmdWrite:
        """Return the :DISPlay:SETup:SHOW command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SHOW")

    @property
    def theme(self) -> SCPICmdWrite:
        """Return the :DISPlay:SETup:THEMe command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:THEMe")

    @property
    def waveforms(self) -> SCPICmdWrite:
        """Return the :DISPlay:SETup:WAVeforms command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:WAVeforms")


class InfiniiumDisplayStyleCommands(BaseSCPICmd):
    """The :DISPlay:STYLe command tree."""

    @property
    def area(self) -> SCPICmdWrite:
        """Return the :DISPlay:STYLe:AREA command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:AREA")


class InfiniiumDisplayToolbarCommands(BaseSCPICmd):
    """The :DISPlay:TOOLbar command tree."""

    @property
    def enable(self) -> SCPICmdWrite:
        """Return the :DISPlay:TOOLbar:ENABle command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:ENABle")


class InfiniiumDisplayVectorCommands(BaseSCPICmd):
    """The :DISPlay:VECTor command tree."""

    @property
    def enable(self) -> SCPICmdWrite:
        """Return the :DISPlay:VECTor:ENABle command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:ENABle")


####################################################################################################


class InfiniiumMarkerCommands(BaseSCPICmd):
    """The :MARKer command tree."""

    def __init__(self, device: "PIControl | None" = None) -> None:
        """Initialize the Marker commands."""
        super().__init__(device, ":MARKer")
        self._x1 = InfiniiumMarkerX1Commands(device, f"{self._cmd_syntax}:X1")
        self._x1d = InfiniiumMarkerX1DCommands(device, f"{self._cmd_syntax}:X1D")
        self._x2 = InfiniiumMarkerX2Commands(device, f"{self._cmd_syntax}:X2")
        self._x2d = InfiniiumMarkerX2DCommands(device, f"{self._cmd_syntax}:X2D")
        self._xda = InfiniiumMarkerXDACommands(device, f"{self._cmd_syntax}:XDA")
        self._yd = InfiniiumMarkerYDACommands(device, f"{self._cmd_syntax}:YDA")

    @property
    def x1(self) -> "InfiniiumMarkerX1Commands":
        """Return the :MARKer:X1 commands."""
        return self._x1

    @property
    def x1d(self) -> "InfiniiumMarkerX1DCommands":
        """Return the :MARKer:X1D commands."""
        return self._x1d

    @property
    def x2(self) -> "InfiniiumMarkerX2Commands":
        """Return the :MARKer:X2 commands."""
        return self._x2

    @property
    def x2d(self) -> "InfiniiumMarkerX2DCommands":
        """Return the :MARKer:X2D commands."""
        return self._x2d

    @property
    def xda(self) -> "InfiniiumMarkerXDACommands":
        """Return the :MARKer:XDA commands."""
        return self._xda

    @property
    def yda(self) -> "InfiniiumMarkerYDACommands":
        """Return the :MARKer:YDA commands."""
        return self._yd

    # Direct commands
    @property
    def clear_all(self) -> SCPICmdWrite:
        """Return the :MARKer:CLEar:ALL command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:CLEar:ALL")

    @property
    def command_mode(self) -> SCPICmdWrite:
        """Return the :MARKer:COMMand:MODE command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:COMMand:MODE")

    @property
    def count_mode(self) -> SCPICmdWrite:
        """Return the :MARKer:COUNt:MODE command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:COUNt:MODE")

    @property
    def count_source(self) -> SCPICmdWrite:
        """Return the :MARKer:COUNt:SOURce command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:COUNt:SOURce")

    @property
    def count_total(self) -> SCPICmdRead:
        """Return the :MARKer:COUNt:TOTal? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:COUNt:TOTal")

    @property
    def count_value(self) -> SCPICmdRead:
        """Return the :MARKer:COUNt:VALue? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:COUNt:VALue")

    @property
    def domain(self) -> SCPICmdWrite:
        """Return the :MARKer:DOMain command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:DOMain")

    @property
    def function(self) -> SCPICmdWrite:
        """Return the :MARKer:FUNCtion command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:FUNCtion")

    @property
    def label(self) -> SCPICmdWrite:
        """Return the :MARKer:LABel command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:LABel")

    @property
    def mode(self) -> SCPICmdWrite:
        """Return the :MARKer:MODE command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:MODE")

    @property
    def panel_mode(self) -> SCPICmdWrite:
        """Return the :MARKer:PANel:MODE command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:PANel:MODE")

    @property
    def panel_show(self) -> SCPICmdWrite:
        """Return the :MARKer:PANel:SHOW command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:PANel:SHOW")

    @property
    def plane(self) -> SCPICmdWrite:
        """Return the :MARKer:PLANE command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:PLANE")

    @property
    def show(self) -> SCPICmdWrite:
        """Return the :MARKer:SHOW command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SHOW")

    @property
    def source(self) -> SCPICmdWrite:
        """Return the :MARKer:SOURce command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SOURce")

    @property
    def spacing(self) -> SCPICmdWrite:
        """Return the :MARKer:SPACing command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:SPACing")

    @property
    def statistics_clear(self) -> SCPICmdWrite:
        """Return the :MARKer:STATistics:CLEar command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:STATistics:CLEar")

    @property
    def tscale(self) -> SCPICmdWrite:
        """Return the :MARKer:TSCale command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:TSCale")

    @property
    def unass(self) -> SCPICmdWrite:
        """Return the :MARKer:UNASsigned command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:UNASsigned")

    @property
    def vscale(self) -> SCPICmdWrite:
        """Return the :MARKer:VSCale command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:VSCale")


class InfiniiumMarkerX1Commands(BaseSCPICmd):
    """The :MARKer:X1 command tree."""

    @property
    def position(self) -> SCPICmdWrite:
        """Return the :MARKer:X1:POSition command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:POSition")

    @property
    def yposition(self) -> SCPICmdWrite:
        """Return the :MARKer:X1:YPOSition command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:YPOSition")


class InfiniiumMarkerX1DCommands(BaseSCPICmd):
    """The :MARKer:X1D command tree."""

    @property
    def position(self) -> SCPICmdWrite:
        """Return the :MARKer:X1D:POSition command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:POSition")


class InfiniiumMarkerX2Commands(BaseSCPICmd):
    """The :MARKer:X2 command tree."""

    @property
    def position(self) -> SCPICmdWrite:
        """Return the :MARKer:X2:POSition command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:POSition")

    @property
    def yposition(self) -> SCPICmdWrite:
        """Return the :MARKer:X2:YPOSition command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:YPOSition")


class InfiniiumMarkerX2DCommands(BaseSCPICmd):
    """The :MARKer:X2D command tree."""

    @property
    def position(self) -> SCPICmdWrite:
        """Return the :MARKer:X2D:POSition command."""
        return SCPICmdWrite(self._device, f"{self._cmd_syntax}:POSition")


class InfiniiumMarkerXDACommands(BaseSCPICmd):
    """The :MARKer:XDA command tree."""

    @property
    def position(self) -> SCPICmdRead:
        """Return the :MARKer:XDA:POSition? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:POSition")


class InfiniiumMarkerYDACommands(BaseSCPICmd):
    """The :MARKer:YDA command tree."""

    @property
    def position(self) -> SCPICmdRead:
        """Return the :MARKer:YDA:POSition? query command."""
        return SCPICmdRead(self._device, f"{self._cmd_syntax}:POSition")
