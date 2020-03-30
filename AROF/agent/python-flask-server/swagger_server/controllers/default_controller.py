import connexion
import six

from swagger_server.models.arof_parameters import ArofParameters  # noqa: E501
from swagger_server import util

from subprocess import call

arof_pool_db = None


def initialise():
    global arof_pool_db
    arof_pool_db = ArofParameters()
    arof_pool_db.arof_pool = []


initialise()


def create_configuration(arof_pool):  # noqa: E501
    """Create configuration

    Create arof configuration # noqa: E501

    :param arof_pool: arof pool
    :type arof_pool: dict | bytes

    :rtype: ArofParameters
    """
    global arof_pool_db
    initialise()

    if connexion.request.is_json:
        arof_pool_db = ArofParameters.from_dict(connexion.request.get_json())  # noqa: E501
        exec_config_app(arof_pool)
        return arof_pool_db

    else:
        return 'Error!'


def delete_configuration():  # noqa: E501
    """Delete configuration

    Delete all configuration # noqa: E501


    :rtype: None
    """
    global arof_pool_db
    initialise()
    
    call_arg_list = ["swagger_server/arof-conf/arof-conf", "-v", "-i", "0", "-e", "0"]
    call(call_arg_list)
    call_arg_list = ["swagger_server/arof-conf/arof-conf", "-v", "-i", "1", "-e", "0"]
    call(call_arg_list)
    call_arg_list = ["swagger_server/arof-conf/arof-conf", "-v", "-i", "2", "-e", "0"]
    call(call_arg_list)
    call_arg_list = ["swagger_server/arof-conf/arof-conf", "-v", "-i", "3", "-e", "0"]
    call(call_arg_list)

    return arof_pool_db


def retrieve_configuration():  # noqa: E501
    """Retrieve configuration

    Retrieve operation of resource: laser # noqa: E501


    :rtype: List[ArofParameters]
    """
    global arof_pool_db
    return arof_pool_db


def update_configuration(arof_pool):  # noqa: E501
    """Update configuration

    Update arof configuration # noqa: E501

    :param arof_pool: arof pool
    :type arof_pool: dict | bytes

    :rtype: ArofParameters
    """
    global arof_pool_db
    if not arof_pool_db:
        initialise()

    if connexion.request.is_json:
        new_arof_pool = ArofParameters.from_dict(connexion.request.get_json())  # noqa: E501

        if new_arof_pool.arof_pool:
            for old_arof in arof_pool_db.arof_pool:
                replaced = False
                for new_arof in new_arof_pool.arof_pool:
                    if old_arof.arof_id == new_arof.arof_id:
                        replaced = True
                        break
                if not replaced:
                    new_arof_pool.arof_pool.append(old_arof)

        arof_pool_db = new_arof_pool
        exec_config_app(arof_pool)
        return arof_pool_db

    else:
        return 'Error!'

def exec_config_app(arof_pool):
    """Execute configuration application

    Call application that is responsible to configure the actual ARoF HW   
    
    :param arof_pool: arof pool
    :type arof_pool: dict | bytes

    :param arof_id: arof id
    :type arof_id: int [0,3]
    :param enable: enable or disable the laser
    :type enable: bool
    :param wavelength: wavelength
    :type wavelength: int [1, 79]

    :rtype: ArofParameters
    """
    # print(['AROF_POOL:', arof_pool])
    for k in arof_pool.values():
        for l in range(len(k)): 
            [arof_id, enable, wavelength] = k[l].values()
            # call_arg_list = ["swagger_server/arof-conf/arof-conf", "-i", "{:d}".format(arof_id), "-e", "{:d}".format(enable), "-w", "{:d}".format(wavelength)]
            call_arg_list = ["swagger_server/arof-conf/arof-conf", "-v", "-i", "{:d}".format(arof_id), "-e", "{:d}".format(enable), "-w", "{:d}".format(wavelength)]
            # print (['CMD:', call_arg_list])
            call(call_arg_list)

    return 'bOK'
