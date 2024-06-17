GET_USER_RESPONSE_SCHEMA = {
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
        "person": {
            "type": "object",
            "properties": {
                "email": {
                    "type": ["string", "null"],
                    "format": "email"
                }
            },
            "required": []
        },
        "name": {
            "type": "string"
        },
        "avatar_url": {
            "type": ["string", "null"],
            "format": "uri"
        }
    },
    "required": ["object", "id", "type", "name"]
}


GET_USER_RESPONSE_SCHEMA_401_404 = {
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