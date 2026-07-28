import unittest 
from main import Strint

class TestStrint(unittest.TestCase):
    def test_len(self):
        self.assertEqual(len(Strint(541)), 3, '\nطول Strint(541) برابر ۳ می‌باشد.')
        self.assertEqual(len(Strint(5)), 1, '\nطول Strint(5) برابر ۱ می‌باشد.')

    def test_call(self):
        number = Strint(8132495706)
        self.assertEqual(number(), '۸۱۳۲۴۹۵۷۰۶', '\nبا فراخوانی Strint(8132495706) کاراکترهای فارسی آن که برابر ۸۱۳۲۴۹۵۷۰۶ است برگردانده می‌شود.')

    def test_inheritance(self):
        self.assertTrue(issubclass(Strint, int), '\nکلاس Strint باید از کلاس int ارث‌بری کرده باشد.')

    def test_lt(self):
        self.assertTrue(Strint(1593) < Strint(14), '\nStrint(14) بزرگتر از Strint(1593) می‌باشد.')
        self.assertFalse(Strint(984) < Strint(4), '\nStrint(4) بزرگتر از Strint(984) می‌باشد.')