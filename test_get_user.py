import pytest
import allure
from client.users.get_user.model import*
from client.users.get_user.api import Users
from client.common.base_class import ResponseHandler

@pytest.mark.schemabased
@allure.feature("users")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a user returns expected results")
@allure.parent_suite("users")
@allure.suite("schemabased")
def test_get_user_schemabased(client):
    users = Users(client.NOTION_API_BASE_URL)
    user_id = client.USER_ID
    response = users.get_user(notion_api_token=client.NOTION_API_TOKEN, user_id=user_id)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(GET_USER_RESPONSE_SCHEMA, response.json())


@pytest.mark.schemabased
@allure.feature("users")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a user returns expected results")
@allure.parent_suite("users")
@allure.suite("schemabased")
def test_get_user_schemabased_unauthorized(client):
    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    users = Users(client.NOTION_API_BASE_URL)
    user_id = client.USER_ID
    response = users.get_user(notion_api_token=NOTION_INVALID_API_TOKEN, user_id=user_id)

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(GET_USER_RESPONSE_SCHEMA_401_404, response.json())


@pytest.mark.schemabased
@allure.feature("users")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a user returns expected results")
@allure.parent_suite("users")
@allure.suite("schemabased")
def test_get_user_invalid_parent_page_id(client):
    users = Users(client.NOTION_API_BASE_URL)
    invalid_parent_page_id = "be907abe-510e-4116-a3d1-7ea71018c06f"
    user_id = invalid_parent_page_id
    response = users.get_user(notion_api_token=client.NOTION_API_TOKEN, user_id=user_id)

    ResponseHandler.verify_response_code(404, response.status_code)
    ResponseHandler.verify_json_schema(GET_USER_RESPONSE_SCHEMA_401_404, response.json())
