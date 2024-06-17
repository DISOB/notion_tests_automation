RETRIEVE_PAGE_PROPERTY_RESPONSE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "object": {
            "type": "string"
        },
        "results": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "object": {
                            "type": "string"
                        },
                        "type": {
                            "type": "string"
                        },
                        "id": {
                            "type": "string"
                        },
                        "title": {
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
                                        },
                                        "link": {
                                            "type": "null"
                                        }
                                    },
                                    "required": [
                                        "content",
                                        "link"
                                    ]
                                },
                                "annotations": {
                                    "type": "object",
                                    "properties": {
                                        "bold": {
                                            "type": "boolean"
                                        },
                                        "italic": {
                                            "type": "boolean"
                                        },
                                        "strikethrough": {
                                            "type": "boolean"
                                        },
                                        "underline": {
                                            "type": "boolean"
                                        },
                                        "code": {
                                            "type": "boolean"
                                        },
                                        "color": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "bold",
                                        "italic",
                                        "strikethrough",
                                        "underline",
                                        "code",
                                        "color"
                                    ]
                                },
                                "plain_text": {
                                    "type": "string"
                                },
                                "href": {
                                    "type": "null"
                                }
                            },
                            "required": [
                                "type",
                                "text",
                                "annotations",
                                "plain_text",
                                "href"
                            ]
                        }
                    },
                    "required": [
                        "object",
                        "type",
                        "id",
                        "title"
                    ]
                }
            ]
        },
        "next_cursor": {
            "type": "null"
        },
        "has_more": {
            "type": "boolean"
        },
        "type": {
            "type": "string"
        },
        "property_item": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string"
                },
                "next_url": {
                    "type": "null"
                },
                "type": {
                    "type": "string"
                },
                "title": {
                    "type": "object"
                }
            },
            "required": [
                "id",
                "next_url",
                "type",
                "title"
            ]
        },
        "request_id": {
            "type": "string"
        }
    },
    "required": [
        "object",
        "results",
        "next_cursor",
        "has_more",
        "type",
        "property_item",
        "request_id"
    ]
}


RETRIEVE_PAGE_PROPERTY_RESPONSE_SCHEMA_401 = {
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
