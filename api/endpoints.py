class Endpoint:
    def __init__(self, api, base_url):
        self.api = api
        self.base_url = base_url


class People(Endpoint):
    def get(self, people_id):
        return self.api.get(f"{self.base_url}/people/{people_id}")