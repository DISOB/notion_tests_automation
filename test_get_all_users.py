import pytest
import allure
import requests

from client.common.base_class import ResponseHandler
from client.users.get_all_users.api import Users
from client.users.get_all_users.model import*


@pytest.mark.schemabased
@allure.feature("users")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that <Users are received correctly>")
@allure.parent_suite("users")
@allure.suite("schemabased")
def test_get_all_users_schemabased(client):
    users = Users(client.NOTION_API_BASE_URL)
    response = users.get_all_users(notion_api_token=client.NOTION_API_TOKEN)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(RESPONSE_SCHEMA, response.json())


@pytest.mark.schemabased
@allure.feature("users")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that <Users are received correctly>")
@allure.parent_suite("users")
@allure.suite("schemabased")
def test_get_all_users_schemabased_unauthorized(client):
    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    users = Users(client.NOTION_API_BASE_URL)
    response = users.get_all_users(notion_api_token=NOTION_INVALID_API_TOKEN)

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(RESPONSE_SCHEMA_401, response.json())




