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


class NameFlagTests(unittest.TestCase):
    def test_main_prints_name_when_provided(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            main(["--name", "James"])
        self.assertEqual(buffer.getvalue().strip(), "hello from codex demo, James")

    def test_main_shout_with_name(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            main(["--name", "James", "--shout"])
        self.assertEqual(buffer.getvalue().strip(), "HELLO FROM CODEX DEMO, JAMES")


class VersionFlagTests(unittest.TestCase):
    def test_main_prints_version_and_exits(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer), self.assertRaises(SystemExit) as exit_ctx:
            main(["--version"])
        self.assertEqual(buffer.getvalue().strip(), "v0.1.0")
        self.assertEqual(exit_ctx.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
