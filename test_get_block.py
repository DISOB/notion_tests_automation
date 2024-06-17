import pytest
import allure
from client.common.base_class import ResponseHandler
from client.blocks.get_block.api import Blocks
from client.blocks.get_block.model import*

@pytest.mark.schemabased
@allure.feature("blocks")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a block returns expected results")
@allure.parent_suite("blocks")
@allure.suite("schemabased")
def test_get_block_schemabased(client):
    blocks = Blocks(client.NOTION_API_BASE_URL, client.BLOCK_ID)
    response = blocks.get_block(notion_api_token=client.NOTION_API_TOKEN)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(RESPONSE_SCHEMA, response.json())


@pytest.mark.schemabased
@allure.feature("blocks")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a block returns expected results")
@allure.parent_suite("blocks")
@allure.suite("schemabased")
def test_get_block_schemabased_unauthorized(client):
    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    blocks = Blocks(client.NOTION_API_BASE_URL, client.BLOCK_ID)
    response = blocks.get_block(notion_api_token=NOTION_INVALID_API_TOKEN)

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(RESPONSE_SCHEMA_401, response.json())