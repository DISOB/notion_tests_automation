import pytest
import allure

from client.common.base_class import ResponseHandler
from client.comments.create_comment.api import Comments
from client.comments.create_comment.model import*

@pytest.mark.schemabased
@allure.feature("commnts")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that creating a comment returns expected results")
@allure.parent_suite("comments")
@allure.suite("schemabased")
def test_create_comment_schemabased(client):
    comments = Comments(client.NOTION_API_BASE_URL)
    parent_id = client.PAGE_ID
    parent_type = "page_id"
    rich_text = [{
        "type": "text",
        "text": {
            "content": "This is a test comment",
            "link": None
        }
    }]
    response = comments.create_comment(notion_api_token=client.NOTION_API_TOKEN, parent_id=parent_id, parent_type=parent_type, rich_text=rich_text)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(RESPONSE_SCHEMA, response.json())


@pytest.mark.schemabased
@allure.feature("comments")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that creating a comment returns expected results")
@allure.parent_suite("comments")
@allure.suite("schemabased")
def test_create_comment_schemabased_unauthorized(client):
    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    comments = Comments(client.NOTION_API_BASE_URL)
    parent_id = client.PAGE_ID
    parent_type = "page_id"
    rich_text = [{
        "type": "text",
        "text": {
            "content": "This is a test comment",
            "link": None
        }
    }]
    response = comments.create_comment(notion_api_token=NOTION_INVALID_API_TOKEN, parent_id=parent_id, parent_type=parent_type, rich_text=rich_text)

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(RESPONSE_SCHEMA_401, response.json())