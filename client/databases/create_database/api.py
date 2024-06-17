from client.common.base_class import RequestSender


class Databases(RequestSender):
    RESOURCE = "/v1/databases"

    def __init__(self, host, parent_page_id):
        RequestSender.__init__(self)
        self.endpoint = f"{host}{self.RESOURCE}"
        self.parent_page_id = parent_page_id

    def create_database(self, notion_api_token, title, properties):
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        data = {
            "parent": {"type": "page_id", "page_id": self.parent_page_id},
            "title": [{"type": "text", "text": {"content": title}}],
            "properties": properties
        }
        response = self.send_request("POST", url=self.endpoint, headers=headers, json=data)
        return response
