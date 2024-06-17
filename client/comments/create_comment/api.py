from client.common.base_class import RequestSender

class Comments(RequestSender):
    RESOURCE = "/v1/comments"

    def __init__(self, host):
        RequestSender.__init__(self)
        self.endpoint = f"{host}{self.RESOURCE}"

    def create_comment(self, notion_api_token, parent_id, parent_type, rich_text):
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        body = {
            "parent": {
                "type": parent_type,
                parent_type: parent_id
            },
            "rich_text": rich_text
        }
        response = self.send_request("POST", url=self.endpoint, headers=headers, json=body)
        return response
