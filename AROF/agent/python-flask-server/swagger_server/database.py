from swagger_server.models.operation import Operation

operations = list()


def create_operation(arof_id, enable):
    """
    Create operation by ID

    :param arof_id: arof id
    :type arof_id: int
    :param enable: enable or disable the laser
    :type enable: bool

    :rtype: Operation
    """
    op = Operation(arof_id, enable)
    if len(operations) != 0:
        for elem in operations:
            if arof_id not in elem:
                operations.append(op)
    else:
        operations.append(op)

    return op
