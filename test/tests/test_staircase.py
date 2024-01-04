from staircase.staircase import get_staircase
import unittest


class StaircaseTest(unittest.TestCase):
    def test_give_2_h_should_be_hh(self):
        n = 2
        pattern = "#"
        expected_output = " #\n" + "##"

        result = get_staircase(n, pattern)

        self.assertEqual(result, expected_output, f"Shoule be {expected_output}")
