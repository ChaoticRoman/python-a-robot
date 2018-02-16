from unittest import TestCase, main
from unittest.mock import patch, mock_open

from single_read import single_read


class TestSingleRead(TestCase):

    def test_single_read(self):
        # prepare mock and save reference to it
        fake_open = mock_open(read_data='test_data')

        # patch and test
        with patch('single_read.open', fake_open):
            result = single_read()

        # check assertions
        fake_open.assert_called_once_with('test')
        fake_open.return_value.read.assert_called_once_with()
        self.assertEqual(result, 'test_data')

if __name__ == "__main__":
    main()
