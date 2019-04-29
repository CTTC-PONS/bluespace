import requests


def get(host):
    """
    Retrieve operations on beams

    :param host: ip address from REST API agent
    :type host: str
    :return: list of operations
    """
    request = requests.get('http://%s:5002/api/obfn' % host, headers=headers)
    return request.json()


def post(host, operations):
    """
    Create operations on beams

    :param host: ip address from REST API agent
    :type host: str
    :param operations: operations to be configured on the beams
    :type operations: list
    :return: list of operations
    """
    request = requests.post('http://%s:5002/api/arof' % host, headers=headers, params=operations)
    return request.json()


def put(host, id, x, y):
    """
    Modify operation on beam specified by ID

    :param host: ip address from REST API agent
    :type host: str
    :param beam_id: beam id
    :type beam_id: int
    :param x: X Offset Angle (deg)
    :type x: int
    :param y: Y Offset Angle (deg)
    :type y: int
    :return: operation modified
    """
    payload = {'x_offset_angle': x, 'y_offset_angle': y}
    request = requests.put('http://%s:5002/api/arof/%s' % (host, id), headers=headers, params=payload)
    return request.json()


def delete(host):
    """
    Remove operations on beams

    :param host: ip address from REST API agent
    :type host: str
    """
    request = requests.delete('http://%s:5002/api/obfn/%s' % host, headers=headers)
    # return request


if __name__ == '__main__':
    host = "10.1.7.64"
    headers = {"Content-Type": "application/json"}
    operations = [
        {
            "X_offset_angle": -90,
            "Y_offset_angle": 90,
            "beam_id": 1
        },
        {
            "X_offset_angle": -90,
            "Y_offset_angle": 90,
            "beam_id": 2
        },
        {
            "X_offset_angle": -90,
            "Y_offset_angle": 90,
            "beam_id": 3
        },
        {
            "X_offset_angle": -90,
            "Y_offset_angle": 90,
            "beam_id": 4
        }
    ]

    print("POST")
    print(post(host, operations))

    print("GET")
    print(get(host))

    print("MODIFY BEAM with beam_id = 1")
    print(put(host, 1, -80, 80))

    print("GET")
    print(get(host))

    print("DELETE")
    delete(host)
    print(get(host))
