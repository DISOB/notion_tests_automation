CREATE_RESPONSE_SCHEMA = {
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
                    "plain_text": {"type": "string"}
                },
                "required": ["type", "text", "plain_text"]
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
        "url": {"type": "string", "format": "uri"}
    },
    "required": ["object", "id", "created_time", "last_edited_time", "title", "properties", "parent", "url"]
}


CREATE_PAGE_RESPONSE_SCHEMA_400_401_404 = {
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