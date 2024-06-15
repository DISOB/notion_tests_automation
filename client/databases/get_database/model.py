RESPONSE_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "object": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "cover": {
      "type": "null"
    },
    "icon": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "external": {
          "type": "object",
          "properties": {
            "url": {
              "type": "string"
            }
          },
          "required": [
            "url"
          ]
        }
      },
      "required": [
        "type",
        "external"
      ]
    },
    "created_time": {
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
    "last_edited_time": {
      "type": "string"
    },
    "title": {
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
    "description": {
      "type": "array",
      "items": {}
    },
    "is_inline": {
      "type": "boolean"
    },
    "properties": {
      "type": "object",
      "properties": {
        "Task name": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "name": {
              "type": "string"
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
            "name",
            "type",
            "title"
          ]
        },
        "Assignee": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "people": {
              "type": "object"
            }
          },
          "required": [
            "id",
            "name",
            "type",
            "people"
          ]
        },
        "Status": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "status": {
              "type": "object",
              "properties": {
                "options": {
                  "type": "array",
                  "items": [
                    {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "color": {
                          "type": "string"
                        },
                        "description": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "id",
                        "name",
                        "color",
                        "description"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "color": {
                          "type": "string"
                        },
                        "description": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "id",
                        "name",
                        "color",
                        "description"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "color": {
                          "type": "string"
                        },
                        "description": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "id",
                        "name",
                        "color",
                        "description"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "color": {
                          "type": "string"
                        },
                        "description": {
                          "type": "null"
                        }
                      },
                      "required": [
                        "id",
                        "name",
                        "color",
                        "description"
                      ]
                    }
                  ]
                },
                "groups": {
                  "type": "array",
                  "items": [
                    {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "color": {
                          "type": "string"
                        },
                        "option_ids": {
                          "type": "array",
                          "items": [
                            {
                              "type": "string"
                            }
                          ]
                        }
                      },
                      "required": [
                        "id",
                        "name",
                        "color",
                        "option_ids"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "color": {
                          "type": "string"
                        },
                        "option_ids": {
                          "type": "array",
                          "items": [
                            {
                              "type": "string"
                            }
                          ]
                        }
                      },
                      "required": [
                        "id",
                        "name",
                        "color",
                        "option_ids"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "color": {
                          "type": "string"
                        },
                        "option_ids": {
                          "type": "array",
                          "items": [
                            {
                              "type": "string"
                            },
                            {
                              "type": "string"
                            }
                          ]
                        }
                      },
                      "required": [
                        "id",
                        "name",
                        "color",
                        "option_ids"
                      ]
                    }
                  ]
                }
              },
              "required": [
                "options",
                "groups"
              ]
            }
          },
          "required": [
            "id",
            "name",
            "type",
            "status"
          ]
        },
        "Due": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "date": {
              "type": "object"
            }
          },
          "required": [
            "id",
            "name",
            "type",
            "date"
          ]
        },
        "Summary": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "rich_text": {
              "type": "object"
            }
          },
          "required": [
            "id",
            "name",
            "type",
            "rich_text"
          ]
        }
      },
      "required": [
        "Task name",
        "Assignee",
        "Status",
        "Due",
        "Summary"
      ]
    },
    "parent": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "workspace": {
          "type": "boolean"
        }
      },
      "required": [
        "type",
        "workspace"
      ]
    },
    "url": {
      "type": "string"
    },
    "public_url": {
      "type": "null"
    },
    "archived": {
      "type": "boolean"
    },
    "in_trash": {
      "type": "boolean"
    },
    "request_id": {
      "type": "string"
    }
  },
  "required": [
    "object",
    "id",
    "cover",
    "icon",
    "created_time",
    "created_by",
    "last_edited_by",
    "last_edited_time",
    "title",
    "description",
    "is_inline",
    "properties",
    "parent",
    "url",
    "public_url",
    "archived",
    "in_trash",
    "request_id"
  ]
}