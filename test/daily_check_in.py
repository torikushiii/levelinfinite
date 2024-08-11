# test_check_in.py
import unittest
import requests
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unittest.mock import patch, MagicMock
from modules.check_in import daily_check_in

class TestDailyCheckIn(unittest.TestCase):

    @patch('requests.post')
    def test_daily_check_in_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {'code': 0, 'msg': 'ok'}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        with patch('builtins.print') as mock_print:
            daily_check_in()
            mock_print.assert_called_with("Check-in successful!")

    @patch('requests.post')
    def test_daily_check_in_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {'code': 1001009, 'msg': 'Some error message'}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        with patch('builtins.print') as mock_print:
            daily_check_in()
            mock_print.assert_called_with("Check-in failed: Some error message")

    @patch('requests.post')
    def test_daily_check_in_unexpected_response(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {'code': 12345, 'msg': 'unexpected'}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        with patch('builtins.print') as mock_print:
            daily_check_in()
            mock_print.assert_called_with("Unexpected response: {'code': 12345, 'msg': 'unexpected'}")

    @patch('requests.post')
    def test_daily_check_in_request_exception(self, mock_post):
        mock_post.side_effect = requests.exceptions.RequestException("Network error")

        with patch('builtins.print') as mock_print:
            daily_check_in()
            mock_print.assert_called_with("Check-in failed: Network error")

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
from main import main

class TestMain(unittest.TestCase):

    @patch('schedule.every')
    @patch('builtins.print')
    def test_main(self, mock_print, mock_schedule_every):
        mock_schedule = MagicMock()
        mock_schedule.every.return_value.day.at.return_value.do = MagicMock()
        mock_schedule_every.return_value = mock_schedule

        with patch('time.sleep', return_value=None):
            with self.assertRaises(KeyboardInterrupt):
                main()

        mock_print.assert_any_call("Script started...")
        mock_print.assert_any_call("Scheduled daily check-in at 09:00 AM")

if __name__ == '__main__':
    unittest.main()
