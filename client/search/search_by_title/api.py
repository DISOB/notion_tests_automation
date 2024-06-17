from client.common.base_class import RequestSender

class Search(RequestSender):
    RESOURCE = "/v1/search"

    def __init__(self, host):
        RequestSender.__init__(self)
        self.endpoint = f"{host}{self.RESOURCE}"

    def search_by_title(self, notion_api_token, query, page_size=10):
        headers = {
            "Authorization": f"Bearer {notion_api_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        body = {
            "query": query,
            "page_size": page_size,
            "sort": {
                "direction": "ascending",
                "timestamp": "last_edited_time"
            },
            "filter": {
                "value": "page",
                "property": "object"
            }
        }
        response = self.send_request("POST", url=self.endpoint, headers=headers, json=body)
        return response
