import pytest
import allure
from client.common.base_class import ResponseHandler
from client.search.search_by_title.api import Search
from client.search.search_by_title.model import*

@pytest.mark.schemabased
@allure.feature("search")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that searching by title returns expected results")
@allure.parent_suite("search")
@allure.suite("schemabased")
def test_search_by_title_schemabased(client):
    search = Search(client.NOTION_API_BASE_URL)
    query = "Search here"
    response = search.search_by_title(notion_api_token=client.NOTION_API_TOKEN, query=query)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(RESPONSE_SCHEMA, response.json())


@pytest.mark.schemabased
@allure.feature("search")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that searching by title returns expected results")
@allure.parent_suite("search")
@allure.suite("schemabased")
def test_search_by_title_schemabased_unauthorized(client):
    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    search = Search(client.NOTION_API_BASE_URL)
    query = "Search here"
    response = search.search_by_title(notion_api_token=NOTION_INVALID_API_TOKEN, query=query)

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(RESPONSE_SCHEMA_401, response.json())