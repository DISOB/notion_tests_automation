import pytest
import allure
from client.databases.query_database.model import*
from client.databases.query_database.api import Databases
from client.common.base_class import ResponseHandler

@pytest.mark.schemabased
@allure.feature("databases")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that querying the database returns expected results")
@allure.parent_suite("databases")
@allure.suite("schemabased")
def test_query_database_schemabased(client):
    databases = Databases(client.NOTION_API_BASE_URL, client.DATABASE_ID)
    filter_criteria = {
        "property": "Status",
        "status": {
            "equals": "Done"
        }
    }
    response = databases.query_database(notion_api_token=client.NOTION_API_TOKEN, filter=filter_criteria)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(QUERY_RESPONSE_SCHEMA, response.json())


@pytest.mark.schemabased
@allure.feature("databases")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that querying the database returns expected results")
@allure.parent_suite("databases")
@allure.suite("schemabased")
def test_query_database_schemabased_unauthorized(client):
    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    databases = Databases(client.NOTION_API_BASE_URL, client.DATABASE_ID)
    filter_criteria = {
        "property": "Status",
        "status": {
            "equals": "Done"
        }
    }
    response = databases.query_database(notion_api_token=NOTION_INVALID_API_TOKEN, filter=filter_criteria)

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(QUERY_RESPONSE_SCHEMA_400_401_404, response.json())


@pytest.mark.schemabased
@allure.feature("databases")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that querying the database returns expected results")
@allure.parent_suite("databases")
@allure.suite("schemabased")
def test_query_database_validation_error(client):
    databases = Databases(client.NOTION_API_BASE_URL, client.DATABASE_ID)
    filter_criteria = {
        "property": "String",
        "status": {
            "equals": "Done"
        }
    }
    response = databases.query_database(notion_api_token=client.NOTION_API_TOKEN, filter=filter_criteria)

    ResponseHandler.verify_response_code(400, response.status_code)
    ResponseHandler.verify_json_schema(QUERY_RESPONSE_SCHEMA_400_401_404, response.json())


@pytest.mark.schemabased
@allure.feature("databases")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that querying the database returns expected results")
@allure.parent_suite("databases")
@allure.suite("schemabased")
def test_query_database_invalid_parent_page_id(client):
    invalid_parent_page_id = "be907abe-510e-4116-a3d1-7ea71018c06f"
    databases = Databases(client.NOTION_API_BASE_URL, invalid_parent_page_id)
    filter_criteria = {
        "property": "Status",
        "status": {
            "equals": "Done"
        }
    }
    response = databases.query_database(notion_api_token=client.NOTION_API_TOKEN, filter=filter_criteria)

    ResponseHandler.verify_response_code(404, response.status_code)
    ResponseHandler.verify_json_schema(QUERY_RESPONSE_SCHEMA_400_401_404, response.json())