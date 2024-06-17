import pytest
import allure
from client.users.retrieve_bot_user.model import*
from client.users.retrieve_bot_user.api import Users
from client.common.base_class import ResponseHandler

@pytest.mark.schemabased
@allure.feature("users")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving the bot user returns expected results")
@allure.parent_suite("users")
@allure.suite("schemabased")
def test_retrieve_bot_user_schemabased(client):
    users = Users(client.NOTION_API_BASE_URL)
    response = users.retrieve_bot_user(notion_api_token=client.NOTION_API_TOKEN)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(RETRIEVE_BOT_USER_RESPONSE_SCHEMA, response.json())


@pytest.mark.schemabased
@allure.feature("users")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving the bot user returns expected results")
@allure.parent_suite("users")
@allure.suite("schemabased")
def test_retrieve_bot_user_schemabased_unauthorized(client):
    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    users = Users(client.NOTION_API_BASE_URL)
    response = users.retrieve_bot_user(notion_api_token=NOTION_INVALID_API_TOKEN)

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(RETRIEVE_BOT_USER_RESPONSE_SCHEMA_401, response.json())