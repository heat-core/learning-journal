# ارزیاب تسلط مراحل هوش مصنوعی (AI Mastery Stage Evaluator)
### موتور اعتبارسنجی عملی، آزمون‌های تحلیلی و شواهد پیشرفت ۲۴ ماهه

این نرم‌افزار به صورت اختصاصی برای همراهی با نقشه راه ۲۴ ماهه طراحی شده است تا پس از پایان هر مبحث و تمرین، بتوانید **شواهد واقعی تسلط (Proof of Mastery)** خود را اعتبارسنجی کنید.

---

## 🚀 دو حالت اجرایی برنامه (Dual Execution Modes)

### ۱. محیط داشبورد تعاملی وب (Web Interactive Mode)
فایل `index.html` را مستقیماً با دوبار کلیک در مرورگر باز کنید، یا یک وب‌سرور سبک لوکال اجرا نمایید:

```powershell
# اجرای سرور محلی وب
cd C:\Users\Dororo\GitHub\learning-journal\stage-evaluator
python -m http.server 8090
```
سپس در مرورگر خود آدرس `http://localhost:8090` را باز کنید.

**امکانات داشبورد وب:**
- **آزمون‌های تحلیلی و تستی:** سناریوهای واقعی و تست تصمیم‌گیری‌های معماری همراه با تصحیح آنی و تحلیل فارسی پاسخ‌ها.
- **چالش‌های کدنویسی:** بررسی منطق و تست‌های خودکار هر مرحله.
- **چک‌لیست شواهد و گواه (Evidence):** ذخیره پیشرفت و تیک زدن خروجی‌های واقعی در مرورگر (`localStorage`).
- **صدور کارنامه و گواهینامه دیجیتال:** تولید گزارش‌های رسمی با فرمت Markdown و JSON جهت ثبت در ژورنال یادگیری.

---

### ۲. تست‌رنر خط فرمان پایتون (Python CLI Test Runner)
برای تست واقعی کدهای پایتونی خود در ترمینال، دستورهای زیر را اجرا کنید:

```powershell
cd C:\Users\Dororo\GitHub\learning-journal\stage-evaluator

# مشاهده کارنامه و جدول وضعیت تسلط مراحل
python evaluator.py --status

# ارزیابی یک مرحله خاص (مثلاً مرحله ۰ یا ۱)
python evaluator.py --stage 0

# ارزیابی همه مراحل به صورت یکجا
python evaluator.py --all
```

---

## 📁 ساختار پوشه‌های ارزیاب

```text
stage-evaluator/
├── index.html            # رابط کاربری وب با تم تاریک شیشه‌ای مدرن
├── app.css               # استایل‌های مدرن با فونت وزیرمتن و راست‌چین
├── app.js                # منطق آزمون‌ها، محاسبه نمرات و صدور گواهینامه
├── evaluator.py          # تست‌رنر رسمی پایتون با خروجی رنگی ترمینال
├── mastery_ledger.json   # دفترکل ذخیره امتیازات و تاریخچه ارزیابی‌ها
├── challenges/           # فایل‌های پیاده‌سازی کدهای عملی هر مرحله
│   ├── stage_0_python.py
│   ├── stage_1_backend.py
│   ├── stage_2_machine_learning.py
│   ├── stage_3_rag_systems.py
│   ├── stage_4_agentic_mcp.py
│   ├── stage_5_multimodal.py
│   └── stage_6_production_pilot.py
└── tests/                # آزمون‌های واحد خودکار (Unit Tests) هر مرحله
    ├── test_stage_0.py
    ├── test_stage_1.py
    ├── test_stage_2.py
    ├── test_stage_3.py
    ├── test_stage_4.py
    ├── test_stage_5.py
    └── test_stage_6.py
```
