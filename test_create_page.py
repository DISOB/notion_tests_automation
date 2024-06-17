import pytest
import allure
import random
from client.pages.create_page.model import*
from client.pages.create_page.api import Pages
from client.common.base_class import ResponseHandler

@pytest.mark.schemabased
@allure.feature("pages")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that creating a page returns expected results")
@allure.parent_suite("pages")
@allure.suite("schemabased")
def test_create_page_schemabased(client):
    pages = Pages(client.NOTION_API_BASE_URL)
    random_number = random.randint(1000, 9999)
    properties = {
        "title": [
            {
                "type": "text",
                "text": {
                    "content": f"Example Page {random_number}"
                }
            }
        ]
    }
    response = pages.create_page(notion_api_token=client.NOTION_API_TOKEN, parent_page_id=client.PARENT_PAGE_ID, properties=properties)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(CREATE_PAGE_RESPONSE_SCHEMA, response.json())

@pytest.mark.schemabased
@allure.feature("pages")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that creating a page without authorization returns unauthorized")
@allure.parent_suite("pages")
@allure.suite("schemabased")
def test_create_page_schemabased_unauthorized(client):
    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    pages = Pages(client.NOTION_API_BASE_URL)
    random_number = random.randint(1000, 9999)
    properties = {
        "title": [
            {
                "type": "text",
                "text": {
                    "content": f"Example Page {random_number}"
                }
            }
        ]
    }
    response = pages.create_page(notion_api_token=NOTION_INVALID_API_TOKEN, parent_page_id=client.PARENT_PAGE_ID, properties=properties)

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(CREATE_PAGE_RESPONSE_SCHEMA_401, response.json())