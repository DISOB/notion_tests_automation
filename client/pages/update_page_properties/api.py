from client.common.base_class import RequestSender

class Pages(RequestSender):
    RESOURCE = "/v1/pages"

    def __init__(self, host):
        RequestSender.__init__(self)
        self.endpoint = f"{host}{self.RESOURCE}"

    def update_page(self, notion_api_token, page_id, properties):
        url = f"{self.endpoint}/{page_id}"
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        data = {
            "properties": properties
        }
        response = self.send_request("PATCH", url=url, headers=headers, json=data)
        return response
