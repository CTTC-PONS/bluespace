obfn_pool = {}
wavelength = float()


def display_data():
    return {
        "obfn-pool": [obfn_pool[obfn] for obfn in obfn_pool],
        "wavelength": wavelength
    }


def get_data():
    return {
        "obfn-pool": obfn_pool,
        "wavelength": wavelength
    }


def create_operations(new_parameters):
    """
    Create operations

    :param new_parameters: list of new parameters to configure
    :type new_parameters: ObfnParameters

    :return: dictionary of new obfn params
    :rtype: dict
    """
    global obfn_pool, wavelength

    obfn_pool = {}
    for obfn in new_parameters.obfn_pool:
        obfn_pool[obfn.beam_id] = obfn
    wavelength = new_parameters.wavelength

    return get_data()


def delete_operations():
    """
    Delete operations
    """
    global obfn_pool, wavelength

    obfn_pool = list()
    wavelength = None

    return display_data()


def update_operation(new_obfn):
    """
    Update operation

    :param new_obfn: obfn settings
    :type new_obfn: Obfn

    :return: obfn modified
    :rtype: Obfn
    """

    global obfn_pool

    obfn_pool[new_obfn.beam_id] = new_obfn

    return get_data()
