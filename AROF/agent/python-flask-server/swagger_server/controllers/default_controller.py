from subprocess import call

from swagger_server import database


def create_configuration_by_id(arof_id, enable=False):  # noqa: E501
    """Create configuration by ID

    Create operation of resource: laser # noqa: E501

    :param arof_id: arof id
    :type arof_id: int
    :param enable: enable or disable the laser
    :type enable: bool

    :rtype: Operation
    """
    new_op = database.create_operation(arof_id, enable)
    exec_config_app(arof_id, enable)
    return new_op


def delete_configuration_by_id(arof_id):  # noqa: E501
    """Delete configuration by ID

    Delete operation of resource: laser # noqa: E501

    :param arof_id: arof id
    :type arof_id: int

    :rtype: Operation
    """
    op = database.delete_operation(arof_id)
    exec_config_app(arof_id, False)
    return op


def retrieve_configuration():  # noqa: E501
    """Retrieve configuration

    Retrieve operations of resource: laser # noqa: E501

    :rtype: List[Operation]
    """
    return database.operations


def update_configuration_by_id(arof_id, enable=False):  # noqa: E501
    """Update configuration by ID

    Update operation of resource: laser # noqa: E501

    :param arof_id: arof id
    :type arof_id: int
    :param enable: enable or disable the laser
    :type enable: bool

    :rtype: Operation
    """
    op = database.update_operation(arof_id, enable)
    exec_config_app(arof_id, enable)
    return op


def exec_config_app(arof_id, enable):
    """Execute configuration application

    Call application that is responsible to configure the actual ARoF HW   

    :param arof_id: arof id
    :type arof_id: int
    :param enable: enable or disable the laser
    :type enable: bool

    :rtype:
    """
    # call_arg_list = ["swagger_server/arof-conf/arof-conf", "-i", "{:d}".format(arof_id), "-e", "{:d}".format(enable)]
    call_arg_list = ["swagger_server/arof-conf/arof-conf", "-v", "-i", "{:d}".format(arof_id), "-e", "{:d}".format(enable)]
    # print (['CMD:', call_arg_list])
    return call(call_arg_list)
