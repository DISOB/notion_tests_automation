APPEND_BLOCK_CHILDREN_RESPONSE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "object": {
            "type": "string"
        },
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "object": {
                        "type": "string"
                    },
                    "id": {
                        "type": "string",
                        "format": "uuid"
                    },
                    "type": {
                        "type": "string"
                    },
                    "created_time": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "last_edited_time": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "has_children": {
                        "type": "boolean"
                    },
                    "archived": {
                        "type": "boolean"
                    },
                    "paragraph": {
                        "type": "object",
                        "properties": {
                            "rich_text": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "type": {
                                            "type": "string"
                                        },
                                        "text": {
                                            "type": "object",
                                            "properties": {
                                                "content": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": ["content"]
                                        }
                                    },
                                    "required": ["type", "text"]
                                }
                            }
                        },
                        "required": ["rich_text"]
                    }
                },
                "required": ["object", "id", "type", "created_time", "last_edited_time", "has_children", "archived"]
            }
        }
    },
    "required": ["object", "results"]
}
