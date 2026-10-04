# فلوچارت جامع و درخت تصمیم‌گیری نقشه راه ۲۴ ماهه مهندسی هوش مصنوعی
### نسخه اجرایی ۴ - منطبق بر مستند اصلی (Farbod 24-Month AI Blueprint)

---

## ۱. نمای کلان معماری ۲۴ ماهه (Macro 24-Month Architecture)

نمودار زیر توالی فازهای ۵‌گانه سال اول و دوم، پروژه‌های خروجی‌محور (P0 تا P6)، و دروازه‌های کنترل کیفیت (Gates 0-6) را نمایش می‌دهد:

`mermaid
flowchart TD
    classDef foundation fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef ml fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#f8fafc;
    classDef llm fill:#1e1b4b,stroke:#6366f1,stroke-width:2px,color:#f8fafc;
    classDef agent fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#f8fafc;
    classDef multi fill:#451a03,stroke:#f59e0b,stroke-width:2px,color:#f8fafc;
    classDef gate fill:#7f1d1d,stroke:#ef4444,stroke-width:3px,color:#fef2f2;
    classDef career fill:#134e4a,stroke:#14b8a6,stroke-width:2px,color:#f0fdfa;

    Start([شروع: ارزیابی مبانی و تنظیم ابزارها]):::foundation --> Gate0{دروازه ۰: روز هفتم<br/>آزمون پایتون + محیط گیت}:::gate

    Gate0 -->|قبول| Phase1[فاز ۱: مهندسی پایتون، وب، دیتابیس و داکر<br/>هفته ۱ تا ۸]:::foundation
    Gate0 -->|شکاف پایه| Rem1[رفع شکاف با تمرینات Arena + CS50P]:::foundation --> Phase1

    Phase1 --> P0[پروژه P0: Production Python API<br/>FastAPI + PostgreSQL + Docker + CI]:::foundation
    P0 --> Gate1{دروازه ۱: پایان هفته ۸<br/>تست سبز + داکر + OpenAPI}:::gate

    Gate1 -->|قبول| Phase2[فاز ۲: آمار کاربردی و یادگیری ماشین کلاسیک<br/>هفته ۹ تا ۱۶]:::ml
    Gate1 -->|نقص داکر یا تست| FixP0[تکمیل تست و CI به مدت حداکثر ۲ هفته]:::foundation --> Gate1

    Phase2 --> P1[پروژه P1: Production ML Engine<br/>Scikit-Learn + Feature Pipeline + Model Card]:::ml
    P1 --> Gate2{دروازه ۲: پایان هفته ۱۶<br/>بنچ‌مارک واقعی + تست و API مدل}:::gate

    Gate2 -->|قبول| Phase3[فاز ۳: دیپ‌لرنینگ، مدل‌های زبانی محلی و RAG سازمانی<br/>هفته ۱۷ تا ۳۲]:::llm
    Phase3 --> LocalLLM[استقرار محلی مدل روی RTX 3090 24GB<br/>Ollama / vLLM / HuggingFace]:::llm
    LocalLLM --> P2[پروژه P2: Enterprise Evidence-Grounded RAG<br/>Sentence-Transformers + Vector DB + Ragas Eval]:::llm
    P2 --> Gate3{دروازه ۳: پایان هفته ۳۲<br/>ارزیابی ۱۰۰ سؤاله + استناد دقیق + گاردریل امنیتی}:::gate

    Gate3 -->|قبول| Phase4[فاز ۴: سیستم‌های ایجنتی، MCP و هوش چندرسانه‌ای<br/>هفته ۳۳ تا ۴۸]:::agent
    Phase4 --> P3[پروژه P3: Agentic AI Workflow & MCP Server<br/>ReAct + Tool Calling + Human In The Loop]:::agent
    Phase4 --> P4[پروژه P4: Multimodal Media Search Assistant<br/>مزیت تدوین و ویدیو: Whisper + OpenCV + CLIP]:::multi
    P3 & P4 --> Gate4{دروازه ۴: پایان هفته ۴۸<br/>پایلوت کاربر واقعی + ۲ کاربر تست‌کننده}:::gate

    Gate4 -->|قبول| Phase5[فاز ۵: استقرار پایلوت، کمپین استخدامی و مشارکت متن‌باز<br/>ماه ۱۱ تا ۱۸]:::career
    Phase5 --> P5[پروژه P5: Pilot With Real Users<br/>لاگ مانیتورینگ + فیدبک لوپ + پست‌مورتم]:::career
    Phase5 --> P6[پروژه P6: تکرار مقاله پژوهشی یا مشارکت در Open Source]:::career
    Phase5 --> Gate5{دروازه ۵: پایان ماه ۱۲<br/>۴ پروژه شاخص + ۱ پایلوت + رزومه شفاف}:::gate

    Gate5 --> CareerTracks[انتخاب مسیر نهایی: استخدام بین‌المللی / داخلی یا اپلای ارشد]:::career
`

