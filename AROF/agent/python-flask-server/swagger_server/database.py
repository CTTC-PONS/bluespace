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
    if len(operations) != 0:
        index = next((index for (index, op) in enumerate(operations) if op.arof_id == arof_id), None)
        if index is None:
            return add_operation(arof_id, enable)
    else:
        return add_operation(arof_id, enable)


def add_operation(arof_id, enable):
    """
    Create and add operation

    :param arof_id: arof id
    :type arof_id: int
    :param enable: enable or disable the laser
    :type enable: bool

    :rtype: Operation
    """
    op = Operation(arof_id, enable)
    operations.append(op)
    return op    


def update_operation(arof_id, enable):
    """
    Update operation by ID

    :param arof_id: arof id
    :type arof_id: int
    :param enable: enable or disable the laser
    :type enable: bool

    :rtype: Operation
    """
    if len(operations) != 0:
        for item in operations:
            if item.arof_id == arof_id:
                item.arof_id = arof_id
                item.enable = enable
                return item


def delete_operation(arof_id):
    """
    Delete operation by ID

    :param arof_id: arof id
    :type arof_id: int
    """
    if len(operations) != 0:
        for item in operations:
            if item.arof_id == arof_id:
                operations.remove(item)
