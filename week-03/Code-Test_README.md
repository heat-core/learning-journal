اکنون که با موفقیت پروژه‌ی مدل‌سازی کشور کوئرا را تکمیل کرده‌اید و یک مدل شیءگرا از یک سیستم اقتصادی-اجتماعی ساده را پیاده‌سازی نموده‌اید، می‌خواهیم نگاهی دقیق‌تر به چگونگی کارکرد این سیستم، کاربردهای آن و نحوه‌ی استفاده از کلاس‌هایی که ساخته‌اید بیندازیم.
مروری بر مفاهیم کلیدی

این پروژه به شما نشان داد که چگونه می‌توان با استفاده از مفاهیم شیءگرایی مانند کلاس‌ها، اشیاء، ارث‌بری و چندریختی (Polymorphism)، یک سیستم پیچیده را به اجزای کوچک‌تر و قابل‌مدیریت تقسیم کرد.
چگونه شبیه‌ساز کار می‌کند؟

بیایید ببینیم چگونه می‌توانید با کلاس‌هایی که نوشته‌اید، تعامل کنید. ابتدا، کلاس‌های مورد نیاز را وارد (import) می‌کنیم.

# Importing Person classes
from person import Person
from engineer import Engineer
from teacher import Teacher
from worker import Worker

# Importing WorkPlace classes
from work_place import WorkPlace, WorkPlaceIsFull, Consts as WorkPlaceConsts
from mine import Mine
from school import School
from company import Company

Python
main.py

توجه: در کد واقعی، ممکن است نیاز به تنظیم مسیرهای وارد کردن بر اساس ساختار پوشه پروژه باشد.
۱. ایجاد افراد

شما می‌توانید نمونه‌هایی از انواع مختلف افراد ایجاد کنید.

# Creating an engineer
raha = Engineer(name="Raha", age=30)

# Creating a teacher
sara = Teacher(name="Sara", age=25)

# Creating a worker
taha = Worker(name="Taha", age=22)

print(f"Total number of people: {len(Person.instances)}")
for p in Person.instances:
    print(f"- {p.name} ({p.get_job()}), Level: {p.level}")

Python
main.py

خروجی:

Total number of people: 3
- Raha (engineer), Level: 1
- Sara (teacher), Level: 1
- Taha (worker), Level: 1

Plain text

هر فرد با نام، سن، سطح اولیه‌ی ۱ و شغل مشخص خود ایجاد می‌شود.
۲. ایجاد محل‌های کار

به طور مشابه، می‌توانید محل‌های کار مختلفی ایجاد کنید.

# Creating a mine
kavir_mine = Mine(name="Kavir Mine")

# Creating a school
danesh_school = School(name="Danesh School")

# Creating a company
pishro_company = Company(name="Pishro Company")

print(f"\nTotal number of workplaces: {len(WorkPlace.instances)}")
for wp in WorkPlace.instances:
    print(f"- {wp.name} ({wp.get_expertise()}), Level: {wp.level}, Initial Capacity: {wp.capacity}")

Python

خروجی:

Total number of workplaces: 3
- Kavir Mine (mine), Level: 1, Initial Capacity: 1
- Danesh School (school), Level: 1, Initial Capacity: 1
- Pishro Company (company), Level: 1, Initial Capacity: 1

Plain text

هر محل کار با نام، سطح اولیه‌ی ۱، تخصص و ظرفیت اولیه خود (که توسط calc_capacity در سازنده والد فراخوانی نمی‌شود ولی در upgrade فراخوانی می‌شود) ایجاد می‌شود.
۳. استخدام افراد در محل‌های کار

افراد می‌توانند در محل‌های کار مرتبط استخدام شوند.

try:
    kavir_mine.hire(taha)
    print(f"\n{taha.name} was hired at {taha.work_place.name}.")

    danesh_school.hire(sara)
    print(f"{sara.name} was hired at {sara.work_place.name}.")

    pishro_company.hire(raha)
    print(f"{raha.name} was hired at {raha.work_place.name}.")

    print(f"Employees of {pishro_company.name}: {[e.name for e in pishro_company.employees]}")

    # Attempting to hire beyond capacity
    kamran = Engineer(name="Kamran", age=35)
    pishro_company.hire(kamran) # This line would raise an error

