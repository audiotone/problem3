import requests


class ServerConnector:

    def __init__(self, address, port, local):
        self.url = address if local else f"{address}:{port}"
        print(f"Init ServerConnector with url: {self.url}")


    def get_unique_code(self, unique_identifier):
        # TODO add error handling
        result = requests.post(f"{self.url}",
                               json={
                                   'unique_identifier': unique_identifier
                               }
                               ).json()
        return result['unique_code'] if result['status'] == "200" else result['message']

    def send_message(self, unique_identifier, unique_code, message):
        # TODO: Add error handling
        result = requests.post(f"{self.url}",
                               json = {
                                   'unique_identifier': unique_identifier,
                                   'unique_code': unique_code,
                                   'message': message
                               }
                               ).json()
        return result['status']


