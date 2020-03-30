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
        exec_config_app(obfn_params)
        return obfn_parameters_db

        

    else:
        return 'Error!'


def delete_configuration():  # noqa: E501
    """Delete configuration

    Delete OBFN configuration # noqa: E501


    :rtype: None
    """
    global obfn_parameters_db
    initialise()

    # Disabling arof modulators
    call_arg_list = ["swagger_server/obfn-conf/obfn-conf", "-v", "-i", "0", "-e", "0"]
    call(call_arg_list)
    call_arg_list = ["swagger_server/obfn-conf/obfn-conf", "-v", "-i", "1", "-e", "0"]
    call(call_arg_list)
    call_arg_list = ["swagger_server/obfn-conf/obfn-conf", "-v", "-i", "2", "-e", "0"]
    call(call_arg_list)
    call_arg_list = ["swagger_server/obfn-conf/obfn-conf", "-v", "-i", "3", "-e", "0"]
    call(call_arg_list)

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
        exec_config_app(obfn_params)
        return obfn_parameters_db

    else:
        return 'Error!'


def exec_config_app(obfn_params):
    """Execute configuration application

    Call application that is responsible to configure the actual OBFN HW  
    
    :param obfn_params: operations
    :type obfn_params: dict | bytes

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
    # print(['OBFN_PARAMS:', obfn_params])
    # print(['kOBFN_PARAMS:', obfn_params.keys()])
    # print(['vOBFN_PARAMS:', obfn_params.values()])
    l = 0
    for k in obfn_params['obfn-pool']:
        # print('runk', k)
        # print('runw', obfn_params['wavelength-reference-pool'][l])
        [beam_enable, beam_id, width, x_offset_angle, y_offset_angle] = k.values()
        [w_id, wavelength] = obfn_params['wavelength-reference-pool'][l].values()
        # print(beam_enable)
        # print(beam_id)
        # print(width)
        # print(x_offset_angle)
        # print(y_offset_angle)
        # print(wavelength)
        call_arg_list = ["swagger_server/obfn-conf/obfn-conf", "-v", "-w", "{:f}".format(wavelength), "-i",
            "{:d}".format(beam_id), "-e", "{:d}".format(beam_enable),
            "-x", "{:f}".format(x_offset_angle), "-y", "{:f}".format(y_offset_angle),
            "-z", "{:f}".format(width)]
        # print (['CMD:', call_arg_list])
        call(call_arg_list)
        l = l+1

    return 'bOK'
 