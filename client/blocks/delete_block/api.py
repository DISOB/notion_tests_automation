from client.common.base_class import RequestSender


class Blocks(RequestSender):
    RESOURCE = "/v1/blocks"

    def __init__(self, host):
        RequestSender.__init__(self)
        self.endpoint = f"{host}{self.RESOURCE}"

    def delete_block(self, notion_api_token, block_id):
        url = f"{self.endpoint}/{block_id}"
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
        }

        response = self.send_request("DELETE", url=url, headers=headers)
        return response
