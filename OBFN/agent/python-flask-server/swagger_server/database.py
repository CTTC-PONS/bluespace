from swagger_server.models.operations import Operations

operations_list = Operations()


def create_operations(new_operations):
    """
    Create operations

    :param new_operations: list of new operations to configure
    :type new_operations: list

    :return: list of operations saved to configure
    :rtype: list
    """
    actual_operations = list()
    if len(operations_list.operations) != 0: 
        for nop in new_operations:  # for each new operation 
            if not any(op.beam_id == nop.beam_id for op in
                       operations_list.operations):  # if not exists new beam_id 
                operations_list.operations.append(nop)  # append new operation
                actual_operations.append(nop)
    else:
        operations_list.operations = new_operations  # add new operations to operations_list
        actual_operations = new_operations

    return actual_operations


def delete_operations():
    """
    Delete operations
    """
    if len(operations_list.operations) != 0: 
        operations_list.operations = []


def update_operation(beam_id, x_offset_angle, y_offset_angle, wavelength):
    """
    Update operation

    :param beam_id: beam id
    :type beam_id: int
    :param x_offset_angle: x offset angle for beam beam_id
    :type  x_offset_angle: float
    :param y_offset_angle: y offset angle for beam beam_id
    :type  y_offset_angle: float 
    :param wavelength: reference wavelength for calculation of beam pij, phij (j in [0,15]) parameters
    :type wavelength: float

    :return: operation modified
    :rtype: Operation
    """  
    if len(operations_list.operations) != 0:   
        index = next((index for (index, op) in enumerate(operations_list.operations) if op.beam_id == beam_id), None)
        # returns de index position if beam id exist in list of operations. None, otherwise
        if index is not None:  # if exists beam id
            operations_list.operations[index].beam_id = beam_id
            operations_list.operations[index].x_offset_angle = x_offset_angle
            operations_list.operations[index].y_offset_angle = y_offset_angle
            operations_list.operations[index].wavelength = wavelength
            return operations_list.operations[index]