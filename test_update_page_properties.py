import pytest
import allure
import random
from client.pages.update_page_properties.model import*
from client.pages.update_page_properties.api import Pages
from client.common.base_class import ResponseHandler

@pytest.mark.schemabased
@allure.feature("pages")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that updating a page's properties returns expected results")
@allure.parent_suite("pages")
@allure.suite("schemabased")
def test_update_page_properties_schemabased(client):
    pages = Pages(client.NOTION_API_BASE_URL)
    page_id = client.PAGE_TO_UPDATE_ID
    random_number = random.randint(1000, 9999)
    new_title = f"Page to update. Updated Page Title {random_number}"
    properties = {
        "title": {
            "title": [
                {
                    "text": {
                        "content": new_title
                    }
                }
            ]
        }
    }
    response = pages.update_page(notion_api_token=client.NOTION_API_TOKEN, page_id=page_id, properties=properties)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(UPDATE_PAGE_RESPONSE_SCHEMA, response.json())


@pytest.mark.schemabased
@allure.feature("pages")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that updating a page's properties returns expected results")
@allure.parent_suite("pages")
@allure.suite("schemabased")
def test_update_page_properties_schemabased_unauthorized(client):
    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    pages = Pages(client.NOTION_API_BASE_URL)
    page_id = client.PAGE_TO_UPDATE_ID
    random_number = random.randint(1000, 9999)
    new_title = f"Page to update. Updated Page Title {random_number}"
    properties = {
        "title": {
            "title": [
                {
                    "text": {
                        "content": new_title
                    }
                }
            ]
        }
    }
    response = pages.update_page(notion_api_token=NOTION_INVALID_API_TOKEN, page_id=page_id, properties=properties)

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(UPDATE_PAGE_RESPONSE_SCHEMA_401, response.json())
