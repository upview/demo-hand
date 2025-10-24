import os
import sys

try:
    from job_worker import PhaseResult
except ImportError:
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "src-tauri", "python"))
    from job_worker import PhaseResult


def inspect_finger_motors(run, ethercat):
    ethercat.start_motor_oscillation("fingers", 1.5, 6.0)

    # Operator uses UI switch to confirm "Fingers Move Correctly"
    # UI binds to measurements.fingers_ok and blocks until operator responds

    ethercat.stop_motor_oscillation("fingers")

    return PhaseResult.CONTINUE
