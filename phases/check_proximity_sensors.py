try:
    from tofupilot_types import PhaseResult
except ImportError:
    class PhaseResult:
        CONTINUE = "CONTINUE"
        RETRY = "RETRY"
        SKIP = "SKIP"
        STOP = "STOP"
        FAIL = "FAIL"


def check_proximity_sensors(measurements, ethercat):
    # ========================================
    # WAIT FOR UI INPUT: Operator confirms hand is empty
    # ========================================
    # TODO: Implement operator prompt UI component

    # Read proximity light sensor data for BOTH top and bottom sensors (empty state)
    proximity_empty = ethercat.read_proximity_sensors()
    top_empty_proximity = proximity_empty["top"]
    bot_empty_proximity = proximity_empty["bot"]

    # ========================================
    # WAIT FOR UI INPUT: Operator places handle
    # ========================================
    # TODO: Implement operator prompt UI component

    # Close fingers around the handle
    ethercat.close_fingers(3.0)

    # Read proximity light sensor data for BOTH top and bottom sensors (handle + closed fingers state)
    proximity_handle = ethercat.read_proximity_sensors()
    top_handle_proximity = proximity_handle["top"]
    bot_handle_proximity = proximity_handle["bot"]

    # Open fingers again
    ethercat.open_fingers(3.0)

    # Calculate and record measurements for TOP sensor (2 measurements)
    measurements.add("top_force_delta", abs(top_empty_proximity - top_handle_proximity))
    measurements.add("top_check_order", top_handle_proximity - top_empty_proximity)

    # Calculate and record measurements for BOTTOM sensor (2 measurements)
    measurements.add("bot_force_delta", abs(bot_empty_proximity - bot_handle_proximity))
    measurements.add("bot_check_order", bot_handle_proximity - bot_empty_proximity)

    return PhaseResult.CONTINUE
