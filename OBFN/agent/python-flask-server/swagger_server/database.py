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