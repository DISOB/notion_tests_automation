UPDATE_DATABASE_RESPONSE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "object": {
            "type": "string"
        },
        "id": {
            "type": "string",
            "format": "uuid"
        },
        "created_time": {
            "type": "string",
            "format": "date-time"
        },
        "last_edited_time": {
            "type": "string",
            "format": "date-time"
        },
        "created_by": {
            "type": "object",
            "properties": {
                "object": {
                    "type": "string"
                },
                "id": {
                    "type": "string",
                    "format": "uuid"
                }
            },
            "required": ["object", "id"]
        },
        "last_edited_by": {
            "type": "object",
            "properties": {
                "object": {
                    "type": "string"
                },
                "id": {
                    "type": "string",
                    "format": "uuid"
                }
            },
            "required": ["object", "id"]
        },
        "cover": {
            "type": ["null", "object"]
        },
        "icon": {
            "type": ["null", "object"]
        },
        "parent": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string"
                },
                "workspace": {
                    "type": "boolean"
                }
            },
            "required": ["type", "workspace"]
        },
        "archived": {
            "type": "boolean"
        },
        "in_trash": {
            "type": "boolean"
        },
        "properties": {
            "type": "object",
            "additionalProperties": True
        },
        "url": {
            "type": "string",
            "format": "uri"
        },
        "public_url": {
            "type": ["null", "string"]
        },
        "request_id": {
            "type": "string"
        }
    },
    "required": ["object", "id", "created_time", "last_edited_time", "created_by", "last_edited_by", "parent", "archived", "properties"]
}
