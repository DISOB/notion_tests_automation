import pytest
import allure
from client.common.base_class import ResponseHandler
from client.comments.get_comments.api import Comments
from client.comments.get_comments.model import*

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


@pytest.mark.schemabased
@allure.feature("comments")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving comments returns expected results")
@allure.parent_suite("comments")
@allure.suite("schemabased")
def test_get_comments_schemabased_unauthorized(client):
    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    comments = Comments(client.NOTION_API_BASE_URL, client.PAGE_ID)
    response = comments.get_comments(notion_api_token=NOTION_INVALID_API_TOKEN)

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(RESPONSE_SCHEMA_401_404, response.json())


@pytest.mark.schemabased
@allure.feature("comments")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving comments returns expected results")
@allure.parent_suite("comments")
@allure.suite("schemabased")
def test_get_comments_invalid_parent_page_id(client):
    invalid_parent_page_id = "be907abe-510e-4116-a3d1-7ea71018c06f"
    comments = Comments(client.NOTION_API_BASE_URL, invalid_parent_page_id)
    response = comments.get_comments(notion_api_token=client.NOTION_API_TOKEN)

    ResponseHandler.verify_response_code(404, response.status_code)
    ResponseHandler.verify_json_schema(RESPONSE_SCHEMA_401_404, response.json())