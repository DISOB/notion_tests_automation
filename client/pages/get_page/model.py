GET_PAGE_RESPONSE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "object": {"type": "string"},
        "id": {"type": "string", "format": "uuid"},
        "created_time": {"type": "string", "format": "date-time"},
        "last_edited_time": {"type": "string", "format": "date-time"},
        "cover": {
            "type": ["null", "object"],
            "properties": {
                "type": {"type": "string"},
                "external": {
                    "type": "object",
                    "properties": {
                        "url": {"type": "string", "format": "uri"}
                    },
                    "required": ["url"]
                }
            },
            "required": ["type", "external"]
        },
        "icon": {
            "type": ["null", "object"],
            "properties": {
                "type": {"type": "string"},
                "emoji": {"type": "string"}
            },
            "required": ["type", "emoji"]
        },
        "parent": {
            "type": "object",
            "properties": {
                "type": {"type": "string"},
                "page_id": {"type": "string", "format": "uuid"},
                "workspace": {"type": "boolean"}
            },
            "required": ["type"],
            "oneOf": [
                {"required": ["page_id"]},
                {"required": ["workspace"]}
            ]
        },
        "archived": {"type": "boolean"},
        "properties": {
            "type": "object",
            "additionalProperties": {"type": "object"}
        },
        "url": {"type": "string", "format": "uri"}
    },
    "required": ["object", "id", "created_time", "last_edited_time", "parent", "archived", "properties", "url"]
}


GET_PAGE_RESPONSE_SCHEMA_401_404 = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "object": {
      "type": "string"
    },
    "status": {
      "type": "integer"
    },
    "code": {
      "type": "string"
    },
    "message": {
      "type": "string"
    },
    "request_id": {
      "type": "string"
    }
  },
  "required": [
    "object",
    "status",
    "code",
    "message",
    "request_id"
  ]
}