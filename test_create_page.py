import pytest
import allure
from client.pages.create_page.model import CREATE_PAGE_RESPONSE_SCHEMA
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
    properties = {
        "title": [
            {
                "type": "text",
                "text": {
                    "content": "Test Page"
                }
            }
        ]
    }
    response = pages.create_page(notion_api_token=client.NOTION_API_TOKEN, parent_page_id=client.PARENT_PAGE_ID, properties=properties)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(CREATE_PAGE_RESPONSE_SCHEMA, response.json())
