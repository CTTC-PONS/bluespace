from swagger_server.models.operation import Operation
from agent-bvt.lib.

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
    if op not in operations:
        # TODO laser enable
        operations.append(op)
    return op


def update_operation(arof_id, enable):
    """
    Update Operation by ID

    :param arof_id: arof id
    :type arof_id: int
    :param enable: enable or disable the laser
    :type enable: bool

    :rtype: Operation
    """
    for item in operations:
        if item.arof_id == arof_id:
            item.arof_id = arof_id
            item.enable = enable
            # TODO laser enable
            return item


def delete_operation(arof_id):
    """
    Delete operation by ID

    :param arof_id: arof id
    :type arof_id: int

    :rtype: None
    """
    for item in operations:
        if item.arof_id == arof_id:
            # TODO disable laser
            operations.remove(item)