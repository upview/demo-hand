try:
    from tofupilot_types import PhaseResult
except ImportError:
    class PhaseResult:
        CONTINUE = "CONTINUE"
        RETRY = "RETRY"
        SKIP = "SKIP"
        STOP = "STOP"
        FAIL = "FAIL"


def check_hall_sensors(measurements, ethercat):
    # ========================================
    # WAIT FOR UI INPUT: Operator confirms hand is empty
    # ========================================
    # TODO: Implement operator prompt UI component

    # Read Hall 3D sensor data for BOTH top and bottom sensors (empty state)
    hall_empty = ethercat.read_hall_sensors()
    top_empty_hall = hall_empty["top"]
    bot_empty_hall = hall_empty["bot"]

    # ========================================
    # WAIT FOR UI INPUT: Operator places handle
    # ========================================
    # TODO: Implement operator prompt UI component

    # Read Hall 3D sensor data for BOTH top and bottom sensors (handle in hand state)
    hall_handle = ethercat.read_hall_sensors()
    top_handle_hall = hall_handle["top"]
    bot_handle_hall = hall_handle["bot"]

    # Calculate and record measurements for TOP sensor (6 measurements)
    measurements.add("top_magnetic_field_delta_x", abs(top_empty_hall[0] - top_handle_hall[0]))
    measurements.add("top_magnetic_field_delta_y", abs(top_empty_hall[1] - top_handle_hall[1]))
    measurements.add("top_magnetic_field_delta_z", abs(top_empty_hall[2] - top_handle_hall[2]))
    measurements.add("top_check_order_x", top_handle_hall[0] - top_empty_hall[0])
    measurements.add("top_check_order_y", top_handle_hall[1] - top_empty_hall[1])
    measurements.add("top_check_order_z", top_handle_hall[2] - top_empty_hall[2])

    # Calculate and record measurements for BOTTOM sensor (6 measurements)
    measurements.add("bot_magnetic_field_delta_x", abs(bot_empty_hall[0] - bot_handle_hall[0]))
    measurements.add("bot_magnetic_field_delta_y", abs(bot_empty_hall[1] - bot_handle_hall[1]))
    measurements.add("bot_magnetic_field_delta_z", abs(bot_empty_hall[2] - bot_handle_hall[2]))
    measurements.add("bot_check_order_x", bot_handle_hall[0] - bot_empty_hall[0])
    measurements.add("bot_check_order_y", bot_handle_hall[1] - bot_empty_hall[1])
    measurements.add("bot_check_order_z", bot_handle_hall[2] - bot_empty_hall[2])

    return PhaseResult.CONTINUE
