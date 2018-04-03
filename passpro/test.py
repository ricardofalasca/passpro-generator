from unittest import TestCase
from passpro import PasswordPronounceable


class PasswordGenerateTestCase(TestCase):
    def setUp(self):
        self._min = 5
        self._max = 15

    def test_as_instance(self):
        _quantity = 1000

        # initialize an instance
        pp = PasswordPronounceable()
        
        pwds = [pp.generate(self._min, self._max) for _ in range(0, _quantity)]

        self.assertEqual(len(pwds), _quantity)
        [self.assertTrue(all([len(p) >= self._min, len(p) <= self._max]))
         for p in pwds]

    def test_as_class_method(self):
        pwd = PasswordPronounceable.new(self._min, self._max)

        self.assertIsNotNone(pwd)
        self.assertTrue(all([len(pwd) >= self._min, len(pwd) <= self._max]))
