from client.common.base_class import RequestSender

class Databases(RequestSender):
    RESOURCE = "/v1/databases"

    def __init__(self, host):
        RequestSender.__init__(self)
        self.host = host

    def update_database(self, notion_api_token, database_id, properties):
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        endpoint = f"{self.host}{self.RESOURCE}/{database_id}"
        data = {"properties": properties}
        response = self.send_request("PATCH", url=endpoint, headers=headers, json=data)
        return response
