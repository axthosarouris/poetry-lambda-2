from datetime import date

from assertpy import assert_that

from src import new_user_handler

EMPTY_CONTEXT = None


class NewUserHandlerTest:

    def should_return_username_and_time_of_creation(self):
        input = {"name": "Orestis"}
        actual_output= new_user_handler.handle_request(input, EMPTY_CONTEXT)
        currentDate = date.today()
        expected_output = {"name": "Orestis", "timestamp": str(currentDate)}
        assert_that(actual_output).is_equal_to(expected_output)
