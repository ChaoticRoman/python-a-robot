from unittest import TestCase, main
from unittest.mock import patch, mock_open

from single_write import single_write


class TestSingleWrite(TestCase):

    def test_single_write(self):
        # prepare mock and save reference to it
        fake_open = mock_open()

        # patch and test
        with patch('single_write.open', fake_open):
            single_write()

        # check assertions
        fake_open.assert_called_once_with('test', 'w')
        fake_open.return_value.write.assert_called_once_with('abc')


if __name__ == "__main__":
    main()
