from client.common.base_class import RequestSender


class Pages(RequestSender):
    RESOURCE = "/v1/pages"

    def __init__(self, host):
        RequestSender.__init__(self)
        self.endpoint = f"{host}{self.RESOURCE}"

    def get_page(self, notion_api_token, page_id):
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        response = self.send_request("GET", url=f"{self.endpoint}/{page_id}", headers=headers)
        return response

    def get_page_property(self, notion_api_token, page_id, property_id):
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        response = self.send_request("GET", url=f"{self.endpoint}/{page_id}/properties/{property_id}", headers=headers)
        return response
