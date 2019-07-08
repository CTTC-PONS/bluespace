import connexion
import six

from swagger_server.models.operations import Operations  # noqa: E501
from swagger_server import util
from swagger_server import database


def create_configuration(new_operations=None):  # noqa: E501
    """Create configuration

    Create operations of resource: beams # noqa: E501

    :param new_operations: list of operations
    :type new_operations: list

    :rtype: Operations
    """
    if connexion.request.is_json:
        new_operations = Operations.from_dict(connexion.request.get_json())  # noqa: E501
        database.create_operations(new_operations.operations)

    return database.operations_list


def delete_configuration():  # noqa: E501
    """Delete configuration

    Delete operations of resource: beams # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def retrieve_configuration():  # noqa: E501
    """Retrieve configuration

    Retrieve operations of resource: beams # noqa: E501


    :rtype: Operations
    """
    return database.operations_list


def update_configuration_by_id(beam_id, X_offset_angle=None, Y_offset_angle=None):  # noqa: E501
    """Update configuration by ID

    Update operation of resource: beams # noqa: E501

    :param beam_id: beam id
    :type beam_id: int
    :param X_offset_angle: X Offset Angle (deg)
    :type X_offset_angle: int
    :param Y_offset_angle: Y Offset Angle (deg)
    :type Y_offset_angle: int

    :rtype: Operations
    """
    return 'do some magic!'
