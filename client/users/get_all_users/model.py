RESPONSE_SCHEMA = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "object": {"type": "string"},
    "results": {
      "type": "array",
      "items": {
        "oneOf": [
          {
            "type": "object",
            "properties": {
              "object": {"type": "string"},
              "id": {"type": "string"},
              "name": {"type": "string"},
              "avatar_url": {"type": ["string", "null"]},
              "type": {"type": "string"},
              "person": {"type": "object"}
            },
            "required": ["object", "id", "name", "type", "person"]
          },
          {
            "type": "object",
            "properties": {
              "object": {"type": "string"},
              "id": {"type": "string"},
              "name": {"type": "string"},
              "avatar_url": {"type": ["string", "null"]},
              "type": {"type": "string"},
              "bot": {
                "type": "object",
                "properties": {
                  "owner": {
                    "type": "object",
                    "properties": {
                      "type": {"type": "string"},
                      "workspace": {"type": "boolean"}
                    },
                    "required": ["type", "workspace"]
                  },
                  "workspace_name": {"type": "string"}
                },
                "required": ["owner"]
              }
            },
            "required": ["object", "id", "name", "type", "bot"]
          }
        ]
      }
    },
    "next_cursor": {"type": ["string", "null"]},
    "has_more": {"type": "boolean"},
    "type": {"type": "string"},
    "user": {"type": "object"},
    "request_id": {"type": "string"}
  },
  "required": ["object", "results", "next_cursor", "has_more", "type", "request_id"]
}
