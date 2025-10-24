try:
    from tofupilot_types import PhaseResult
except ImportError:
    class PhaseResult:
        CONTINUE = "CONTINUE"
        RETRY = "RETRY"
        SKIP = "SKIP"
        STOP = "STOP"
        FAIL = "FAIL"


def inspect_thumb_motor(run, ethercat):
    ethercat.start_motor_oscillation("thumb", 0.5, 3.0)

    # Operator uses UI switch to confirm "Thumb Moves Correctly"
    # UI binds to measurements.thumb_ok and blocks until operator responds

    ethercat.stop_motor_oscillation("thumb")

    return PhaseResult.CONTINUE
