import unittest
from parameterized import parameterized
from merge_strings import merge


class MergeStringsTest(unittest.TestCase):

    @parameterized.expand([
        ('abc', 'stuvwx', 'asbtcuvwx'),
        ('stuvwx', 'abc', 'satbucvwx'),
        ('true', 'lies', 'tlriuees'),
        ('ma te ria l', ' de sign ', 'm ad et es irgina  l'),
        (' ch e ck', 'l is t', ' lc hi se  tck'),
        ('', '', ''),
        ('trial', '', 'trial'),
        ('', 'over', 'over'),
        (None, None, ''),
        ('game', None, 'game'),
        (None, 'plan', 'plan')
    ])
    def test_merge_strings(self, first_string, second_string, expected_result):
        self.longMessage = True
        actual = merge(first_string, second_string)
        message = 'For first-string {0}, second-string {1} expected result = {2}, and actual value = {3}'.format(
            first_string, second_string, expected_result, actual)
        self.assertEqual(expected_result, actual, message)
