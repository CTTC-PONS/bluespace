import connexion
import six

from swagger_server.models.operation import Operation  # noqa: E501
from swagger_server import util


def create_configuration(body):  # noqa: E501
    """Create configuration

    Create operations of resource: beam # noqa: E501

    :param body: configuration parameters
    :type body: list | bytes

    :rtype: List[Operation]
    """
    if connexion.request.is_json:
        body = [Operation.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def delete_configuration():  # noqa: E501
    """Delete configuration

    Delete operations of resource: beam # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def retrieve_configuration():  # noqa: E501
    """Retrieve configuration

    Retrieve operations of resource: beam # noqa: E501


    :rtype: List[Operation]
    """
    return 'do some magic!'


def update_configuration_by_id(beam_id, X_offset_angle=None, Y_offset_angle=None):  # noqa: E501
    """Update configuration by ID

    Update operation of resource: beam # noqa: E501

    :param beam_id: beam id
    :type beam_id: int
    :param X_offset_angle: X Offset Angle (deg)
    :type X_offset_angle: int
    :param Y_offset_angle: Y Offset Angle (deg)
    :type Y_offset_angle: int

    :rtype: Operation
    """
    return 'do some magic!'