except WorkPlaceIsFull as e:
    print(f"Hiring error: {e}")

Python

خروجی:

Taha was hired at Kavir Mine.
Sara was hired at Danesh School.
Raha was hired at Pishro Company.
Employees of Pishro Company: ['Raha']
Hiring error: work place is full!

Plain text

متد hire فرد را به لیست کارمندان محل کار اضافه می‌کند و work_place فرد را به‌روز می‌کند. اگر ظرفیت پر باشد، استثنای WorkPlaceIsFull رخ می‌دهد.
۴. ارتقاء سطح (Upgrade)

هم افراد و هم محل‌های کار می‌توانند ارتقاء یابند.

print(f"\nInitial level of {raha.name}: {raha.level}")
raha.upgrade()
print(f"New level of {raha.name}: {raha.level}")

print(f"\nInitial level and capacity of {kavir_mine.name}: Level {kavir_mine.level}, Capacity {kavir_mine.capacity}")
kavir_mine.upgrade()
print(f"New level and capacity of {kavir_mine.name}: Level {kavir_mine.level}, Capacity {kavir_mine.capacity}")

Python

خروجی:

Initial level of Raha: 1
New level of Raha: 2

Initial level and capacity of Kavir Mine: Level 1, Capacity 1
New level and capacity of Kavir Mine: Level 2, Capacity 4

Plain text

ارتقاء سطح فرد، level او را افزایش می‌دهد. ارتقاء سطح محل کار، level آن را افزایش داده و متد calc_capacity را برای به‌روزرسانی ظرفیت فراخوانی می‌کند.
۵. محاسبات مالی

کلاس‌ها متدهایی برای محاسبه‌ی درآمد، هزینه و وضعیت مالی خالص دارند.

taha_base_income = taha.calc_income()
print(f"\nBase daily income for {taha.name}: {taha_base_income}")

taha_life_cost = taha.calc_life_cost()
print(f"Daily living cost for {taha.name}: {taha_life_cost}")

taha_net_daily = taha.calc()
print(f"Net daily financial status for {taha.name}: {taha_net_daily}")


mine_maintenance_cost = kavir_mine.calc_costs()
print(f"\nDaily maintenance cost for {kavir_mine.name}: {mine_maintenance_cost}")

mine_net_daily = kavir_mine.calc()
print(f"Net daily financial status for {kavir_mine.name}: {mine_net_daily}")

Python

خروجی:

Base daily income for Taha: 545
Daily living cost for Taha: 293
Net daily financial status for Taha: 477.7463914933369

Daily maintenance cost for Kavir Mine: 2600
Net daily financial status for Kavir Mine: -2600

Plain text
۶. محاسبات کلی

متدهای استاتیک calc_all برای محاسبه مجموع وضعیت مالی تمام افراد یا تمام محل‌های کار استفاده می‌شوند.

total_people_financial_status = Person.calc_all()
print(f"\nTotal daily financial status of all people: {total_people_financial_status}")

total_workplaces_financial_status = WorkPlace.calc_all()
print(f"Total daily financial status of all workplaces: {total_workplaces_financial_status}")

overall_economy_status = total_people_financial_status + total_workplaces_financial_status
print(f"Overall simulator economy status: {overall_economy_status}")

Python

خروجی:

Total daily financial status of all people: 1003.5953800911152
Total daily financial status of all workplaces: -7600
Overall simulator economy status: -6596.404619908884

Plain text
کاربردهای دیگر

این شبیه‌ساز یک نقطه‌ی شروع بود. شما می‌توانید آن را با افزودن ویژگی‌های جدید گسترش دهید:

    انواع شغل و محل کار جدید: مانند کشاورز و مزرعه، پزشک و بیمارستان.
    منابع و تولید: مدل‌سازی تولید کالاها و خدمات.
    بازار: مکانیزمی برای خرید و فروش.
    دولت و مالیات: اضافه کردن یک نهاد دولتی و سیستم مالیاتی.

پروژه‌ی «کشور کوئرا» یک تمرین برای به‌کارگیری عملی اصول شیءگرایی بود. با درک نحوه‌ی تعامل کلاس‌ها و اشیاء، شما اکنون می‌توانید مدل‌های پیچیده‌تری را طراحی و پیاده‌سازی کنید.