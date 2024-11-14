from unittest import TestCase
from parse_session import get_interval_diff, get_intervals, get_session, get_total_time


class TestParser(TestCase):
    def test_get_session(self):
        assert get_session(session_file="session_data.txt") == 8

    def test_get_intervals(self):
        assert get_intervals(session_file="session_data.txt") == [
            ["06:15", "06:42"],
            ["06:17", "06:36"],
            ["06:36", "06:55"],
            ["06:55", "07:08"],
            ["06:54", "07:32"],
            ["07:33", "07:43"],
            ["20:00", "20:16"],
            ["20:20", "21:04"],
        ], get_intervals(session_file="session_data.txt")

    def test_get_interval_diff(self):
        assert get_interval_diff(["06:15", "06:42"]) == 27, get_interval_diff(
            ["06:15", "06:42"]
        )

    def test_get_total_time(self):
        assert get_total_time("session_data.txt") == 186.0, get_total_time(
            "session_data.txt"
        )
