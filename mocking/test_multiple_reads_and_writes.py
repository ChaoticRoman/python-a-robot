from unittest import TestCase, main
from unittest.mock import patch, mock_open

from multiple_reads_and_writes import f


class TestMultipleReadsAndWrites(TestCase):

    def test_multiple_reads_and_writes(self):
        # Prepare mock with multiple read data
        fake_open = mock_open()
        fake_open.return_value.read.side_effect = ['abc', 'def']

        # Patch and test
        with patch('multiple_reads_and_writes.open', fake_open):
            result = f()

        # Check your assertions
        assert fake_open.call_args_list == [
            (('test', 'w'), ),
            (('test2', 'w'), ),
            (('test', ), ),
            (('test2', ), )
        ]
        assert fake_open.return_value.write.call_args_list == [
            (('abc', ), ),
            (('def', ), ),
        ]
        assert result == 'abcdef'


if __name__ == "__main__":
    main()
