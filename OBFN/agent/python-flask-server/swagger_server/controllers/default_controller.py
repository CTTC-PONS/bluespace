import connexion
import six

from swagger_server.models.operation import Operation  # noqa: E501
from swagger_server.models.operations import Operations  # noqa: E501
from swagger_server import util


def create_configuration(body):  # noqa: E501
    """Create configuration

    Create operations of resource: beams # noqa: E501

    :param body: operations
    :type body: dict | bytes

    :rtype: Operations
    """
    if connexion.request.is_json:
        body = Operations.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


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
    return 'do some magic!'


def update_configuration_by_id(beam_id, x_offset_angle, y_offset_angle, wavelength=None):  # noqa: E501
    """Update configuration by ID

    Update operation of resource: beams # noqa: E501

    :param beam_id: beam id
    :type beam_id: int
    :param x_offset_angle: X Offset Angle (deg)
    :type x_offset_angle: 
    :param y_offset_angle: Y Offset Angle (deg)
    :type y_offset_angle: 
    :param wavelength: wavelength
    :type wavelength: 

    :rtype: Operation
    """
    return 'do some magic!'
