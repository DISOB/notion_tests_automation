RESPONSE_SCHEMA = {
  "type": "object",
  "properties": {
      "results": {
      "type": "array",
      "items": [
          {
          "type": "object",
          "properties": {
              "object": {"type": "string"},
              "id": {"type": "string"},
              "type": {"type": "string"},
              "person": {
                  "type": "object",
                  "properties": {
                      "email": {"type": "string"}
                  },
                  "required": ["email"]
              },
              "name": {"type": "string"},
              "avatar_url": {"type": "string"}
              },
              "required": ["object", "id", "type", "person", "name", "avatar_url"]
          },
          {
              "type": "object",
              "properties": {
                  "object": {"type": "string"},
                  "id": {
                  "type": "string"
                },
                "type": {
                  "type": "string"
                },
                "bot": {
                  "type": "object"
                },
                "name": {
                  "type": "string"
                },
                "avatar_url": {
                  "type": "string"
                }
              },
              "required": [
                "object",
                "id",
                "type",
                "bot",
                "name",
                "avatar_url"
              ]
            }
      ]
    },
    "next_cursor": {
      "type": "string"
    },
    "has_more": {
      "type": "boolean"
    }
  },
  "required": [
    "results",
    "next_cursor",
    "has_more"
  ]
}
