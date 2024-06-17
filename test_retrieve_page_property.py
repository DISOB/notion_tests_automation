import pytest
import allure
from client.pages.retrieve_page_property.model import RETRIEVE_PAGE_PROPERTY_RESPONSE_SCHEMA
from client.pages.retrieve_page_property.api import Pages
from client.common.base_class import ResponseHandler

# Не хватает property_id в client. Нужно узнать, как получить property_id

@pytest.mark.schemabased
@allure.feature("pages")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a page property returns expected results")
@allure.parent_suite("pages")
@allure.suite("schemabased")
def test_retrieve_page_property_schemabased(client):
    pages = Pages(client.NOTION_API_BASE_URL)
    page_id = client.PAGE_ID
    property_id = client.PROPERTY_ID
    response = pages.get_page_property(notion_api_token=client.NOTION_API_TOKEN, page_id=page_id, property_id=property_id)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(RETRIEVE_PAGE_PROPERTY_RESPONSE_SCHEMA, response.json())
