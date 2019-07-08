from swagger_server.models.operations import Operations

operations_list = Operations()


def create_operations(new_operations):
    """
    Create operations

    :param new_operations: list of new operations
    :type new_operations: list

    :return: list of operations
    :rtype: Operations
    """
    if len(operations_list.operations) != 0:  # if exists operations in operations_list
        for nop in new_operations:  # for each new operation
            if not any(op.beam_id == nop.beam_id for op in
                       operations_list.operations):  # if not exists beam_id in operations of operations_list
                operations_list.operations.append(nop)  # append new operations to operations_list
    else:
        operations_list.operations = new_operations  # add new operations to operations_list

# def update_operation(beam_id, X_offset_angle, Y_offset_angle):
#     """
#     Update Operation by ID

#     :param beam_id: beam id
#     :type beam_id: int
#     :param X_offset_angle: X Offset Angle (deg)
#     :type X_offset_angle: int
#     :param Y_offset_angle: Y Offset Angle (deg)
#     :type Y_offset_angle: int

#     :rtype: Operation
#     """
#     for item in operations:
#         if item.beam_id == beam_id:
#             item.x_offset_angle = X_offset_angle
#             item.y_offset_angle = Y_offset_angle
#             return item
