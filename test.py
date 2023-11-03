import unittest
from unittest import TestCase
from parameterized.parameterized import parameterized
from io import StringIO
from unittest.mock import patch
from typing import Literal

from main import print_file_contents

# initialize data for unittesting
SMALL = ''
with open('test_files/small.txt', 'r', encoding='utf-8') as f:
    SMALL = f.read()

HELLO = ''
with open('test_files/hello.txt', 'r', encoding='utf-8') as f:
    HELLO = f.read()

WALRUS = ''
with open('test_files/walrus.txt', 'r', encoding='utf-8') as f:
    WALRUS = f.read()

LARGE = ''
with open('test_files/large.txt', 'r', encoding='utf-8') as f:
    LARGE = f.read()


class TestPyHead(TestCase):
    """Test py-head functionality."""

    @parameterized.expand(
        [
            ['lines', 100, 'test_files/walrus.txt', WALRUS],
            ['lines', 1, 'test_files/walrus.txt', WALRUS[:38]],
            ['lines', 2, 'test_files/walrus.txt', WALRUS[:39]],
            ['lines', 3, 'test_files/walrus.txt', WALRUS[:40]],
            ['lines', None, 'test_files/walrus.txt', WALRUS],
            ['lines', 1, 'test_files/hello.txt', HELLO],
            ['lines', 10, 'test_files/hello.txt', HELLO],
            ['lines', 15, 'test_files/hello.txt', HELLO],
            ['lines', 100, 'test_files/hello.txt', HELLO],
            ['lines', None, 'test_files/hello.txt', HELLO],
            ['lines', 1, 'test_files/small.txt', SMALL[:46]],
            ['lines', 10, 'test_files/small.txt', SMALL],
            ['lines', 100, 'test_files/small.txt', SMALL],
            ['lines', None, 'test_files/small.txt', SMALL],
            ['lines', None, 'test_files/large.txt', LARGE],
            ['lines', 10000, 'test_files/large.txt', LARGE],
            ['lines', 100000, 'test_files/large.txt', LARGE],
            ['lines', 1, 'test_files/large.txt', LARGE[:46]],
        ]
    )
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_lines_from_file(
        self,
        kind: Literal["lines", "bytes"],
        N: int | None,
        filename: str,
        expected_output: str,
        mock_stdout
    ) -> None:
        print_file_contents(kind=kind, N=N, filename=filename)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @parameterized.expand(
        [
            ['bytes', 100, 'test_files/walrus.txt', WALRUS],
            ['bytes', 1, 'test_files/walrus.txt', WALRUS[:1]],
            ['bytes', 2, 'test_files/walrus.txt', WALRUS[:2]],
            ['bytes', 3, 'test_files/walrus.txt', WALRUS[:3]],
            ['bytes', 1, 'test_files/hello.txt', HELLO[:1]],
            ['bytes', 10, 'test_files/hello.txt', HELLO[:10]],
            ['bytes', 15, 'test_files/hello.txt', HELLO],
            ['bytes', 100, 'test_files/hello.txt', HELLO],
            ['bytes', 1, 'test_files/small.txt', SMALL[:1]],
            ['bytes', 2, 'test_files/small.txt', SMALL[:2]],
            ['bytes', 3, 'test_files/small.txt', SMALL[:3]],
            ['bytes', 10, 'test_files/small.txt', SMALL[:10]],
            ['bytes', 1, 'test_files/large.txt', LARGE[:1]],
            ['bytes', 2, 'test_files/large.txt', LARGE[:2]],
            ['bytes', 3, 'test_files/large.txt', LARGE[:3]],
        ]
    )
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_bytes_from_file(
        self,
        kind: Literal["lines", "bytes"],
        N: int | None,
        filename: str,
        expected_output: str,
        mock_stdout
    ) -> None:
        print_file_contents(kind=kind, N=N, filename=filename)
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
