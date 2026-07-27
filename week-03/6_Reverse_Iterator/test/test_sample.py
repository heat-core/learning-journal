import unittest

from main import Reverse


class ScoreListTest(unittest.TestCase):

    def _test_ls(self, ls):
        tmp = list(ls)
        out = []
        for it in Reverse(ls):
            out.append(it)
        out.reverse()
        for a, b in zip(tmp, out):
            self.assertEqual(a, b)
        self.assertEqual(len(tmp), len(out), '\nطول لیست ورودی و خروجی با هم برابر نیست.')
        for a, b in zip(tmp, ls):
            self.assertEqual(a, b)

    def test_1(self):
        ls = [1, 2, 3, 4, 5]
        out = []
        for it in Reverse(ls):
            out.append(it)

        self.assertEqual(out, [5, 4, 3, 2, 1], '\nکلاس Reverse تکمیل شده توسط شما باید لیست [1, 2, 3, 4, 5] را به صورت [5, 4, 3, 2, 1] خروجی دهد.')

    def test_2(self):
        ls = ['mano', 'ali', 'ye', 'teamim']

        out = []
        for it in Reverse(ls):
            out.append(it)

        self.assertEqual(out, ['teamim', 'ye', 'ali', 'mano'], "\nکلاس Reverse تکمیل شده توسط شما باید لیست ['mano', 'ali', 'ye', 'teamim'] را به صورت ['teamim', 'ye', 'ali', 'mano'] خروجی دهد.")
