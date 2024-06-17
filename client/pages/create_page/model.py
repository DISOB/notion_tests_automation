CREATE_PAGE_RESPONSE_SCHEMA = {
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
        "parent": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string"
                },
                "page_id": {
                    "type": "string",
                    "format": "uuid"
                }
            },
            "required": ["type", "page_id"]
        },
        "properties": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "type": {
                        "type": "string"
                    },
                    "title": {
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
                "required": ["id", "type", "title"]
            }
        },
        "url": {
            "type": "string",
            "format": "uri"
        }
    },
    "required": ["object", "id", "created_time", "last_edited_time", "parent", "properties", "url"]
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
