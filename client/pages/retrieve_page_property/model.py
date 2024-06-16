RETRIEVE_PAGE_PROPERTY_RESPONSE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "object": {"type": "string"},
        "type": {"type": "string"},
        "id": {"type": "string"},
        "next_url": {"type": ["null", "string"], "format": "uri"},
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "object": {"type": "string"},
                    "type": {"type": "string"},
                    "rich_text": {
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
                    }
                },
                "required": ["object", "type", "rich_text"]
            }
        }
    },
    "required": ["object", "type", "id", "results"]
}
