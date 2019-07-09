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
    :type operations: dict
    :return: list of new operations
    """
    request = requests.post('http://%s:5002/api/obfn' % host, headers=headers, json=operations)
    return request.json()


def put(host, id, x, y, w):
    """
    Modify operation on a beam specified by ID

    :param host: ip address from REST API agent
    :type host: str
    :param id: beam id
    :type id: int
    :param x: X Offset Angle (deg)
    :type x: float
    :param y: Y Offset Angle (deg)
    :type y: float
    :param w: wavelength
    :type w: float
    :return: operation modified
    """
    payload = {'x_offset_angle': x, 'y_offset_angle': y, 'wavelength': w}
    request = requests.put('http://%s:5002/api/obfn/%s' % (host, id), headers=headers, params=payload)
    return request.json()


def delete(host):
    """
    Remove operations on beams

    :param host: ip address from REST API agent
    :type host: str
    """
    requests.delete('http://%s:5002/api/obfn' % host, headers=headers)


if __name__ == '__main__':
    host = "10.1.7.64"
    headers = {"Content-Type": "application/json"}
    dataset = {
        "operations": [
            {
                "beam_id": 0,
                "x_offset_angle": -90,
                "y_offset_angle": 90,
                "wavelength": 1553
            },
            {
                "beam_id": 1,
                "x_offset_angle": -90,
                "y_offset_angle": 90,
                "wavelength": 1553
            },
            {
                "beam_id": 2,
                "x_offset_angle": -90,
                "y_offset_angle": 90,
                "wavelength": 1553
            },
            {
                "beam_id": 3,
                "x_offset_angle": -90,
                "y_offset_angle": 90,
                "wavelength": 1553
            }
        ]
    }

    print("POST")
    print(post(host, dataset))

    print("GET")
    print(get(host))

    print("MODIFY BEAM with beam_id = 1")
    print(put(host, 1, -80, 80, 1552))

    print("GET")
    print(get(host))

    print("DELETE")
    delete(host)

    print("GET")
    print(get(host))
