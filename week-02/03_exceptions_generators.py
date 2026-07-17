فایل جدید بساز: week-02/03_exceptions_generators.py
بخش اول — Exception Handling:
یه تابع بنویس به اسم divide_numbers(a, b) که:

دو عدد می‌گیره و a / b رو برمی‌گردونه
اگه b صفر بود، به‌جای کرش کردن، یه پیام خطای مشخص چاپ کنه (با try/except) و None برگردونه
تایپ‌هینت هم داشته باشه: def divide_numbers(a: float, b: float) -> float | None:

بخش دوم — Generator:
یه تابع generator بنویس به اسم count_up_to(n) که:

از عدد ۱ تا n رو یکی‌یکی با yield برمی‌گردونه (نه با return یه لیست کامل)
تو if __name__ == "__main__": با یه حلقه for روش iterate کن و چاپش کن