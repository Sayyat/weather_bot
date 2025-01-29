# Telegram Бот (Aiogram) Жобасы


Бұл жоба Telegram мессенджері үшін жазылған ботты көрсетеді. Ботта бірнеше негізгі функциялар қарастырылған:
- Қала атауын сақтау және көрсету
- Ауа райын (Visual Crossing API арқылы) тексеру
- Бірнеше тілде жұмыс істеуді қолдау (i18n)
- Пайдаланушының сұраныстарын өңдеу үшін маршрутизация (router) және күй басқару (StateMachine)
- Логтау және конфигурация файлдарымен (`.env`) жұмыс істеу


[Жоба Youtube - та](https://www.youtube.com/watch?v=oQIel3SUruI&t=40s)

## Мазмұны
1. [Технологиялар мен кітапханалар](#технологиялар-мен-кітапханалар)
2. [Орнату және баптау](#орнату-және-баптау)
3. [Параметрлер (.env)](#параметрлер-env)
4. [Ботты іске қосу](#ботты-іске-қосу)
5. [Бот командалары](#бот-командалары)
6. [Локализация (i18n)](#локализация-i18n)
7. [Қатысу және үлес қосу](#қатысу-және-үлес-қосу)
8. [Лицензия](#лицензия)

---

## Технологиялар мен кітапханалар
- **[Python 3.9+](https://www.python.org/) 3.11.9 ұсынылады**
- **[Aiogram](https://docs.aiogram.dev/)** – Telegram Bot API-мен жұмыс істеуге арналған кітапхана.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** – `.env` файлындағы құпия деректерді оқу үшін.
- **[Visual Crossing](https://www.visualcrossing.com/)** – Ауа райы туралы деректерге арналған API.
- **[i18n](https://pypi.org/project/aiogram-i18n/)** – Халықаралықдандыру (локализация) жүйесі.
- **[logging](https://docs.python.org/3/library/logging.html)** – Лог жүргізу механизмі.

## Орнату және баптау

1. **Жаңа қалта** ашыңыз (мысалы, `weather_bot`).
2. **Виртуалды орта** жасаңыз және іске қосыңыз:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. **Керекті кітапханаларды** орнатыңыз:
   ```bash
   pip install -r requirements.txt
   ```
   Егер `requirements.txt` файлы жоқ болса, кітапханаларды қолмен орнатыңыз:
   ```bash
   pip install aiogram aiogram[i18n] python-dotenv
   ```

## Параметрлер (.env)

Жоба түбірінде (root) `.env` файлын жасаңыз. Мысалы:

```env
BOT_TOKEN="telegram_bot_father_token_here"
WEATHER_API_KEY="visual_crossing_api_key_here"
```

> **Ескерту**: `.env` файлын ешқашан жалпыға қолжетімді жерге жүктемеңіз (GitHub-қа pushed, т.с.с). Ол құпия деректерді сақтау үшін қажет.

## Ботты іске қосу

1. `.env` файлыңыздағы параметрлердің дұрыс толтырылғанын тексеріңіз.
2. Төмендегі пәрмен арқылы ботты іске қосыңыз:
   ```bash
   python main.py
   ```
3. Терминалда «Bot started» сынды хабарламаны көрсеңіз, бот сәтті іске қосылды деген сөз.

## Бот командалары

| Команда               | Сипаттамасы                                       |
|-----------------------|--------------------------------------------------|
| `/start`              | Ботты бастау, негізгі нұсқаулықты көрсету        |
| `/set_my_city`        | Өз қалаңызды орнату үшін                         |
| `/show_my_city`       | Бұрын орнатылған қалаңызды көру                  |
| `/weather_in_my_city` | Орнатылған қалаңыздың ауа райын тексеру          |
| `weather:{city}`      | Кез келген қала бойынша бір реттік ауа райын тексеру |
| `/set_language`       | Боттың тілін өзгерту (қазақша, орысша, ағылшынша) |

> **state** және **StatesGroup** – бұл Aiogram-дағы пайдаланушының ботпен ара қатынасын басқару үшін қолданылатын механизм. Олар бірнеше диалогтік қадамдарды ұйымдастыруға көмектеседі.

## Локализация (i18n)

Жоба бірнеше тілді қолдайды. **i18n** кітапханасы арқылы енгізілген. Тілдерді ауыстыру үшін `/set_language` командасын пайдаланыңыз.  

Локализация файлы (мысалы, `locales/`) ішінде әр тілге сәйкес `.json` немесе `.mo/.po` файлдар құрып, аудармалар жазылады. Aiogram іске қосылғанда, пайдаланушының таңдауына қарай қажет файлдар жүктеледі.

## Қатысу және үлес қосу

1. **Fork** жасап алыңыз немесе репозиторийді жүктеңіз.
2. Қажетті өзгертулер енгізіңіз.
3. **Pull Request** жіберіңіз немесе жобаны жеке қолданысыңызға бейімдеңіз.

## Лицензия

Бұл жоба ашық көзі бар (open-source) жоба үлгісі ретінде жарияланған. Қосымша ақпаратты `LICENSE` файлынан қараңыз (егер ол репозиторийде болса).  

Егер сұрақтарыңыз немесе ұсыныстарыңыз болса, еркін түрде issue немесе pull-request жіберіңіз!  
Рахмет!