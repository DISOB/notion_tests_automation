import pytest
import allure
import copy
from client.common.base_class import ResponseHandler
from client.blocks.get_block_children.api import Blocks as Get_Blocks
from client.blocks.append_block_children.api import Blocks as Append_Blocks
from client.blocks.delete_block.api import Blocks as Delete_Blocks
from client.blocks.get_block_children.model import*


@pytest.fixture()
def processing(client):
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
        blocks.append((response := append_blocks.append_block_children(notion_api_token=client.NOTION_API_TOKEN, block_id=client.PAGE_FOR_GET_CHILD_ID, children=children)).json()["results"][0]["id"])
        ResponseHandler.verify_response_code(200, response.status_code)

    yield page_size

    delete_blocks = Delete_Blocks(client.NOTION_API_BASE_URL)
    for block in blocks:
        delete_blocks.delete_block(notion_api_token=client.NOTION_API_TOKEN, block_id=block)


@pytest.mark.schemabased
@allure.feature("blocks")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a block returns expected results")
@allure.parent_suite("blocks")
@allure.suite("schemabased")
def test_get_block_children_schemabased(client, processing):
    page_size = processing

    get_blocks = Get_Blocks(client.NOTION_API_BASE_URL)
    response = get_blocks.get_block_children(notion_api_token=client.NOTION_API_TOKEN, page_id=client.PAGE_FOR_GET_CHILD_ID, page_size=page_size)

    schema = copy.deepcopy(GET_BLOCK_CHILDREN_RESPONSE_SCHEMA)
    schema["properties"]["results"]["items"] *= page_size

    ResponseHandler.verify_response_code(200, response.status_code)
    ResponseHandler.verify_json_schema(schema, response.json())


@pytest.mark.schemabased
@allure.feature("blocks")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a block returns expected results")
@allure.parent_suite("blocks")
@allure.suite("schemabased")
def test_get_block_children_schemabased_unauthorized(client, processing):
    """
    Сложная функция:
    1. создаются несколько блоков в цикле
    2. сохраняются их id
    3. происходит получение этих блоков
    4. они все удаляются по сохраненным id
    :param client:
    :return:
    """

    NOTION_INVALID_API_TOKEN = "INVALID_TOKEN"
    page_size = processing

    get_blocks = Get_Blocks(client.NOTION_API_BASE_URL)
    response = get_blocks.get_block_children(notion_api_token=NOTION_INVALID_API_TOKEN, page_id=client.PAGE_FOR_GET_CHILD_ID, page_size=page_size)

    # schema = copy.deepcopy(GET_BLOCK_CHILDREN_RESPONSE_SCHEMA)
    # schema["properties"]["results"]["items"] *= page_size

    ResponseHandler.verify_response_code(401, response.status_code)
    ResponseHandler.verify_json_schema(GET_BLOCK_CHILDREN_RESPONSE_SCHEMA_401_404, response.json())


@pytest.mark.schemabased
@allure.feature("blocks")
@allure.severity("allure.severity_level.CRITICAL")
@allure.description("Verify that retrieving a block returns expected results")
@allure.parent_suite("blocks")
@allure.suite("schemabased")
def test_get_block_children_invalid_parent_page_id(client, processing):
    page_size = processing
    invalid_parent_page_id = "be907abe-510e-4116-a3d1-7ea71018c06f"
    get_blocks = Get_Blocks(client.NOTION_API_BASE_URL)
    response = get_blocks.get_block_children(notion_api_token=client.NOTION_API_TOKEN, page_id=invalid_parent_page_id, page_size=page_size)

    # schema = copy.deepcopy(GET_BLOCK_CHILDREN_RESPONSE_SCHEMA)
    # schema["properties"]["results"]["items"] *= page_size

    ResponseHandler.verify_response_code(404, response.status_code)
    ResponseHandler.verify_json_schema(GET_BLOCK_CHILDREN_RESPONSE_SCHEMA_401_404, response.json())


