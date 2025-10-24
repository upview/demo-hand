try:
    from tofupilot_types import PhaseResult
except ImportError:
    class PhaseResult:
        CONTINUE = "CONTINUE"
        RETRY = "RETRY"
        SKIP = "SKIP"
        STOP = "STOP"
        FAIL = "FAIL"


def initialize_ethercat(run, ethercat):

    # 1. Prompt operator to confirm ethercat is plugged in
    # TODO: Implement operator prompt

    # 2. Prompt operator to confirm 24V-2A power supply connected
    # TODO: Implement operator prompt

    # 3. Detect ethercat interface
    interface = ethercat.find_interface(20, 1.0)
    if interface is None:
        return PhaseResult.FAIL

    # 4. Update hal_ethercat.yaml config file
    if not ethercat.update_config(interface):
        return PhaseResult.FAIL

    # 5. Count ethercat slaves
    slave_count = ethercat.count_slaves(10, 0.5)
    state = ethercat.get_state()

    if slave_count != state["expected_slaves"]:
        return PhaseResult.FAIL

    # 6. Cleanup any existing legend_hal and legend_broker processes
    ethercat.cleanup_processes()

    # 7. Launch legend_broker subprocess
    if not ethercat.launch_broker(10):
        return PhaseResult.FAIL

    # 8. Launch legend_hal subprocess
    if not ethercat.launch_hal(20):
        return PhaseResult.FAIL

    # 9. Return success
    return PhaseResult.CONTINUE
