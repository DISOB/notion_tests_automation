from client.common.base_class import RequestSender


class Databases(RequestSender):
    RESOURCE = "/v1/databases"

    def __init__(self, host, database_id):
        RequestSender.__init__(self)
        self.endpoint = f"{host}{self.RESOURCE}/{database_id}"
        self.database_id = database_id

    def get_database(self, notion_api_token):
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        response = self.send_request("GET", url=self.endpoint, headers=headers)
        return response
