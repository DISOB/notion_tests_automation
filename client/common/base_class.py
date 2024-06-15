import logging
import requests
import jsonschema

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.propagate = True


class RequestSender:
    def __init__(self) -> None:
        pass

    def send_request(self, method: str, url: str, **kwargs) -> requests.Response:
        try:
            response = requests.request(method, url, **kwargs)
            logger.info(self.format_message(response))
            return response
        except requests.exceptions.ConnectionError as e:
            logger.exception(f"ConnectionError: {e}")

    @staticmethod
    def format_message(response):
        return f"\n\n\n" \
               f"REQUEST METHOD: {response.request.method}\n" \
               f"REQUEST URL: {response.request.url}\n" \
               f"REQUEST HEADERS: {response.request.headers}\n" \
               f"REQUEST BODY: {response.request.body}\n\n" \
               f"RESPONSE STATUS CODE: {response.status_code}\n" \
               f"RESPONSE BODY: {response.text}\n"


class ResponseHandler:
    ASSERTIONERROR_STATUSCODE = "Status code | AssertionError: expected response to have status code {} but got {}"
    ASSERTIONERROR_RESPONSEBODYVALUE = "Response Body | AssertionError: expected response body to equal '{}' but got '{}'"
    ASSERTIONERROR_SETUP = "Setup | AssertionError: {}"
    ASSERTIONERROR_CHECK = "Check | AssertionError: {}"

    @classmethod
    def log_assert(cls, func, messages):
        if not func:
            logging.error(messages)
        assert func, messages

    @classmethod
    def verify_response_code(cls, expected, actual):
        cls.log_assert(actual == expected, cls.ASSERTIONERROR_STATUSCODE.format(expected, actual))

    @classmethod
    def verify_json_schema(cls, schema, response):
        def validate(schema, response):
            try:
                jsonschema.validate(instance=response, schema=schema)
            except jsonschema.exceptions.ValidationError as e:
                return False, e
            return True, "The response schema is correct"

        validate, message = validate(schema, response)
        assert validate, f"Schema Check | AssertionError: {message}"
