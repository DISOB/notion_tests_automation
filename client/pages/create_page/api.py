from client.common.base_class import RequestSender

class Pages(RequestSender):
    RESOURCE = "/v1/pages"

    def __init__(self, host):
        RequestSender.__init__(self)
        self.endpoint = f"{host}{self.RESOURCE}"

    def create_page(self, notion_api_token, parent_page_id, properties):
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        data = {
            "parent": {"type": "page_id", "page_id": parent_page_id},
            "properties": properties
        }
        response = self.send_request("POST", url=self.endpoint, headers=headers, json=data)
        return response
