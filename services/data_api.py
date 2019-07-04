import requests


class AccessToProjects:
    def __init__(self):
        pass

    def get(self, id):
        response = requests.get('https://localhost:<port>/projects/{0}/calc'.format(id))
        return response.json(), response.status_code

    def put(self, id, status):
        requests.put('https://localhost:<port>/projects/{0}/calc'.format(id), json={"status":status})


class AccessToContracts:

    def __init__(self):
        pass

    def get(self, id):
        response = requests.get("http://localhost:5000/api/contracts/{0}".format(id))
        return response.json(), response.status_code
