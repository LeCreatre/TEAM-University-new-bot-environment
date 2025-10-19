# bot.py
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

TOKEN = os.getenv("BOT_TOKEN") or "PASTE_YOUR_TOKEN_HERE"

# === Главное меню (ровно в заданном порядке) ===
MENU = [
    "О TEAM University",
    "Программы Обучения",
    "Курс Pre-Foundation",
    "Стоимость и Гранты",
    "Как поступить",
    "Наши Преподаватели",
    "3D Кампус Тур",
    "Наши Учредители",
    "Чат с Admissions TEAM",
    "Контакты",
]

def main_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(*[KeyboardButton(t) for t in MENU])
    return kb

# === ТЕКСТЫ ОТВЕТОВ (ИДЕНТИЧНЫ ТВОИМ) ===
TEXT_START = (
    "Привет! я ваш личный бот-консультант который поможет вам больше узнать о первом предпринимательском университете страны- TEAM University"
)

TEXT_1 = (
    "TEAM University — это первый предпринимательский университет в Узбекистане который был основан в 2020 году- 10 предпринимателями в партнерстве с университетом Великобритании- London South Bank University (est. 1892) Наш образовательный партнер- в общем мировом рейтинге университетов Times Higher Education LSBU занимает 601 место. \n\n"
    "В TEAM University- студенты учатся не просто теории, а тому, как строить бизнес, управлять проектами и работать в международной среде.\n\n"
    "Наши преподаватели — зарубежные и местные эксперты, действующие предприниматели, а учебный процесс связан с реальными компаниями и кейсами.\n\n"
    "TEAM — это сообщество людей, которые хотят создавать, а не просто учиться и также мы помогаем нашим студентам развивать карьеру и находить стажировки."
)

# В ЭТОМ БЛОКЕ фраза "Узнать подробнее о направлении" должна быть ссылкой,
# при этом мы сохраняем точный вид строки (оставляем дефис и URL в тексте).
TEXT_2 = (
    "В TEAM University есть 3 актуальные программы обучения: \n"
    "BA (Hons) Предпринимательство и Международный Бизнес \n"
    "<a href='https://teamuni.uz/ru/ba-hons-entrepreneurship-with-international-business/'>Узнать подробнее о направлении</a>- https://teamuni.uz/ru/ba-hons-entrepreneurship-with-international-business/\n\n"
    "BA (Hons) Предпринимательство и Цифровые Инновации\n"
    "<a href='https://teamuni.uz/ru/ba-hons-entrepreneurship-with-digital-innovations/'>Узнать подробнее о направлении</a>- https://teamuni.uz/ru/ba-hons-entrepreneurship-with-digital-innovations/\n \n"
    "BA (Hons) Предпринимательство и Маркетинг\n"
    "<a href='https://teamuni.uz/ru/ba-hons-entrepreneurship-with-marketing/'>Узнать подробнее о направлении</a>- https://teamuni.uz/ru/ba-hons-entrepreneurship-with-marketing/\n\n"
    "строка “узнать подробнее о направлении” - должна быть ссылкой, то есть когда нажимаешь на предложение у тебя сразу открывается ссылка, не нужно лишних кнопок."
)

TEXT_3 = (
    "Pre-Foundation — это подготовительный курс для тех, кто хочет поступить в TEAM University, но пока не уверен в уровне английского или просто хочет подготовиться.\n"
    "На курсе изучают английский, а также знакомятся с университетской культурой.\n"
    "Вы попадаете в атмосферу настоящего студенческого комьюнити: бизнес-завтраки, \n"
    "мероприятия, встречи с предпринимателями.После завершения курса можно поступить без вступительных экзаменов."
)

TEXT_4 = (
    "Годовая плата за обучение в университете TEAM составляет 38 348 000 Сум, оплата за обучение может производиться частями. Мы поддерживаем тех, кто показывает хорошие результаты, участвует в жизни университета и стремится к развитию. \n"
    "TEAM University предлагает различные гранты для мотивированных студентов.\n"
    "Существуют также академические гранты, скидки по результатам тестов и конкурсов."
)

