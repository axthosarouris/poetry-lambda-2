from assertpy import assert_that

from src import handler

EMPTY_CONTEXT = None
EMPTY_BODY = None


class HandlerTest:

    def should_return_hello(self):
        response=handler.handle_request(EMPTY_BODY, EMPTY_CONTEXT)
        assert_that(response).is_equal_to("hello world 2")
