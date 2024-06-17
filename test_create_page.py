import time
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
def test_create_page_unauthorized(client):
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
    ResponseHandler.verify_json_schema(CREATE_PAGE_RESPONSE_SCHEMA_400_401_404, response.json())


@pytest.mark.schemabased
@allure.feature("pages")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that creating a page with invalid JSON returns a 400 status code")
@allure.parent_suite("pages")
@allure.suite("schemabased")
def test_create_page_validation_error(client):
    pages = Pages(client.NOTION_API_BASE_URL)
    # Creating an invalid JSON by omitting required fields or using incorrect types
    invalid_properties = {
        "title": [
            {
                "type": "text",
                # Missing the "text" key which makes this JSON invalid
            }
        ]
    }
    response = pages.create_page(notion_api_token=client.NOTION_API_TOKEN, parent_page_id=client.PARENT_PAGE_ID, properties=invalid_properties)

    ResponseHandler.verify_response_code(400, response.status_code)
    ResponseHandler.verify_json_schema(CREATE_PAGE_RESPONSE_SCHEMA_400_401_404, response.json())



pytest.mark.schemabased
@allure.feature("pages")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that creating a page without authorization returns unauthorized")
@allure.parent_suite("pages")
@allure.suite("schemabased")
def test_create_page_invalid_parent_page_id(client):
    pages = Pages(client.NOTION_API_BASE_URL)
    invalid_parent_page_id = "be907abe-510e-4116-a3d1-7ea71018c06f"
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
    response = pages.create_page(notion_api_token=client.NOTION_API_TOKEN, parent_page_id=invalid_parent_page_id, properties=properties)

    ResponseHandler.verify_response_code(404, response.status_code)
    ResponseHandler.verify_json_schema(CREATE_PAGE_RESPONSE_SCHEMA_400_401_404, response.json())


# @pytest.mark.schemabased
# @allure.feature("pages")
# @allure.severity("allure.severity_level.CRITICAL")
# @allure.description("Verify that creating a page returns expected results")
# @allure.parent_suite("pages")
# @allure.suite("schemabased")
# def test_create_page_schemabased(client):
#     pages = Pages(client.NOTION_API_BASE_URL)
#     properties = {
#         "title": [
#             {
#                 "type": "text",
#                 "text": {
#                     "content": "Example Page"
#                 }
#             }
#         ]
#     }
#     # Отправляем 100 запросов за 1 секунду
#     for _ in range(100):
#         response = pages.create_page(notion_api_token=client.NOTION_API_TOKEN, parent_page_id=client.PARENT_PAGE_ID, properties=properties)
#         time.sleep(0.01)  # Пауза между запросами, чтобы не превысить лимит
#
#     # Проверяем, что сервер вернул ошибку 429
#     ResponseHandler.verify_response_code(429, response.status_code)