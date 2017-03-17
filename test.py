import unittest
from unittest import TestCase
from unittest.mock import patch, call

import game

class TestGuessingGame(TestCase):


    @patch('builtins.input', side_effect=[1,5,3])
    def test_get_guess_valid(self, mock_input):

        self.assertEqual(1, game.get_guess())
        self.assertEqual(5, game.get_guess())
        self.assertEqual(3, game.get_guess())


    # Test that the user input validator rejects non-numeric input
    @patch('builtins.input', side_effect=['pizza','   ','sdfs234',3])
    def test_get_guess_invalid(self, mock_input):
        # Assert all the invalid inputs are ignored.
        self.assertEqual(3, game.get_guess())


    # Does compare correctly determine if a number is higher or lower than another?
    def test_compare_guess_to_secret(self):
        self.assertEqual(game.correct, game.compare(5, 5))
        self.assertEqual(game.high, game.compare(5, 7))
        self.assertEqual(game.low, game.compare(5, 3))


    @patch('game.make_secret_number', side_effect=[4])
    @patch('builtins.input', side_effect=[0,10,5,3,4]) # Too low, too high, too high, too low, just right
    @patch('builtins.print')
    def test_game(self, mock_print, mock_input, mock_secret):
        game.main()

        expected_print = [ game.low, game.high, game.high, game.low, game.correct];
        calls = [ call(out) for out in expected_print ]

        # Examine the calls made to mock_print and assert they are as expected

        mock_print.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()
