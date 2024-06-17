import pytest
import allure
import random
from client.databases.create_database.model import*
from client.databases.create_database.api import Databases
from client.common.base_class import ResponseHandler

@pytest.mark.schemabased
@allure.feature("databases")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that creating a database returns expected results")
@allure.parent_suite("databases")
@allure.suite("schemabased")
def test_create_database_schemabased(client):
    databases = Databases(client.NOTION_API_BASE_URL, client.PARENT_PAGE_ID)
    random_number = random.randint(1000, 9999)
    title = f"Example Database {random_number}"
    properties = {
        "Name": {
            "title": {}
        },
        "Tags": {
            "multi_select": {
                "options": [
                    {"name": "Tag1"},
                    {"name": "Tag2"}
                ]
            }
        }
    }
    response = databases.create_database(notion_api_token=client.NOTION_API_TOKEN, title=title, properties=properties)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(CREATE_RESPONSE_SCHEMA, response.json())


@pytest.mark.schemabased
@allure.feature("databases")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that creating a database returns expected results")
@allure.parent_suite("databases")
@allure.suite("schemabased")
def test_create_database_schemabased_unauthorized(client):
    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    databases = Databases(client.NOTION_API_BASE_URL, client.PARENT_PAGE_ID)
    random_number = random.randint(1000, 9999)
    title = f"Example Database {random_number}"
    properties = {
        "Name": {
            "title": {}
        },
        "Tags": {
            "multi_select": {
                "options": [
                    {"name": "Tag1"},
                    {"name": "Tag2"}
                ]
            }
        }
    }
    response = databases.create_database(notion_api_token=NOTION_INVALID_API_TOKEN, title=title, properties=properties)

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(CREATE_RESPONSE_SCHEMA_401, response.json())