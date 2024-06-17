import pytest
import allure
from client.pages.get_page.model import*
from client.pages.get_page.api import Pages
from client.common.base_class import ResponseHandler

@pytest.mark.schemabased
@allure.feature("pages")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a page returns expected results")
@allure.parent_suite("pages")
@allure.suite("schemabased")
def test_get_page_schemabased(client):
    pages = Pages(client.NOTION_API_BASE_URL)
    page_id = client.PAGE_ID
    response = pages.get_page(notion_api_token=client.NOTION_API_TOKEN, page_id=page_id)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(GET_PAGE_RESPONSE_SCHEMA, response.json())


@pytest.mark.schemabased
@allure.feature("pages")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a page returns expected results")
@allure.parent_suite("pages")
@allure.suite("schemabased")
def test_get_page_schemabased_unauthorized(client):
    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    pages = Pages(client.NOTION_API_BASE_URL)
    page_id = client.PAGE_ID
    response = pages.get_page(notion_api_token=NOTION_INVALID_API_TOKEN, page_id=page_id)

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(GET_PAGE_RESPONSE_SCHEMA_401_404, response.json())


@pytest.mark.schemabased
@allure.feature("pages")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a page returns expected results")
@allure.parent_suite("pages")
@allure.suite("schemabased")
def test_get_page_invalid_parent_page_id(client):
    invalid_parent_page_id = "be907abe-510e-4116-a3d1-7ea71018c06f"
    pages = Pages(client.NOTION_API_BASE_URL)
    page_id = invalid_parent_page_id
    response = pages.get_page(notion_api_token=client.NOTION_API_TOKEN, page_id=page_id)

    ResponseHandler.verify_response_code(404, response.status_code)
    ResponseHandler.verify_json_schema(GET_PAGE_RESPONSE_SCHEMA_401_404, response.json())