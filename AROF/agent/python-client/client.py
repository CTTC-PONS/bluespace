import requests


def get(host):
    """
    Retrieve operations on the Laser

    :param host: ip address from REST API agent
    :type host: str
    :return: list of operations
    """
    request = requests.get('http://%s:5001/api/arof' % host, headers=headers)
    return request.json()


def post(host, id, status):
    """
    Create operation on the Laser

    :param host: ip address from REST API agent
    :type host: str
    :param id: laser id
    :type id: int
    :param status: if True laser is enable, disable otherwise
    :return: new operation
    """
    payload = {'enable': status}
    request = requests.post('http://%s:5001/api/arof/%s' % (host, id), headers=headers, params=payload)
    return request.json()


def put(host, id, status):
    """
    Modify operation on the Laser

    :param host: ip address from REST API agent
    :type host: str
    :param id: laser id
    :type id: int
    :param status: if True laser is enable, disable otherwise
    :return: operation modified
    """
    payload = {'enable': status}
    request = requests.put('http://%s:5001/api/arof/%s' % (host, id), headers=headers, params=payload)
    return request.json()


def delete(host, id):
    """
    Remove operations on the Laser

    :param host: ip address from REST API agent
    :type host: str
    :param id: laser id
    :type id: int
    """
    request = requests.delete('http://%s:5001/api/arof/%s' % (host, id), headers=headers)
    # return request


if __name__ == '__main__':
    host = "10.1.7.65"
    headers = {"Content-Type": "application/json"}

    print("ENSURE LASERS OFF")
    status = False
    print(post(host, 1, status))
    print(post(host, 2, status))
    print(post(host, 3, status))
    print(post(host, 4, status))

    print("ENABLE LASERS")
    status = True
    print(put(host, 1, status))
    print(put(host, 2, status))
    print(put(host, 3, status))
    print(put(host, 4, status))

    print("GET OPERATIONS ON LASERS")
    print(get(host))

    print("DISABLE LASERS 1 AND 2")
    status = False
    print(put(host, 1, status))
    print(put(host, 2, status))

    print("GET OPERATIONS ON LASERS")
    print(get(host))

    print("DISABLE LASERS")
    delete(host, 1)
    delete(host, 2)
    delete(host, 3)
    delete(host, 4)
    print(get(host))
