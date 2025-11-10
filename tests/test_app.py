import io
import unittest
from contextlib import redirect_stdout

from app import get_greeting, main


class GetGreetingTests(unittest.TestCase):
    def test_returns_expected_message(self) -> None:
        self.assertEqual(get_greeting(), "hello from codex demo")


class MainTests(unittest.TestCase):
    def test_main_shouts_when_flag_enabled(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            main(["--shout"])
        self.assertEqual(buffer.getvalue().strip(), "HELLO FROM CODEX DEMO")


if __name__ == "__main__":
    unittest.main()