---

## ۲. فلوچارت تشخیصی وضعیت: «الان کجای مسیرم و گام بعدی چیه؟»

هر زمان که سردرگم شدید یا خواستید وضعیت فعلی خود را بسنجید، از نمودار زیر استفاده کنید:

`mermaid
flowchart TD
    classDef check fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef action fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#f8fafc;
    classDef stop fill:#7f1d1d,stroke:#ef4444,stroke-width:2px,color:#fef2f2;

    Q1{آیا پایتون پیشرفته، ساختار شی‌ءگرا،<br/>تایپینگ و ماژولار بودن را مسلط هستید؟}:::check
    Q1 -->|خیر یا شک دارم| A1[گام بعدی شما:<br/>۱. حل ۲۰ مرحله چالش python-learning-arena<br/>۲. مطالعه فصل‌های هدفمند پایتون پیشرفته کوئرا]:::action
    Q1 -->|بله، کدهای تست‌شده می‌نویسم| Q2{آیا پروژه P0 شامل FastAPI، داکر،<br/>دیتابیس PostgreSQL و تست pytest دارید؟}:::check

    Q2 -->|خیر| A2[گام بعدی شما:<br/>ساخت پروژه P0: سرویس بک‌اند ماژولار با معماری لایه‌ای،<br/>کانتینر داکر و خط لوله CI در گیتهاب]:::action
    Q2 -->|بله، در گیتهاب موجود است| Q3{آیا مفاهیم آمار کاربردی و الگوریتم‌های<br/>کلاسیک یادگیری ماشین با Scikit-Learn را در قالب مدل‌کارت پیاده کردید؟}:::check

    Q3 -->|خیر| A3[گام بعدی شما:<br/>ورود به فاز ۲: یادگیری ماشین پیشرفته کوئرا + StatQuest<br/>ساخت پروژه P1 همراه با Feature Pipeline]:::action
    Q3 -->|بله، پیاده شده| Q4{آیا سیستم RAG بومی روی گرافیک RTX 3090<br/>همراه با بنچ‌مارک ارزیابی ۱۰۰ سؤاله Ragas ساخته‌اید؟}:::check

    Q4 -->|خیر| A4[گام بعدی شما:<br/>ورود به فاز ۳: استقرار مدل روی RTX 3090 با vLLM/Ollama<br/>پیاده‌سازی پایگاه برداری و پروژه P2]:::action
    Q4 -->|بله، ارزیابی شده است| Q5{آیا ایجنت ابزارمحور با پروتکل MCP و پروژه چندرسانه‌ای P4<br/>با پردازش ویدیو/صوت را تکمیل کرده‌اید؟}:::check

    Q5 -->|خیر| A5[گام بعدی شما:<br/>ورود به فاز ۴: ساخت Agentic AI با کنترل لوپ دستی<br/>و موتور جستجوی چندرسانه‌ای ویدیو با Whisper و CLIP]:::action
    Q5 -->|بله| A6[گام بعدی شما:<br/>ورود به فاز پایلوت واقعی، آماده‌سازی رزومه بر پایه Evidence<br/>و شروع درخواست‌های شغلی یا مکاتبه ارشد]:::action
`

