from client.common.base_class import RequestSender


class Databases(RequestSender):
    RESOURCE = "/v1/databases"

    def __init__(self, host, database_id):
        RequestSender.__init__(self)
        self.endpoint = f"{host}{self.RESOURCE}/{database_id}"
        self.database_id = database_id

    def query_database(self, notion_api_token, filter):
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        data = {
            "filter": filter
        }
        response = self.send_request("POST", url=f"{self.endpoint}/query", headers=headers, json=data)
        return response
