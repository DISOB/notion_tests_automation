from client.common.base_class import RequestSender

class Blocks(RequestSender):
    RESOURCE = "/v1/blocks"

    def __init__(self, host, block_id):
        RequestSender.__init__(self)
        self.endpoint = f"{host}{self.RESOURCE}/{block_id}"
        self.block_id = block_id

    def get_block(self, notion_api_token):
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        response = self.send_request("GET", url=self.endpoint, headers=headers)
        return response
