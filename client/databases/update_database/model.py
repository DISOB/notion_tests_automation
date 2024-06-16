UPDATE_RESPONSE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "object": {"type": "string"},
        "id": {"type": "string"},
        "created_time": {"type": "string", "format": "date-time"},
        "last_edited_time": {"type": "string", "format": "date-time"},
        "title": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {"type": "string"},
                    "text": {
                        "type": "object",
                        "properties": {
                            "content": {"type": "string"},
                            "link": {"type": ["null", "object"]}
                        },
                        "required": ["content"]
                    },
                    "annotations": {
                        "type": "object",
                        "properties": {
                            "bold": {"type": "boolean"},
                            "italic": {"type": "boolean"},
                            "strikethrough": {"type": "boolean"},
                            "underline": {"type": "boolean"},
                            "code": {"type": "boolean"},
                            "color": {"type": "string"}
                        },
                        "required": ["bold", "italic", "strikethrough", "underline", "code", "color"]
                    },
                    "plain_text": {"type": "string"},
                    "href": {"type": ["null", "string"]}
                },
                "required": ["type", "text", "annotations", "plain_text"]
            }
        },
        "properties": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "type": {"type": "string"}
                },
                "required": ["id", "name", "type"],
                "additionalProperties": True
            }
        },
        "parent": {
            "type": "object",
            "properties": {
                "type": {"type": "string"},
                "page_id": {"type": "string", "format": "uuid"}
            },
            "required": ["type", "page_id"]
        },
        "archived": {"type": "boolean"},
        "is_inline": {"type": "boolean"},
        "public_url": {"type": ["null", "string"]}
    },
    "required": ["object", "id", "created_time", "last_edited_time", "title", "properties", "parent", "archived", "is_inline"]
}
