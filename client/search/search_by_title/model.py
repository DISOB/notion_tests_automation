RESPONSE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "object": {"type": "string"},
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "object": {"type": "string"},
                    "id": {"type": "string"},
                    "created_time": {"type": "string"},
                    "last_edited_time": {"type": "string"},
                    "created_by": {
                        "type": "object",
                        "properties": {
                            "object": {"type": "string"},
                            "id": {"type": "string"}
                        },
                        "required": ["object", "id"]
                    },
                    "parent": {
                        "type": "object",
                        "properties": {
                            "type": {"type": "string"},
                            "page_id": {"type": "string"},
                            "database_id": {"type": "string"}
                        },
                        "required": ["type"]
                    },
                    "properties": {"type": "object"},
                    "url": {"type": "string"}
                },
                "required": ["object", "id", "created_time", "last_edited_time", "created_by", "parent", "properties", "url"]
            }
        },
        "next_cursor": {"type": ["null", "string"]},
        "has_more": {"type": "boolean"}
    },
    "required": ["object", "results", "has_more"]
}


RESPONSE_SCHEMA_401 = {
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
