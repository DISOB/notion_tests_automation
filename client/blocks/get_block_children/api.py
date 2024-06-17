from client.common.base_class import RequestSender


class Blocks(RequestSender):
    RESOURCE = "/v1/blocks"

    def __init__(self, host):
        RequestSender.__init__(self)
        self.endpoint = f"{host}{self.RESOURCE}"

    def get_block_children(self, notion_api_token, page_id, page_size):
        url = f"{self.endpoint}/{page_id}/children?page_size={page_size}"
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
        }

        response = self.send_request("GET", url=url, headers=headers)
        return response
