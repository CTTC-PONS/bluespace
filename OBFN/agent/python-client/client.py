import requests


def get(host, port):
    """
    Retrieve operations on the Laser

    :param host: ip address from REST API agent
    :type host: str
    :return: list of operations
    """
    request = requests.get('http://%s:%s/api/obfn' % (host, port) , headers=headers)
    return request.json()


def post(host, port, id, status, x, y, z, wavelength):
    """
    Create operation on the Laser

    :param host: ip address from REST API agent
    :type host: str
    :param id: laser id
    :type id: int
    :param status: if True laser is enable, disable otherwise
    :return: new operation
    """

    payload = { 'obfn-pool': [{ 'beam-enable' : status, 'beam-id' : id, 'width' : z, 'x-offset-angle' : x, 'y-offset-angle' : y}], "wavelength-reference-pool" : [{'wavelength-id' : id, 'central-frequency' : wavelength}]  }
    request = requests.post('http://%s:%s/api/obfn' % (host, port), headers=headers, json=payload)
    return request.json()


def put(host, port, id, status, x, y, z, wavelength):
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
    payload = { 'obfn-pool': [{ 'beam-enable' : status, 'beam-id' : id, 'width' : z, 'x-offset-angle' : x, 'y-offset-angle' : y}], "wavelength-reference-pool" : [{'wavelength-id' : id, 'central-frequency' : wavelength}]  }
    request = requests.put('http://%s:%s/api/obfn' % (host, port), headers=headers, json=payload)
    return request.json()


def delete(host, port):
    """
    Remove operations on the Laser

    :param host: ip address from REST API agent
    :type host: str
    :param id: laser id
    :type id: int
    """
    requests.delete('http://%s:%s/api/obfn' % (host, port), headers=headers)


if __name__ == '__main__':
    host = "localhost"
    port = "5002"
    headers = {"Content-Type": "application/json"}

    print("ENSURE BEAMS OFF")
    status = False
    wavelength = 1
    xOffset = 20
    yOffset = 0
    beamWidth = 10
    print(post(host, port, 0, status, xOffset, yOffset, beamWidth, wavelength))
    print(post(host, port, 1, status, xOffset, yOffset, beamWidth, wavelength))
    print(post(host, port, 2, status, xOffset, yOffset, beamWidth, wavelength))
    print(post(host, port, 3, status, xOffset, yOffset, beamWidth, wavelength))

    print("ENABLE BEAM 1")
    status = True
    beamId = 1
    wavelength  = 3
    xOffset = 30
    yOffset = 10
    beamWidth = 15
    print(put(host, port, beamId, status, xOffset, yOffset, beamWidth, wavelength))

    print("GET OPERATIONS ON BEAMS")
    print(get(host, port))

    print("DISABLE BEAMS")
    delete(host, port)

    print("GET OPERATIONS ON BEAMS")
    print(get(host, port))
