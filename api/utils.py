import requests

class ApiWrapper:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(headers or {})

    def get(self, endpoint, params=None):
        response = self.session.get(f"{self.base_url}/{endpoint}", params=params)
        return response

    def post(self, endpoint, data=None):
        response = self.session.post(f"{self.base_url}/{endpoint}", json=data)
        return response

    def put(self, endpoint, data=None):
        response = self.session.put(f"{self.base_url}/{endpoint}", json=data)
        return response

    def delete(self, endpoint):
        response = self.session.delete(f"{self.base_url}/{endpoint}")
        return response