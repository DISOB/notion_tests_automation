import pytest
import allure
import random
from client.blocks.append_block_children.model import*
from client.blocks.append_block_children.api import Blocks
from client.common.base_class import ResponseHandler

@pytest.mark.schemabased
@allure.feature("blocks")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that appending children to a block returns expected results")
@allure.parent_suite("blocks")
@allure.suite("schemabased")
def test_append_block_children_schemabased(client):
    blocks = Blocks(client.NOTION_API_BASE_URL)
    parent_page_id = client.PARENT_PAGE_ID
    random_number = random.randint(1000, 9999)
    children = [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": f"Example Block {random_number}"
                        }
                    }
                ]
            }
        }
    ]
    response = blocks.append_block_children(notion_api_token=client.NOTION_API_TOKEN, block_id=parent_page_id, children=children)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(APPEND_BLOCK_CHILDREN_RESPONSE_SCHEMA, response.json())


@pytest.mark.schemabased
@allure.feature("blocks")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that appending children to a block returns expected results")
@allure.parent_suite("blocks")
@allure.suite("schemabased")
def test_append_block_children_schemabased_unauthorized(client):
    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    blocks = Blocks(client.NOTION_API_BASE_URL)
    parent_page_id = client.PARENT_PAGE_ID
    random_number = random.randint(1000, 9999)
    children = [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": f"Example Block {random_number}"
                        }
                    }
                ]
            }
        }
    ]
    response = blocks.append_block_children(notion_api_token=NOTION_INVALID_API_TOKEN, block_id=parent_page_id, children=children)

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(APPEND_BLOCK_CHILDREN_RESPONSE_SCHEMA_401, response.json())
