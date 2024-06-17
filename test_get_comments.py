import pytest
import allure

from client.common.base_class import ResponseHandler
from client.comments.get_comments.api import Comments
from client.comments.get_comments.model import RESPONSE_SCHEMA

@pytest.mark.schemabased
@allure.feature("comments")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving comments returns expected results")
@allure.parent_suite("comments")
@allure.suite("schemabased")
def test_get_comments_schemabased(client):
    comments = Comments(client.NOTION_API_BASE_URL, client.PAGE_ID)
    response = comments.get_comments(notion_api_token=client.NOTION_API_TOKEN)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(RESPONSE_SCHEMA, response.json())
