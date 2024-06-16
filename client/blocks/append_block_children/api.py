from client.common.base_class import RequestSender

class Blocks(RequestSender):
    RESOURCE = "/v1/blocks"

    def __init__(self, host):
        RequestSender.__init__(self)
        self.endpoint = f"{host}{self.RESOURCE}"

    def append_block_children(self, notion_api_token, block_id, children):
        url = f"{self.endpoint}/{block_id}/children"
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        data = {
            "children": children
        }
        response = self.send_request("PATCH", url=url, headers=headers, json=data)
        return response
