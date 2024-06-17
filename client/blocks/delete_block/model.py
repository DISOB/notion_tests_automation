DELETE_BLOCK_RESPONSE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "object": {
            "type": "string"
        },
        "id": {
            "type": "string"
        },
        "parent": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string"
                },
                "page_id": {
                    "type": "string"
                }
            },
            "required": [
                "type",
                "page_id"
            ]
        },
        "created_time": {
            "type": "string"
        },
        "last_edited_time": {
            "type": "string"
        },
        "created_by": {
            "type": "object",
            "properties": {
                "object": {
                    "type": "string"
                },
                "id": {
                    "type": "string"
                }
            },
            "required": [
                "object",
                "id"
            ]
        },
        "last_edited_by": {
            "type": "object",
            "properties": {
                "object": {
                    "type": "string"
                },
                "id": {
                    "type": "string"
                }
            },
            "required": [
                "object",
                "id"
            ]
        },
        "has_children": {
            "type": "boolean"
        },
        "archived": {
            "type": "boolean"
        },
        "in_trash": {
            "type": "boolean"
        },
        "type": {
            "type": "string"
        },
        "paragraph": {
            "type": "object",
            "properties": {
                "rich_text": {
                    "type": "array",
                    "items": [
                        {
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
                    ]
                },
                "color": {
                    "type": "string"
                }
            },
            "required": [
                "rich_text",
                "color"
            ]
        },
        "request_id": {
            "type": "string"
        }
    },
    "required": [
        "object",
        "id",
        "parent",
        "created_time",
        "last_edited_time",
        "created_by",
        "last_edited_by",
        "has_children",
        "archived",
        "in_trash",
        "type",
        "paragraph",
        "request_id"
    ]
}


DELETE_BLOCK_RESPONSE_SCHEMA_401 = {
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