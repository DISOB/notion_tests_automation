RESPONSE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "object": {"type": "string"},
        "id": {"type": "string"},
        "created_time": {"type": "string"},
        "last_edited_time": {"type": "string"},
        "has_children": {"type": "boolean"},
        "type": {"type": "string"},
        "archived": {"type": "boolean"}
    },
    "required": ["object", "id", "created_time", "last_edited_time", "has_children", "type", "archived"]
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