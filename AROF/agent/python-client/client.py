import requests


def get(host, port):
    """
    Retrieve operations on the Laser

    :param host: ip address from REST API agent
    :type host: str
    :return: list of operations
    """
    request = requests.get('http://%s:%s/api/arof' % (host, port) , headers=headers)
    return request.json()


def post(host, port, id, status, wavelength):
    """
    Create operation on the Laser

    :param host: ip address from REST API agent
    :type host: str
    :param id: laser id
    :type id: int
    :param status: if True laser is enable, disable otherwise
    :return: new operation
    """

    payload = { 'arof-pool': [{ 'arof-id' : id, 'enabled' : status, 'wavelength' : wavelength}]  }
    request = requests.post('http://%s:%s/api/arof' % (host, port), headers=headers, json=payload)
    return request.json()


def put(host, port, id, status, wavelength):
    """
    Modify operation on the Laser

    :param host: ip address from REST API agent
    :type host: str
    :param id: laser id
    :type id: int
    :param status: if True laser is enable, disable otherwise
    :type status: bool
    :return: operation modified
    """
    payload = { 'arof-pool': [{ 'arof-id' : id, 'enabled' : status, 'wavelength' : wavelength}]  }
    request = requests.put('http://%s:%s/api/arof' % (host, port), headers=headers, json=payload)
    return request.json()


def delete(host, port):
    """
    Remove operations on the Laser

    :param host: ip address from REST API agent
    :type host: str
    :param id: laser id
    :type id: int
    """
    requests.delete('http://%s:%s/api/arof' % (host, port), headers=headers)


if __name__ == '__main__':
    host = "localhost"
    port = "5000"
    headers = {"Content-Type": "application/json"}

    print("ENSURE LASERS OFF")
    status = False
    wavelength = 1
    print(post(host, port, 0, status, wavelength))
    print(post(host, port, 1, status, wavelength))
    print(post(host, port, 2, status, wavelength))
    print(post(host, port, 3, status, wavelength))

    print("ENABLE LASERS")
    status = True
    wavelength  = 3
    print(put(host, port, 0, status, wavelength))
    print(put(host, port, 1, status, wavelength))
    print(put(host, port, 2, status, wavelength))

    print("GET OPERATIONS ON LASERS")
    print(get(host, port))

    print("DISABLE LASERS 1 AND 2, AND ENABLE LASER 3")
    status = False
    wavelength = 5
    print(put(host, port, 1, status, wavelength))
    print(put(host, port, 2, status, wavelength))
    print(put(host, port, 3, True, 1))

    print("GET OPERATIONS ON LASERS")
    print(get(host, port))

    print("DISABLE LASERS")
    delete(host, port)

    print("GET OPERATIONS ON LASERS")
    print(get(host, port))
