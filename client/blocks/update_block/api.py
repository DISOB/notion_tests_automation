from client.common.base_class import RequestSender


class Blocks(RequestSender):
    RESOURCE = "/v1/blocks"

    def __init__(self, host):
        RequestSender.__init__(self)
        self.endpoint = f"{host}{self.RESOURCE}"

    def update_block(self, notion_api_token, block_id, rich_text):
        url = f"{self.endpoint}/{block_id}"
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        data = {
            "paragraph": {
                "rich_text": rich_text,
            }
        }

        response = self.send_request("PATCH", url=url, headers=headers, json=data)
        return response
