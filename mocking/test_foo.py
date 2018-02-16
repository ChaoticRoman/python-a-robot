#!/usr/bin/python3
"""Simple exercise in unittest and its mock."""
import time
import unittest
from unittest.mock import patch


class MyCoolCustomError(Exception):
    pass


def my_print(x):
    print(x)


def f(num2):
    print(num2, "is not contained!")
    return(0)


# Function we want to test:
def chatty_function_which_takes_a_lot_of_time(num1, num2):
    print("hello!")
    if num1 < 0 or num2 < 0:
        raise MyCoolCustomError("num1 and num2 must be bigger then 0.")

    for i in range(num1, num2):
        time.sleep(2)
        my_print(i)
    return(f(num2))


# Our test case containing two tests follows.
# NOTE: When tested function(s) is in different file use name of that file
#       instead of test_foo
class TestFoo(unittest.TestCase):

    # First test to check basic functionality of tested function
    # NOTE: Notice that mocks are passed to arguments in opposite order
    #       then they are patched
    @patch("test_foo.print")
    @patch("test_foo.f")
    @patch("test_foo.my_print")
    @patch("test_foo.time.sleep")
    def test_foo_patch(self, mock_sleep, mock_my_print, mock_f, mock_print):

        # We dont want real f to be called, but we want to fake
        # f returning value
        mock_f.return_value = 1

        # Getting output of main function. Because sleep and my_print
        # are mocked, function wont take so much time and wont print anything
        result = chatty_function_which_takes_a_lot_of_time(1, 3)

        # This would print nothing because print is mocked out.
        # Often is better to separate your test code and code under the test.
        print('Hello from test.')

        # Testing if result is equal to expected output (in this case 1)
        self.assertEqual(result, 1)

        # Testing if f was called just once with this parameter
        mock_f.assert_called_once_with(3)

        # Testing if mocked my_print was called twice
        assert mock_my_print.call_count == 2
        # or
        self.assertEqual(mock_my_print.call_count, 2)

        # Testing if my_print was called with these arguments
        assert mock_my_print.call_args_list == [((1,),), ((2,),)]
        # NOTE: every call is tuple of tuple or tuple of tuple and dictionary.
        #       Inner tuple contains positional arguments and dictionary
        #       may contain keyword arguments. In this example there
        #       are two calls of one positional argument and none keyword
        #       argument (= two tuples of tuple).
        #
        #       Example calls and their call_args_list:
        #       f1()                   ->    [((),)]
        #       f2(1), f2(None)        ->    [((1,),), ((None,),)]
        #       f3(1, 2), f3(10, 20)   ->    [((1, 2),), ((10, 20),)]
        #       f4(a=5), f4(b=5)       ->    [((), {'a': 5}), ((), {'b': 5})]
        #       f5(1, 2, a=5)          ->    [((1, 2), {'a': 5})]

    # Second test to check if your custom error is thrown
    @patch("test_foo.print")
    @patch("test_foo.f")
    @patch("test_foo.my_print")
    @patch("test_foo.time.sleep")
    def test_custom_exception(self, mock_sleep, mock_my_print, mock_f, mock_print):
        # NOTE: When error is defined in a different file use:
        #       file.MyCoolCustomError
        with self.assertRaises(MyCoolCustomError):
            chatty_function_which_takes_a_lot_of_time(-5, -1)

if __name__ == "__main__":
    chatty_function_which_takes_a_lot_of_time(1, 3)
