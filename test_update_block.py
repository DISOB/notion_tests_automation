import pytest
import allure
import random
from client.blocks.update_block.model import UPDATE_BLOCK_RESPONSE_SCHEMA
from client.blocks.update_block.api import Blocks
from client.common.base_class import ResponseHandler


@pytest.mark.schemabased
@allure.feature("blocks")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that appending children to a block returns expected results")
@allure.parent_suite("blocks")
@allure.suite("schemabased")
def test_update_block_schemabased(client):
    blocks = Blocks(client.NOTION_API_BASE_URL)
    random_number = random.randint(1000, 9999)
    rich_text = [{
        "text": {"content": f"Block id here ({random_number})"}
    }]
    response = blocks.update_block(notion_api_token=client.NOTION_API_TOKEN, block_id=client.BLOCK_ID, rich_text=rich_text)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(UPDATE_BLOCK_RESPONSE_SCHEMA, response.json())