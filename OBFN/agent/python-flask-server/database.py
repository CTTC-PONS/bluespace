import sys

from swagger_server.models.operation import Operation

operations = list()


def update_operation(beam_id, X_offset_angle, Y_offset_angle):
    """
    Update Operation by ID

    :param beam_id: beam id
    :type beam_id: int
    :param X_offset_angle: X Offset Angle (deg)
    :type X_offset_angle: int
    :param Y_offset_angle: Y Offset Angle (deg)
    :type Y_offset_angle: int

    :rtype: Operation
    """
    for item in operations:
        if item.beam_id == beam_id:
            item.x_offset_angle = X_offset_angle
            item.y_offset_angle = Y_offset_angle
            return item
