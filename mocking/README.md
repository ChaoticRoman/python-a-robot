This repository contains simple examples how to use Python 3 unittesting.

All example tests can be run by `python3 -m unittest discover .`


# Basic example of code with functionality and its unittest in one file

There is an example program to be tested, it can be run by `./test_foo.py`

and unittested by `python3 -m unittest test_foo.py`

# Mocking out opening, reading and writing of files

Mocking out opening, reading and writing files is relatively straightforward
in Python 3 for simple cases thanks to
[unittest.mock.mock_open](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.mock_open).
See [single_read.py](single_read.py), [test_single_read.py](test_single_read.py),
[single_write.py](single_write.py) and [test_single_write.py](test_single_write.py).

The stuff gets more complicated in case of several reads and writes to different
files in single routine. Here I got full testing of file name and content
accomplished using Mock's powerful
[side_effect](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect)
attribute. See [multiple_reads_and_writes.py](multiple_reads_and_writes.py) and
[test_multiple_reads_and_writes.py](test_multiple_reads_and_writes.py).
