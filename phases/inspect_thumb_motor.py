import os
import sys

try:
    from job_worker import PhaseResult
except ImportError:
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "src-tauri", "python"))
    from job_worker import PhaseResult


def inspect_thumb_motor(run, ethercat):
    ethercat.start_motor_oscillation("thumb", 0.5, 3.0)

    # Operator uses UI switch to confirm "Thumb Moves Correctly"
    # UI binds to measurements.thumb_ok and blocks until operator responds

    ethercat.stop_motor_oscillation("thumb")

    return PhaseResult.CONTINUE
