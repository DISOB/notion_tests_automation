RETRIEVE_BOT_USER_RESPONSE_SCHEMA = {
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
        "type": {
            "type": "string"
        },
        "bot": {
            "type": "object",
            "properties": {
                "owner": {
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
                }
            },
            "required": ["owner"]
        },
        "name": {
            "type": "string"
        },
        "avatar_url": {
            "type": ["string", "null"],
            "format": "uri"
        }
    },
    "required": ["object", "id", "type", "bot", "name"]
}
