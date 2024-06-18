import pytest
import allure
from client.pages.retrieve_page_property.model import*
from client.pages.retrieve_page_property.api import Pages
from client.common.base_class import ResponseHandler


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


@pytest.mark.schemabased
@allure.feature("pages")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a page property returns expected results")
@allure.parent_suite("pages")
@allure.suite("schemabased")
def test_retrieve_page_property_schemabased_unauthorized(client):
    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    pages = Pages(client.NOTION_API_BASE_URL)
    page_id = client.PAGE_ID
    property_id = client.PROPERTY_ID
    response = pages.get_page_property(notion_api_token=NOTION_INVALID_API_TOKEN, page_id=page_id, property_id=property_id)

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(RETRIEVE_PAGE_PROPERTY_RESPONSE_SCHEMA_401_404, response.json())


@pytest.mark.schemabased
@allure.feature("pages")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a page property returns expected results")
@allure.parent_suite("pages")
@allure.suite("schemabased")
def test_retrieve_page_property_invalid_parent_page_id(client):
    pages = Pages(client.NOTION_API_BASE_URL)
    invalid_page_id = "be907abe-510e-4116-a3d1-7ea71018c06f"
    property_id = client.PROPERTY_ID
    response = pages.get_page_property(notion_api_token=client.NOTION_API_TOKEN, page_id=invalid_page_id, property_id=property_id)

    ResponseHandler.verify_response_code(404, response.status_code)
    ResponseHandler.verify_json_schema(RETRIEVE_PAGE_PROPERTY_RESPONSE_SCHEMA_401_404, response.json())


@pytest.mark.schemabased
@allure.feature("pages")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a page property returns expected results")
@allure.parent_suite("pages")
@allure.suite("schemabased")
def test_retrieve_page_property_validation_error(client):
    pages = Pages(client.NOTION_API_BASE_URL)
    page_id = client.PAGE_ID
    property_id = client.PROPERTY_ID
    invalid_property_id = "invalid_property_id"
    response = pages.get_page_property(notion_api_token=client.NOTION_API_TOKEN, page_id=page_id, property_id=invalid_property_id)

    ResponseHandler.verify_response_code(400, response.status_code)
    ResponseHandler.verify_json_schema(RETRIEVE_PAGE_PROPERTY_RESPONSE_SCHEMA_401_404, response.json())
