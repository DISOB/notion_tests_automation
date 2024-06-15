from client.common.base_class import RequestSender


class Users(RequestSender):
    RESOURCE = "/v1/users"

    def __init__(self, host):
        RequestSender.__init__(self)
        self.endpoint = f"{host}{self.RESOURCE}"

    def get_all_users(self, notion_api_token):
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
}
        response = self.send_request("GET", url=self.endpoint, headers=headers)
        return response
