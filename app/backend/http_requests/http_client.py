import requests

class HttpClient:
    BASE_URL = "https://reqres.in/api"

    def get_users(self, page=2):
        response = requests.get(f"{self.BASE_URL}/users", params={"page": page})
        response.raise_for_status()
        return response.json()

    def get_single_user(self, user_id):
        response = requests.get(f"{self.BASE_URL}/users/{user_id}")
        return response.json() if response.status_code == 200 else None

    def get_list_resource(self):
        response = requests.get(f"{self.BASE_URL}/unknown")
        response.raise_for_status()
        return response.json()

    def get_single_resource(self, resource_id):
        response = requests.get(f"{self.BASE_URL}/unknown/{resource_id}")
        return response.json() if response.status_code == 200 else None

    def create_user(self, name, job):
        response = requests.post(f"{self.BASE_URL}/users", json={"name": name, "job": job})
        response.raise_for_status()
        return response.json()

    def update_user(self, user_id, name, job):
        response = requests.put(f"{self.BASE_URL}/users/{user_id}", json={"name": name, "job": job})
        response.raise_for_status()
        return response.json()

    def delete_user(self, user_id):
        response = requests.delete(f"{self.BASE_URL}/users/{user_id}")
        return response.status_code == 204

    def register_successful(self, email, password):
        response = requests.post(f"{self.BASE_URL}/register", json={"email": email, "password": password})
        return response.json() if response.status_code == 200 else None

    def register_unsuccessful(self, email):
        response = requests.post(f"{self.BASE_URL}/register", json={"email": email})
        return response.json() if response.status_code == 400 else None

    def login_successful(self, email, password):
        response = requests.post(f"{self.BASE_URL}/login", json={"email": email, "password": password})
        return response.json() if response.status_code == 200 else None

    def delayed_response(self, delay):
        response = requests.get(f"{self.BASE_URL}/users", params={"delay": delay})
        response.raise_for_status()
        return response.json()
