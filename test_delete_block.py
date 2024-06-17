import pytest
import allure
import random
from client.blocks.delete_block.model import*
from client.blocks.delete_block.api import Blocks as Delete_Blocks
from client.blocks.append_block_children.api import Blocks as Append_Blocks
from client.common.base_class import ResponseHandler


@pytest.mark.schemabased
@allure.feature("blocks")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that appending children to a block returns expected results")
@allure.parent_suite("blocks")
@allure.suite("schemabased")
def test_delete_block_schemabased(client):
    """
    создает блок с названием BLOCK FOR DELETE, потом из его response получает id и удаляет блок по этому id
    :param client:
    :return:
    """
    delete_blocks = Delete_Blocks(client.NOTION_API_BASE_URL)
    append_blocks = Append_Blocks(client.NOTION_API_BASE_URL)

    children = [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": f"BLOCK FOR DELETE"
                        }
                    }
                ]
            }
        }
    ]
    response = append_blocks.append_block_children(notion_api_token=client.NOTION_API_TOKEN, block_id=client.PARENT_PAGE_ID, children=children)

    block_id = response.json()["results"][0]["id"]

    response = delete_blocks.delete_block(notion_api_token=client.NOTION_API_TOKEN, block_id=block_id)

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(DELETE_BLOCK_RESPONSE_SCHEMA, response.json())


@pytest.mark.schemabased
@allure.feature("blocks")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that appending children to a block returns expected results")
@allure.parent_suite("blocks")
@allure.suite("schemabased")
def test_delete_block_schemabased_unauthorized(client):
    """
    создает блок с названием BLOCK FOR DELETE, потом из его response получает id и удаляет блок по этому id
    :param client:
    :return:
    """
    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    delete_blocks = Delete_Blocks(client.NOTION_API_BASE_URL)
    append_blocks = Append_Blocks(client.NOTION_API_BASE_URL)

    children = [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": f"BLOCK FOR DELETE"
                        }
                    }
                ]
            }
        }
    ]
    response = append_blocks.append_block_children(notion_api_token=client.NOTION_API_TOKEN, block_id=client.PARENT_PAGE_ID, children=children)

    block_id = response.json()["results"][0]["id"]

    response = delete_blocks.delete_block(notion_api_token=NOTION_INVALID_API_TOKEN, block_id=block_id)

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(DELETE_BLOCK_RESPONSE_SCHEMA_400_401_404, response.json())