TEXT_5 = (
    "Процесс поступления в TEAM University максимально понятный и открытый.\n"
    "Вы подаете заявку онлайн и сдаете внутренний вступительный экзамен в кампусе университета TEAM (на нашем сайте по ссылке ниже также вы можете посмотреть образец теста). \n\n"
    "Если у вас есть сертификат IELTS- 5.5 или DUOLINGO- 90 вы можете поступить в TEAM University без вступительных экзаменов. \n\n"
    "После этого остается только оформить документы. Все шаги, сроки и документы подробно описаны на нашем сайте. "
)

TEXT_6 = (
    "Преподаватели TEAM University — это профессионалы с опытом в бизнесе, IT, маркетинге и финансах. Многие из них — выпускники международных университетов и действующие эксперты в своих областях. Они помогают студентам не только понять предмет, но и применить знания в жизни, найти идею для стартапа и развить soft skills."
)

TEXT_7 = (
    "Текст ответа- Открой двери TEAM University в 3D-туре!\n"
    "Посети современные аудитории, коворкинги, зоны отдыха и уютные пространства кампуса. Мы создали среду, где комфортно учиться, развиваться и общаться."
)

TEXT_8 = (
    "TEAM University основан известными предпринимателями Узбекистана — людьми, которые создали успешные компании и теперь помогают новым поколениям студентов.\n"
    "Учредители активно участвуют в жизни университета: проводят лекции, встречаются со студентами и делятся своим опытом.\n"
    "TEAM — это университет, где бизнес стоит не рядом с образованием, а внутри него."
)

TEXT_9 = (
    "Если у вас остались вопросы — о поступлении, грантам, оплате или просто о студенческой жизни — пишите нам прямо сейчас.\n"
    "Команда Admissions ответит в течение нескольких минут и поможет со всеми шагами поступления. Не откладывайте: напишите, если хотите уточнить детали или получить консультацию в кампусе университета TEAM "
)

TEXT_10 = (
    "📍 Адрес: г. Ташкент, Мирзо-Улугбекский район, улица Темура Малика, 146\n"
    "📞 Телефон: +998 71 200 20 60\n"
    "✉️ Email: info@teamuni.uz\n"
    "🕘 График работы: Пн–Пт 09:00–18:00\n"
    "Будем рады ответить на все вопросы и встретиться с вами в нашем кампусе! \n"
)

# === КНОПКИ "ниже" (строго по формулировкам) ===
BTN_4 = ("Узнайте подробнее", "https://teamuni.uz/ru/fees")
BTN_5 = ("Узнайте подробнее", "https://teamuni.uz/ru/admission")
BTN_6 = ("Узнайте подробнее", "https://teamuni.uz/ru/academic-staff")
BTN_7 = ("Смотреть тур", "https://my.matterport.com/show/?m=xoz1yxpFF7t")
BTN_8 = ("Узнайте подробнее", "https://teamuni.uz/ru/founders-of-team-university")
BTN_9 = ("Чат с Admissions TEAM", "https://t.me/teamuni_uz")

# === Сопоставление разделов: (текст, (текст_кнопки, url) | None) ===
SECTIONS = {
    "О TEAM University": (TEXT_1, None),
    "Программы Обучения": (TEXT_2, None),  # без дополнительных кнопок
    "Курс Pre-Foundation": (TEXT_3, None),
    "Стоимость и Гранты": (TEXT_4, BTN_4),
    "Как поступить": (TEXT_5, BTN_5),
    "Наши Преподаватели": (TEXT_6, BTN_6),
    "3D Кампус Тур": (TEXT_7, BTN_7),
    "Наши Учредители": (TEXT_8, BTN_8),
    "Чат с Admissions TEAM": (TEXT_9, BTN_9),
    "Контакты": (TEXT_10, None),
}

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def cmd_start(message: types.Message):
    await message.answer(TEXT_START, reply_markup=main_kb())

@dp.message_handler(lambda m: m.text in MENU)
async def handle_menu(message: types.Message):
    title = message.text
    text, btn = SECTIONS[title]

    if btn is None:
        await message.answer(text)
        return

    btn_text, btn_url = btn
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text=btn_text, url=btn_url))
    await message.answer(text, reply_markup=kb)

@dp.message_handler()
async def fallback(message: types.Message):
    await message.answer("Пожалуйста, выберите раздел из меню ниже 👇", reply_markup=main_kb())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