---

## ۳. جدول تفصیلی دروازه‌های تصمیم‌گیری (Decision Gates Specification)

| دروازه (Gate) | زمان ارزیابی | شرط عبور (Pass Criteria) | در صورت رد شدن چه باید کرد؟ (Fail Action) |
| :--- | :--- | :--- | :--- |
| **Gate 0** | پایان هفته اول | قبولی بالای ۷۰٪ در تست‌های تشخیصی پایتون، راه‌اندازی کلید SSH گیت‌هاب و برنچ‌بندی تمیز. | توقف هرگونه ورود به کتابخانه‌های سنگین، حل ۲۰ چالش در python-learning-arena. |
| **Gate 1** | پایان هفته ۸ | انتشار ریپازیتوری P0 شامل FastAPI، اعتبارسنجی Pydantic، پایگاه داده PostgreSQL، تست با pytest بالای ۸۰٪ پوشش و Dockerfile بدون خطا. | تمدید حداکثر ۲ هفته؛ ممنوعیت خرید هر دوره جدید یا رفتن به سراغ یادگیری ماشین تا P0 تکمیل شود. |
| **Gate 2** | پایان هفته ۱۶ | پروژه P1 یادگیری ماشین با خط لوله تمیز پیش‌پردازش، ارزیابی بدون Data Leakage، مستند Model Card و سرویس RESTful آماده پیش‌بینی. | بازبینی اعتبارسنجی متقاطع (Cross-Validation)؛ مجاز نیستید قبل از یادگیری ماشین کلاسیک مستقیماً وارد ایجنت‌ها شوید. |
| **Gate 3** | پایان هفته ۳۲ | پروژه P2 سیستم RAG روی RTX 3090 با حداقل ۱۰۰ سؤال تست استاندارد (Evaluation Dataset)، ارزیابی Faithfulness و Context Recall با Ragas، استناد دقیق به خط و پاراگراف. | ممنوعیت ورود به فریم‌ورک‌های پیچیده ایجنت؛ ابتدا خطای سیستم بازیابی (Retrieval) و رتبه‌بندی مجدد (Reranking) را به زیر ۱۵٪ برسانید. |
| **Gate 4** | پایان هفته ۴۸ | پروژه P3 ایجنت با پروتکل MCP و پروژه P4 چندرسانه‌ای ویدیو/صوت؛ ارائه به حداقل ۲ کاربر واقعی برای تست تجربی. | عدم توسعه فیچرهای فانتزی؛ رفع باگ‌های گزارش‌شده کاربران، ساخت لاگ خطا و Runbook. |
| **Gate 5** | پایان ماه ۱۲ | پورتفولیوی ۴ پروژه‌ای قابل دفاع، حداقل ۱ پول‌ریکوئست پذیرفته‌شده در پروژه‌های عمومی معتبر، رزومه مبتنی بر خروجی و عدد و رقم. | ورود به کمپین جاب اپلای با ۵ الی ۸ درخواست هدفمند هفتگی برای موقعیت‌های Junior/Intern پایتون و هوش مصنوعی. |
| **Gate 6** | پایان ماه ۱۸ | تخصص عمیق در معماری سیستم‌های هوش مصنوعی (AI Systems)، سابقه کار تیمی یا فریلنسری پرداختی، نمره آیلتس بالای ۷.۰ برای مقاصد مهاجرتی/تحصیلی. | تمرکز روی یک نقش تخصصی، قطع مطالعه منابع پراکنده و ورود به قراردادهای بین‌المللی یا مصاحبه‌های ارشد. |
