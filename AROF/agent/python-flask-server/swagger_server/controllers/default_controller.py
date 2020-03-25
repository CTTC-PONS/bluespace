import connexion
import six

from swagger_server.models.arof_parameters import ArofParameters  # noqa: E501
from swagger_server import util

arof_pool_db = None


def initialise():
    global arof_pool_db
    arof_pool_db = ArofParameters()
    arof_pool_db.arof_pool = []


def create_configuration(arof_pool):  # noqa: E501
    """Create configuration

    Create arof configuration # noqa: E501

    :param arof_pool: arof pool
    :type arof_pool: dict | bytes

    :rtype: ArofParameters
    """
    global arof_pool_db

    if connexion.request.is_json:
        arof_pool_db = ArofParameters.from_dict(connexion.request.get_json())  # noqa: E501
        return arof_pool_db

    else:
        return 'Error!'


def delete_configuration():  # noqa: E501
    """Delete configuration

    Delete all configuration # noqa: E501


    :rtype: None
    """
    global arof_pool_db
    arof_pool_db = ArofParameters()
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

        for old_arof in arof_pool_db.arof_pool:
            replaced = False
            for new_arof in new_arof_pool.arof_pool:
                if old_arof.arof_id == new_arof.arof_id:
                    replaced = True
                    break
            if not replaced:
                new_arof_pool.arof_pool.append(old_arof)

        arof_pool_db = new_arof_pool

        return arof_pool_db

    else:
        return 'Error!'
