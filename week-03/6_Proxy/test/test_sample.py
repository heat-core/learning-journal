import unittest

from main import Proxy


class Hi:
    def __init__(self):
        self.number = 0

    def f1(self):
        pass

    def f2(self):
        pass


class Test(unittest.TestCase):
    def test_sample_1(self):
        str_proxy = Proxy("test_string")
        self.assertTrue(isinstance(str_proxy, Proxy), 'نام کلاس موردنظر باید Proxy باشد.')
        t = Hi()
        proxy = Proxy(t)
        proxy.number = 6
        self.assertTrue(6, t.number)

    def test_sample_2(self):
        proxy = Proxy("Test String")
        proxy.upper()
        self.assertEqual("upper", proxy.last_accessed_attribute())
        try:
            proxy.no_such_method()
            self.assertFalse(True)
        except Exception as e:
            self.assertEqual("No such attribute.", str(e), 'تابع موردنظر جزو توابع تعریف‌شده نیست؛ پس باید استثنایی با پیغام No such attribute. پرتاب شود.')

        self.assertEqual(1, proxy.count_of_accesses("upper"), 'متد upper تاکنون ۱ بار روی شیء موردنظر فراخوانی شده‌است.')
        self.assertEqual(0, proxy.count_of_accesses("capitalize"), 'متد capitalize تاکنون روی شیء موردنظر فراخوانی نشده‌است.')

    def test_sample_3(self):
        proxy = Proxy(Hi())
        proxy.f1()
        self.assertTrue(proxy.was_accessed("f1"), 'متد f1 روی شیء موردنظر فراخوانی شده‌است.')
        self.assertFalse(proxy.was_accessed("f2"), 'متد f2 روی شیء موردنظر فراخوانی نشده‌است.')
        proxy.f2()
        self.assertTrue(proxy.was_accessed("f2"), 'متد f2 روی شیء موردنظر فراخوانی شده‌است.')
        self.assertFalse(proxy.was_accessed("not valid"), 'متد not valid روی شیء موردنظر فراخوانی نشده‌است.')

    def test_sample_4(self):
        t = Hi()
        proxy = Proxy(t)

        try:
            proxy.last_accessed_attribute()
        except Exception as e:
            self.assertEqual("No attribute was accessed.", str(e), 'تابه‌حال متد معتبری فراخوانی نشده، پس باید استثنایی با پیغام No Method Is Invoked پرتاب شود.')

        proxy.f1()
        proxy.f2()
        self.assertEqual("f2", proxy.last_accessed_attribute(), 'آخرین متد معتبری که فراخوانی شده، f2 است.')
