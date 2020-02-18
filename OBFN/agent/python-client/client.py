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


def put(host, dataset_put):
    request = requests.put('http://%s:5002/api/obfn' % (host), headers=headers, json=dataset_put)
    return request.json()


def delete(host):
    """
    Remove operations on beams

    :param host: ip address from REST API agent
    :type host: str
    """
    requests.delete('http://%s:5002/api/obfn' % host, headers=headers)


if __name__ == '__main__':
    host = "10.1.7.84"
    headers = {"Content-Type": "application/json"}
    dataset = {
        "obfn-pool": [
            {
                "beam_id": 0,
                "beam_enable": True,
                "x_offset_angle": -90,
                "y_offset_angle": 90,
                "width": 150
            },
            {
                "beam_id": 1,
                "beam_enable": True,
                "x_offset_angle": -90,
                "y_offset_angle": 90,
                "width": 155
            },
            {
                "beam_id": 2,
                "beam_enable": True,
                "x_offset_angle": -90,
                "y_offset_angle": 90,
                "width": 160
            },
            {
                "beam_id": 3,
                "beam_enable": True,
                "x_offset_angle": -90,
                "y_offset_angle": 90,
                "width": 165
            }
        ],
        "wavelength": 150
    }

    dataset_put = {
        "beam_id": 2,
        "beam_enable": False,
        "x_offset_angle": -90,
        "y_offset_angle": 90,
        "width": 150
    }

    print("POST")
    print(post(host, dataset))

    print("GET")
    print(get(host))

    print("MODIFY BEAM with beam_id = 1")
    print(put(host, dataset_put))

    print("GET")
    print(get(host))

    print("DELETE")
    delete(host)

    print("GET")
    print(get(host))
