from client.common.base_class import RequestSender

class Comments(RequestSender):
    RESOURCE = "/v1/comments"

    def __init__(self, host, page_id):
        RequestSender.__init__(self)
        self.endpoint = f"{host}{self.RESOURCE}?block_id={page_id}"
        self.page_id = page_id

    def get_comments(self, notion_api_token):
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        response = self.send_request("GET", url=self.endpoint, headers=headers)
        return response
