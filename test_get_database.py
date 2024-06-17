import pytest
import allure

from client.common.base_class import ResponseHandler
from client.databases.get_database.api import Databases
from client.databases.get_database.model import RESPONSE_SCHEMA



@pytest.mark.schemabased
@allure.feature("databases")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that <Databases are obtained correctly>")
@allure.parent_suite("databases")
@allure.suite("schemabased")
def test_get_database_schemabased(client):
    databases = Databases(client.NOTION_API_BASE_URL, client.DATABASE_ID)
    response = databases.get_database(notion_api_token=client.NOTION_API_TOKEN)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(RESPONSE_SCHEMA, response.json())