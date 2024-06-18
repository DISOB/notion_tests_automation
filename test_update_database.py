import pytest
import allure
from client.databases.update_database.model import*
from client.databases.update_database.api import Databases
from client.common.base_class import ResponseHandler


@pytest.mark.schemabased
@allure.feature("databases")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that updating a database returns expected results")
@allure.parent_suite("databases")
@allure.suite("schemabased")
def test_update_database_schemabased(client):
    databases = Databases(client.NOTION_API_BASE_URL)
    properties = {
        "status": {
            "select": {
                "options": [
                    {
                        "id": "not-started",
                        "name": "Not started",
                        "color": "default"
                    },
                    {
                        "id": "in-progress",
                        "name": "In progress",
                        "color": "blue"
                    },
                    {
                        "id": "done",
                        "name": "Done",
                        "color": "green"
                    },
                    {
                        "id": "archived",
                        "name": "Archived",
                        "color": "gray"
                    }
                ]
            }
        }
    }
    response = databases.update_database(notion_api_token=client.NOTION_API_TOKEN, database_id=client.DATABASE_TO_UPDATE_ID, properties=properties)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(UPDATE_DATABASE_RESPONSE_SCHEMA, response.json())


@pytest.mark.schemabased
@allure.feature("databases")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that updating a database returns expected results")
@allure.parent_suite("databases")
@allure.suite("schemabased")
def test_update_database_schemabased_unauthorized(client):
    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    databases = Databases(client.NOTION_API_BASE_URL)
    properties = {
        "status": {
            "select": {
                "options": [
                    {
                        "id": "not-started",
                        "name": "Not started",
                        "color": "default"
                    },
                    {
                        "id": "in-progress",
                        "name": "In progress",
                        "color": "blue"
                    },
                    {
                        "id": "done",
                        "name": "Done",
                        "color": "green"
                    },
                    {
                        "id": "archived",
                        "name": "Archived",
                        "color": "gray"
                    }
                ]
            }
        }
    }
    response = databases.update_database(notion_api_token=NOTION_INVALID_API_TOKEN, database_id=client.DATABASE_TO_UPDATE_ID, properties=properties)

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(UPDATE_DATABASE_RESPONSE_SCHEMA_401, response.json())


@pytest.mark.schemabased
@allure.feature("databases")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that updating a database returns expected results")
@allure.parent_suite("databases")
@allure.suite("schemabased")
def test_update_database_validation_error(client):
    databases = Databases(client.NOTION_API_BASE_URL)
    properties = {
        "status": {
            "select": {
                "options": "String"
            }
        }
    }
    response = databases.update_database(notion_api_token=client.NOTION_API_TOKEN, database_id=client.DATABASE_TO_UPDATE_ID, properties=properties)

    ResponseHandler.verify_response_code(400, response.status_code)
    ResponseHandler.verify_json_schema(UPDATE_DATABASE_RESPONSE_SCHEMA_401, response.json())


@pytest.mark.schemabased
@allure.feature("databases")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that updating a database returns expected results")
@allure.parent_suite("databases")
@allure.suite("schemabased")
def test_update_database_invalid_parent_page_id(client):
    invalid_page_id = "be907abe-510e-4116-a3d1-7ea71018c06f"
    databases = Databases(client.NOTION_API_BASE_URL)
    properties = {
        "status": {
            "select": {
                "options": [
                    {
                        "id": "not-started",
                        "name": "Not started",
                        "color": "default"
                    },
                    {
                        "id": "in-progress",
                        "name": "In progress",
                        "color": "blue"
                    },
                    {
                        "id": "done",
                        "name": "Done",
                        "color": "green"
                    },
                    {
                        "id": "archived",
                        "name": "Archived",
                        "color": "gray"
                    }
                ]
            }
        }
    }
    response = databases.update_database(notion_api_token=client.NOTION_API_TOKEN, database_id=invalid_page_id, properties=properties)

    ResponseHandler.verify_response_code(404, response.status_code)
    ResponseHandler.verify_json_schema(UPDATE_DATABASE_RESPONSE_SCHEMA_401, response.json())
