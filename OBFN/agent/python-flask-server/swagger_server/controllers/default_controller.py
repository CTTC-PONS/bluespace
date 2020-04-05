import connexion
from swagger_server.models.obfn_parameters import ObfnParameters  # noqa: E501

from subprocess import call

obfn_parameters_db = None


def initialise():
    global obfn_parameters_db
    obfn_parameters_db = ObfnParameters()
    obfn_parameters_db.obfn_pool = []
    obfn_parameters_db.wavelength_reference_pool = []


initialise()


def create_configuration(obfn_params):  # noqa: E501
    """Create configuration

    Create OBFN configuration # noqa: E501

    :param obfn_params: operations
    :type obfn_params: dict | bytes

    :rtype: ObfnParameters
    """
    global obfn_parameters_db

    if connexion.request.is_json:
        obfn_parameters_db = ObfnParameters.from_dict(connexion.request.get_json())  # noqa: E501
        exec_config_app(obfn_parameters_db)
        return obfn_parameters_db

    else:
        return 'Error!'


def delete_configuration():  # noqa: E501
    """Delete configuration

    Delete OBFN configuration # noqa: E501


    :rtype: None
    """
    global obfn_parameters_db

    # Disabling obfn modulators
    for obfn in obfn_parameters_db.obfn_pool:
        obfn.beam_enable = False

    exec_config_app(obfn_parameters_db)

    return obfn_parameters_db


def retrieve_configuration():  # noqa: E501
    """Retrieve configuration

    Retrieve OBFN configuration # noqa: E501


    :rtype: ObfnParameters
    """
    global obfn_parameters_db
    return obfn_parameters_db


def update_configuration(obfn_params):  # noqa: E501
    """Update configuration

    Update OBFN configuration # noqa: E501

    :param obfn_params: operations
    :type obfn_params: dict | bytes

    :rtype: ObfnParameters
    """
    global obfn_parameters_db
    if not obfn_parameters_db:
        initialise()

    if connexion.request.is_json:
        new_obfn_parameters = ObfnParameters.from_dict(connexion.request.get_json())  # noqa: E501
        ids_to_configure = [obfn.beam_id for obfn in new_obfn_parameters.obfn_pool]

        # Build new db
        if new_obfn_parameters.obfn_pool:
            for old_obfn in obfn_parameters_db.obfn_pool:
                replaced = False
                for new_obfn in new_obfn_parameters.obfn_pool:
                    if old_obfn.beam_id == new_obfn.beam_id:
                        replaced = True
                        break
                if not replaced:
                    new_obfn_parameters.obfn_pool.append(old_obfn)
        else:
            new_obfn_parameters.obfn_pool = obfn_parameters_db.obfn_pool
        if new_obfn_parameters.wavelength_reference_pool:
            for old_wavelength_reference in obfn_parameters_db.wavelength_reference_pool:
                replaced = False
                for new_wavelength_reference in new_obfn_parameters.wavelength_reference_pool:
                    if old_wavelength_reference.wavelength_id == new_wavelength_reference.wavelength_id:
                        replaced = True
                        break
                if not replaced:
                    new_obfn_parameters.wavelength_reference_pool.append(old_wavelength_reference)
        else:
            new_obfn_parameters.wavelength_reference_pool = obfn_parameters_db.wavelength_reference_pool

        obfn_parameters_db = new_obfn_parameters

        # Merge changes with the whole information
        parameters_to_configure = ObfnParameters()
        parameters_to_configure.obfn_pool, parameters_to_configure.wavelength_reference_pool = [], []
        for idd in ids_to_configure:
            for obfn in obfn_parameters_db.obfn_pool:
                if obfn.beam_id == idd:
                    parameters_to_configure.obfn_pool.append(obfn)
            for wavelength in obfn_parameters_db.wavelength_reference_pool:
                if wavelength.wavelength_id == idd:
                    parameters_to_configure.wavelength_reference_pool.append(wavelength)
        exec_config_app(parameters_to_configure)

        return obfn_parameters_db

    else:
        return 'Error!'


def exec_config_app(obfn_params):
    """Execute configuration application

    Call application that is responsible to configure the actual OBFN HW  
    
    :param obfn_params: operations
    :type obfn_params: ObfnParemeters

    :param beam_id: beam id
    :type beam_id: int
    :param beam_enable: beam_enable
    :type beam_enable: bool
    :param x_offset_angle: x offset angle for beam beam_id
    :type  x_offset_angle: float
    :param y_offset_angle: y offset angle for beam beam_id
    :type  y_offset_angle: float 
    :param beam_width: beam_width for beam beam_id
    :type  beam_width: float 
    :param wavelength: reference wavelength (ITU channel) for calculation of beam pij, phij (j in [0,15]) parameters.
    :type wavelength: int

    :rtype: ObfnParameters
    """
    print('exec_config_app')
    for obfn in obfn_params.obfn_pool:
        print(obfn)
        for wavelength_reference in obfn_params.wavelength_reference_pool:
            if wavelength_reference.wavelength_id == obfn.beam_id:
                wavelength = wavelength_reference.central_frequency
        call_arg_list = ["swagger_server/obfn-conf/obfn-conf", "-v", "-w", "{:f}".format(wavelength), "-i",
            "{:d}".format(obfn.beam_id), "-e", "{:d}".format(obfn.beam_enable),
            "-x", "{:f}".format(obfn.x_offset_angle), "-y", "{:f}".format(obfn.y_offset_angle),
            "-z", "{:f}".format(obfn.width)]

        print (['CMD:', call_arg_list])
        call(call_arg_list)
    return 'bOK'
 