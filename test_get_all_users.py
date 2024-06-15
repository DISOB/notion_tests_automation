import pytest
import allure

from client.common.base_class import ResponseHandler
from client.users.get_all_users.api import Users
from client.users.get_all_users.model import RESPONSE_SCHEMA


@pytest.mark.schemabased
@allure.feature("users")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that <add desc>")
@allure.parent_suite("users")
@allure.suite("schemabased")
def test_get_all_users_schemabased(client):
    users = Users(client.NOTION_API_BASE_URL)
    response = users.get_all_users(notion_api_token=client.NOTION_API_TOKEN)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(RESPONSE_SCHEMA, response.json())
