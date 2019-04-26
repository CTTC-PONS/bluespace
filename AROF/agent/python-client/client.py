import requests

host_1 = "10.1.7.65"
host_2 = "10.1.7.67"
headers = {"Content-Type": "application/json"}


def get(host):
    """
    Retrieve operations on the Laser

    :param host: ip address from REST API agent
    :return:
    """
    request = requests.get('http://%s:5001/api/arof' % host, headers=headers)
    return request.json()


def post(host, id):
    payload = {'enable': True}
    request = requests.post('http://%s:5001/api/arof/%s' % (host, id), headers=headers, params=payload)
    return request.json()


def put(host, id):
    payload = {'enable': False}
    request = requests.put('http://%s:5001/api/arof/%s' % (host, id), headers=headers, params=payload)
    return request.json()


def delete(host, id):
    request = requests.delete('http://%s:5001/api/arof/%s' % (host, id), headers=headers)
    return request


if __name__ == '__main__':
    print("POST")
    print(post(host_1, 2))
    print(post(host_2, 2))
    print("GET")
    print(get(host_1))
    print(get(host_2))
    print("PUT")
    print(put(host_1, 2))
    print(put(host_2, 2))
    print("GET")
    print(get(host_1))
    print(get(host_2))
    print("DELETE")
    print(delete(host_1, 2))
    print(delete(host_2, 2))