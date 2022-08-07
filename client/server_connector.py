import requests


class ServerConnector:

    def __init__(self, address, port, local):
        self.url = address if local else f"{address}:{port}"
        print(f"Init ServerConnector with url: {self.url}")

    def get_unique_code(self, unique_identifier):
        # TODO add error handling
        try:
            result = requests.post(f"{self.url}",
                                   json={
                                       'unique_identifier': unique_identifier
                                   }
                                   ).json()
            return result
        except requests.ConnectionError:
            result = {
                "status": "error",
                "message": "Couldn't connect to server",
                "unique_code": ""
            }

            return result

    def send_message(self, unique_identifier, unique_code, message):
        # TODO: Add error handling
        result = requests.post(f"{self.url}",
                               json={
                                   'unique_identifier': unique_identifier,
                                   'unique_code': unique_code,
                                   'message': message
                               }
                               ).json()
        return result
