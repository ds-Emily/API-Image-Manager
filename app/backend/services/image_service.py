from http_requests import HttpClient

class Image_Service:
    def __init__(self):
        self.http_requests = HttpClient()

    def get_user_avatars(self, page=2):
        users_data = self.http_requests.get_users(page)
        avatars = [user['avatar'] for user in users_data['data']]
        return avatars

    def get_single_user_data(self, user_id):
        return self.http_requests.get_single_user(user_id)

    def get_all_resources(self):
        return self.http_requests.get_list_resource()

    def get_single_resource_data(self, resource_id):
        return self.http_requests.get_single_resource(resource_id)

    def create_user(self, name, job):
        return self.http_requests.create_user(name, job)

    def update_user(self, user_id, name, job):
        return self.http_requests.update_user(user_id, name, job)

    def delete_user(self, user_id):
        return self.http_requests.delete_user(user_id)

    def register_user_successful(self, email, password):
        return self.http_requests.register_successful(email, password)

    def register_user_unsuccessful(self, email):
        return self.http_requests.register_unsuccessful(email)

    def login_user_successful(self, email, password):
        return self.http_requests.login_successful(email, password)

    def get_delayed_response(self, delay):
        return self.http_requests.delayed_response(delay)
