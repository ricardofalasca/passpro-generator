from unittest import TestCase
from passpro import PasswordPronounceable


class PasswordGenerateTestCase(TestCase):
    def setUp(self):
        self._min = 5
        self._max = 15

    def test_password_generate(self):
        _quantity = 1000

        # initialize an instance
        pp = PasswordPronounceable()
        
        pwds = [pp.generate(self._min, self._max) for _ in range(0, _quantity)]

        self.assertEqual(len(pwds), _quantity)
        [self.assertTrue(all([len(p) >= self._min, len(p) <= self._max]))
         for p in pwds]
