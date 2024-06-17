QUERY_RESPONSE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
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
                    # ------------------
                },
                "required": ["object", "id"]
            }
        },
        "next_cursor": {"type": ["null", "string"]},
        "has_more": {"type": "boolean"},
        "type": {"type": "string"},
        "page_or_database": {"type": "object"},
        "request_id": {"type": "string"}
    },
    "required": ["object", "results", "next_cursor", "has_more", "type", "page_or_database", "request_id"]
}


QUERY_RESPONSE_SCHEMA_401 = {
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