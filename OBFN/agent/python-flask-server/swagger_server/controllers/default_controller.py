import connexion
from swagger_server.models.obfn_parameters import ObfnParameters  # noqa: E501


obfn_parameters_db = None


def initialise():
    global obfn_parameters_db
    obfn_parameters_db = ObfnParameters()
    obfn_parameters_db.obfn_pool = []
    obfn_parameters_db.wavelength_reference_pool = []


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

        for old_obfn in obfn_parameters_db.obfn_pool:
            replaced = False
            for new_obfn in new_obfn_parameters.obfn_pool:
                if old_obfn.beam_id == new_obfn.beam_id:
                    replaced = True
                    break
            if not replaced:
                new_obfn_parameters.obfn_pool.append(old_obfn)

        for old_wavelength_reference in obfn_parameters_db.wavelength_reference_pool:
            replaced = False
            for new_wavelength_reference in new_obfn_parameters.wavelength_reference_pool:
                if old_wavelength_reference.wavelength_id == new_wavelength_reference.wavelength_id:
                    replaced = True
                    break
            if not replaced:
                new_obfn_parameters.wavelength_reference_pool.append(old_wavelength_reference)

        obfn_parameters_db = new_obfn_parameters

        return obfn_parameters_db

    else:
        return 'Error!'
