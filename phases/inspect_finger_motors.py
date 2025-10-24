try:
    from tofupilot_types import PhaseResult
except ImportError:
    class PhaseResult:
        CONTINUE = "CONTINUE"
        RETRY = "RETRY"
        SKIP = "SKIP"
        STOP = "STOP"
        FAIL = "FAIL"


def inspect_finger_motors(run, ethercat):
    ethercat.start_motor_oscillation("fingers", 1.5, 6.0)

    # Operator uses UI switch to confirm "Fingers Move Correctly"
    # UI binds to measurements.fingers_ok and blocks until operator responds

    ethercat.stop_motor_oscillation("fingers")

    return PhaseResult.CONTINUE
