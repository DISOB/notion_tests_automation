import os

class Client:
    NOTION_API_TOKEN = os.getenv("NOTION_TOKEN")
    NOTION_API_BASE_URL = "https://api.notion.com"

    #Сомнительно, но окей
    DATABASE_ID = "c860cb8ca7bf4e7eaba9d22fb9c61a57"
    DATABASE_TO_UPDATE_ID = "d1a4e4084ddb499cab7d9496ede4855e"
    PARENT_PAGE_ID = "9a6a7be7edd349f588c9f066965d731c"
    PAGE_ID = "ad4c7a835a9c4b208c62fc6a54953051"
    PAGE_TO_UPDATE_ID = "d6f3fc9a49424ce09235c35ec97f1506"
    PROPERTY_ID = "title"
    BLOCK_ID = "5247382338cf487490245536cfcb22ec"

    #Константа для проверки, что test_get_comments действительно работает
    PAGE_WITHOUT_COMMENTS_ID = "e2fda964fe8f4d138062a7696f8b0f5f"

    # Maxim_Stoletov
    USER_ID = "4f2bb362-523d-4c44-b903-26d89eef6348"

