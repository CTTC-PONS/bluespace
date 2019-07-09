from subprocess import call

import connexion
from swagger_server import database
from swagger_server.models.operations import Operations  # noqa: E501


def create_configuration():  # noqa: E501
    """Create configuration

    Create operations of resource: beams # noqa: E501

    :rtype: Operations
    """
    if connexion.request.is_json:
        new_operations = Operations.from_dict(connexion.request.get_json())  # noqa: E501
        operations_to_configure_HW = database.create_operations(new_operations.operations)
        if len(operations_to_configure_HW) != 0:
            for op in operations_to_configure_HW:  # for each new operation created
                exec_config_app(op.beam_id, op.x_offset_angle, op.y_offset_angle, op.wavelength)

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


def update_configuration_by_id(beam_id, x_offset_angle, y_offset_angle, wavelength=None):  # noqa: E501
    """Update configuration by ID

    Update operation of resource: beams # noqa: E501

    :param beam_id: beam id
    :type beam_id: int
    :param x_offset_angle: x offset angle for beam beam_id
    :type  x_offset_angle: float
    :param y_offset_angle: y offset angle for beam beam_id
    :type  y_offset_angle: float 
    :param wavelength: reference wavelength for calculation of beam pij, phij (j in [0,15]) parameters
    :type wavelength: float

    :rtype: Operation
    """
    return 'do some magic!'


def exec_config_app(beam_id, x_offset_angle, y_offset_angle, wavelength):
    """Execute configuration application

    Call application that is responsible to configure the actual OBFN HW  

    :param beam_id: beam id
    :type beam_id: int
    :param x_offset_angle: x offset angle for beam beam_id
    :type  x_offset_angle: float
    :param y_offset_angle: y offset angle for beam beam_id
    :type  y_offset_angle: float 
    :param wavelength: reference wavelength for calculation of beam pij, phij (j in [0,15]) parameters
    :type wavelength: float

    :rtype:
    """
    call_arg_list = ["swagger_server/obfn-conf/obfn-conf", "-v", "-w", "{:f}".format(wavelength), "-i",
                     "{:d}".format(beam_id), "-x", "{:f}".format(x_offset_angle), "-y", "{:f}".format(y_offset_angle)]
    # print (['CMD:', call_arg_list])
    return call(call_arg_list)
