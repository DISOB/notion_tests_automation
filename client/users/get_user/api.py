from client.common.base_class import RequestSender

class Users(RequestSender):
    RESOURCE = "/v1/users"

    def __init__(self, host):
        RequestSender.__init__(self)
        self.host = host

    def get_user(self, notion_api_token, user_id):
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        endpoint = f"{self.host}{self.RESOURCE}/{user_id}"
        response = self.send_request("GET", url=endpoint, headers=headers)
        return response
