import connexion
import six

from swagger_server.models.operation import Operation  # noqa: E501
from swagger_server.models.operations import Operations  # noqa: E501
from swagger_server import util


def create_configuration_by_id(arof_id, enable=None):  # noqa: E501
    """Create configuration by ID

    Create operation of resource: laser # noqa: E501

    :param arof_id: arof id
    :type arof_id: int
    :param enable: enable or disable the laser
    :type enable: bool

    :rtype: Operation
    """
    return 'do some magic!'


def delete_configuration_by_id(arof_id):  # noqa: E501
    """Delete configuration by ID

    Delete operation of resource: laser # noqa: E501

    :param arof_id: arof id
    :type arof_id: int

    :rtype: None
    """
    return 'do some magic!'


def retrieve_configuration():  # noqa: E501
    """Retrieve configuration

    Retrieve operation of resource: laser # noqa: E501


    :rtype: Operations
    """
    return 'do some magic!'


def update_arof_by_id(arof_id, enable=None):  # noqa: E501
    """Update configuration by ID

    Update operation of resource: laser # noqa: E501

    :param arof_id: arof id
    :type arof_id: int
    :param enable: enable or disable the laser
    :type enable: bool

    :rtype: Operation
    """
    return 'do some magic!'
