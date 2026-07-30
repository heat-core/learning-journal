# راهنمای جامع اصلاح اطلاعات نویسنده (Author) در کامیت‌های گذشته Git

در این راهنما، علت عدم اتصال کامیت‌های محلی به پروفایل GitHub بررسی شده و نحوه حل این مشکل با استفاده از دستورات Git به‌صورت گام‌به‌گام توضیح داده می‌شود.

---

## ۱. علت بروز مشکل

وقتی در GitHub کامیت‌های ارسال‌شده (Push شده) به حساب کاربری شما متصل نمی‌شوند و آواتار شما کنار آن‌ها قرار نمی‌گیرد، دلیل اصلی **عدم تطابق ایمیل یا نام تنظیم‌شده در Git محلی با حساب GitHub** است.

برای مثال، اگر ایمیل ثبت‌شده در تنظیمات محلی Git دارای تایپو باشد (مانند `far.jolani@gmial.com` به جای `farbod.jolani00@gmail.com`)، سیستم Git تغییرات را ثبت می‌کند، اما GitHub قادر به تشخیص هویت شما نیست.

---

## ۲. تنظیم اطلاعات صحیح برای کامیت‌های آینده

برای اینکه تمامی کامیت‌های بعدی به‌صورت خودکار به حساب کاربری شما نسبت داده شوند، تنظیمات سراسری (Global) زیر را در ترمینال اجرا کنید:

```bash
git config --global user.name "heat-core"
git config --global user.email "farbod.jolani00@gmail.com"
```

### بررسی تنظیمات فعلی:
جهت اطمینان از صحت اطلاعات تنظیم‌شده:
```bash
git config --global user.name
git config --global user.email
```

---

## ۳. بازنویسی تاریخچه کامیت‌های گذشته (Rewrite Git History)

اگر کامیت‌های قبلی با ایمیل اشتباه ثبت شده باشند، باید تاریخچه شاخه (Branch) بازنویسی شود تا ایمیل نویسنده (Author Email) و کمیتور (Committer Email) اصلاح گردد.

### دستور بازنویسی تاریخچه:

دستور زیر کل تاریخچه شاخه را پیمایش کرده و تمام کامیت‌هایی که با ایمیل قدیمی ثبت شده‌اند را به ایمیل و نام صحیح تغییر می‌دهد:

```bash
git filter-branch -f --env-filter '
OLD_EMAIL="far.jolani@gmial.com"
CORRECT_NAME="heat-core"
CORRECT_EMAIL="farbod.jolani00@gmail.com"

if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags
```

---

## ۴. اعمال تغییرات روی GitHub (Force Push)

چون هش (Hash) تمامی کامیت‌های گذشته تغییر کرده است، امکان Push معمولی وجود ندارد. برای جایگزینی تاریخچه جدید در مخزن از پرچم `--force` استفاده می‌شود:

```bash
git push --force origin main
```

---

## ۵. خلاصه فرآیند کار

| مرحله | دستور / اقدام | هدف |
| :--- | :--- | :--- |
| **۱. اصلاح کانفیگ** | `git config --global user.email "..."` | تنظیم ایمیل صحیح برای آینده |
| **۲. بازنویسی تاریخچه** | `git filter-branch ...` | جایگزینی ایمیل اشتباه در کامیت‌های قبلی |
| **۳. به‌روزرسانی ریموت** | `git push --force origin main` | همگام‌سازی تاریخچه اصلاح‌شده با GitHub |

