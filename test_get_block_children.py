import pytest
import allure
import copy
from client.common.base_class import ResponseHandler
from client.blocks.get_block_children.api import Blocks as Get_Blocks
from client.blocks.append_block_children.api import Blocks as Append_Blocks
from client.blocks.delete_block.api import Blocks as Delete_Blocks
from client.blocks.get_block_children.model import GET_BLOCK_CHILDREN_RESPONSE_SCHEMA


@pytest.mark.schemabased
@allure.feature("blocks")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a block returns expected results")
@allure.parent_suite("blocks")
@allure.suite("schemabased")
def test_get_block_children_schemabased(client):
    """
    Сложная функция:
    1. создаются несколько блоков в цикле
    2. сохраняются их id
    3. происходит получение этих блоков
    4. они все удаляются по сохраненным id
    :param client:
    :return:
    """
    get_blocks = Get_Blocks(client.NOTION_API_BASE_URL)
    page_size = 3

    append_blocks = Append_Blocks(client.NOTION_API_BASE_URL)
    blocks = []
    for i in range(page_size):
        children = [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": f"Example Block {i}"
                            }
                        }
                    ]
                }
            }
        ]
        blocks.append(append_blocks.append_block_children(notion_api_token=client.NOTION_API_TOKEN, block_id=client.PAGE_FOR_GET_CHILD_ID, children=children).json()["results"][0]["id"])

    response = get_blocks.get_block_children(notion_api_token=client.NOTION_API_TOKEN, page_id=client.PAGE_FOR_GET_CHILD_ID, page_size=page_size)

    delete_blocks = Delete_Blocks(client.NOTION_API_BASE_URL)
    for block in blocks:
        delete_blocks.delete_block(notion_api_token=client.NOTION_API_TOKEN, block_id=block)

    schema = copy.deepcopy(GET_BLOCK_CHILDREN_RESPONSE_SCHEMA)
    schema["properties"]["results"]["items"] *= page_size

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(schema, response.json())
