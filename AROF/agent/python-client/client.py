import requests

host_1 = "10.1.7.65"
host_2 = "10.1.7.67"
headers = {"Content-Type": "application/json"}


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
    :return:
    """
    request = requests.delete('http://%s:5001/api/arof/%s' % (host, id), headers=headers)
    return request


if __name__ == '__main__':
    print("ENSURE LASERS OFF")
    status = False
    print(post(host_1, 1, status))
    print(post(host_1, 2, status))
    print(post(host_2, 3, status))
    print(post(host_2, 4, status))
    print("ENABLE LASERS AROF AGENT 1 ON")
    status = True
    print(put(host_1, 1, status))
    print(put(host_1, 2, status))
    print("ENABLE LASERS AROF AGENT 2 ON")
    print(put(host_2, 3, status))
    print(put(host_2, 4, status))
    print("GET OPERATIONS ON AROF AGENT 1")
    print(get(host_1))
    print("GET OPERATIONS ON AROF AGENT 2")
    print(get(host_2))
    print("DISABLE LASERS AROF AGENT 1")
    status = False
    print(put(host_1, 1, status))
    print(put(host_1, 2, status))
    print("DISABLE LASERS AROF AGENT 2")
    print(put(host_2, 3, status))
    print(put(host_2, 4, status))
    print("GET OPERATIONS ON AROF AGENT 1")
    print(get(host_1))
    print("GET OPERATIONS ON AROF AGENT 2")
    print(get(host_2))
    print("DELETE OPERATIONS ON AROF AGENT 1")
    print(delete(host_1, 1))
    print(delete(host_1, 2))
    print("DELETE OPERATIONS ON AROF AGENT 2")
    print(delete(host_2, 2))
    print(delete(host_2, 3))