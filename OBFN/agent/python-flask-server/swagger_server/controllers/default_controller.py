from subprocess import call

import connexion
from swagger_server import database
from swagger_server.models.obfn_parameters import ObfnParameters  # noqa: E501


def create_configuration():  # noqa: E501
    """Create configuration

    Create operations of resource: beams # noqa: E501

    :rtype: ObfnParameters
    """
    if connexion.request.is_json:
        obfn_parameteres = ObfnParameters.from_dict(connexion.request.get_json())  # noqa: E501
        operations_to_configure_HW = database.create_operations(obfn_parameteres)
        if len(operations_to_configure_HW['obfn-pool']) != 0:
            for op in operations_to_configure_HW['obfn-pool'].values():
                exec_config_app(op.beam_id, op.beam_enable, op.x_offset_angle, op.y_offset_angle, op.width,
                                operations_to_configure_HW['wavelength'])

    e = database.display_data()
    print(e)
    return e


def delete_configuration():  # noqa: E501
    """Delete configuration

    Delete operations of resource: beams # noqa: E501


    :rtype: None
    """
    database.delete_operations()
    e = database.display_data()
    print(e)
    return e


def retrieve_configuration():  # noqa: E501
    """Retrieve configuration

    Retrieve operations of resource: beams # noqa: E501


    :rtype: ObfnParameters
    """
    e = database.display_data()
    print(e)
    return e


def update_configuration():  # noqa: E501
    """Update configuration

    Update operation of resource: beams # noqa: E501

    :param new_obfn:
    :type new_obfn: Obfn

    :rtype: Obfn
    """
    # global wavelength
    #
    # if not connexion.request.is_json:
    #     return
    #
    # new_obfn = Obfn.from_dict(connexion.request.get_json())  # noqa: E501
    #
    # database.update_operation(new_obfn)
    # exec_config_app(new_obfn.beam_id, new_obfn.beam_enable, new_obfn.x_offset_angle, new_obfn.y_offset_angle,
    #                 new_obfn.width)
    #
    # e = database.display_data()
    # print(e)
    # return e

    return create_configuration()


def exec_config_app(beam_id, beam_enable, x_offset_angle, y_offset_angle, width, wavelength=None):
    """Execute configuration application

    Call application that is responsible to configure the actual OBFN HW  

    :param beam_id: beam id
    :type beam_id: int
    :param beam_enable: enable/disable beam
    :type beam_enable: bool
    :param x_offset_angle: x offset angle for beam beam_id
    :type  x_offset_angle: float
    :param y_offset_angle: y offset angle for beam beam_id
    :type  y_offset_angle: float
    :param width:
    :type  width: float
    :param wavelength: reference wavelength for calculation of beam pij, phij (j in [0,15]) parameters
    :type wavelength: float

    :rtype:
    """
    if wavelength:
        call_arg_list = ["swagger_server/obfn-conf/obfn-conf",
                         "-v",
                         "-i", "{:d}".format(beam_id),
                         "-e", "{}".format(beam_enable),
                         "-x", "{:f}".format(x_offset_angle),
                         "-y", "{:f}".format(y_offset_angle),
                         "-d", "{:f}".format(width),
                         "-w", "{:f}".format(wavelength)
                         ]
    else:
        call_arg_list = ["swagger_server/obfn-conf/obfn-conf",
                         "-v",
                         "-i", "{:d}".format(beam_id),
                         "-e", "{}".format(beam_enable),
                         "-x", "{:f}".format(x_offset_angle),
                         "-y", "{:f}".format(y_offset_angle),
                         "-d", "{:f}".format(width)
                         ]

    return call(call_arg_list)
