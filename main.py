from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup
from loader import Start
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# from aiogram.dispatcher.filters import Text

TOKEN_API = "6295255406:AAGvAPhL6qj3-kuxqvDe46b4uaDdOyhJ9Ds"  # автризационный токен
HELP_COMMAND = """
/help - список комманд
/start - начать работу с ботом
/give - бот отправляет стикер пока не работает
/image - бот отправит фото
/location - бот отправит опр. место

"""
# parser_mode="HTML" тип чтения сообщений
bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)  # !
b1 = KeyboardButton("/help")
b2 = KeyboardButton("/image")
b3 = KeyboardButton("/location")
b4 = KeyboardButton("/vote")
b5 = KeyboardButton("/start")
kb.add(b1, b2, b3, b4, b5)


# kb.add(KeyboardButton("/help"))

async def on_startup(_):
    print('Бот запущен')


# Машина состояний
@dp.message_handler(commands=["vote"])
async def vote_command(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='да', callback_data="like")
    ib2 = InlineKeyboardButton(text='нет', callback_data="dislike")
    ib3 = InlineKeyboardButton(text='еще', callback_data='das')
    ikb.add(ib1, ib2, ib3)
    uwu = {"Была ли у вас практика сегодня?": ikb}
    uwu_list = list(uwu.keys())
    await bot.send_message(chat_id=message.from_user.id,
                           text=uwu_list[+1],
                           reply_markup=uwu.get(uwu_list[+1]))
    await Start.start_practice.set()


@dp.message_handler(state=Start.start_practice)
async def practice(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["question1"] =
        data["practice1"] = message.text
        name = data["practice1"]
        uwu = {"question1": ikb}
        await bot.send_message(message.from_user.id,
                               text='Какой был вид занятия?')
        await Start.start_vid


# @dp.message_handler(commands=['vote'])
# async def vote_command(message: types.Message):
# ikb = InlineKeyboardMarkup(row_width=2)
# ib1 = InlineKeyboardButton(text='да', callback_data="like")
# ib2 = InlineKeyboardButton(text='нет', callback_data="dislike")
# ib3 = InlineKeyboardButton(text='еще', callback_data='das')
# ikb.add(ib1, ib2, ib3)
# await bot.send_message(chat_id=message.from_user.id,
# text='Была ли у вас практика по йоге сегодня?',
# reply_markup=ikb)


# @dp.callback_query_handler(text="like")
# async def ikb_cd_handler(callback: types.CallbackQuery):
# ikb = InlineKeyboardMarkup(row_width=2)
# ib1 = InlineKeyboardButton(text='Майсор', callback_data="maisor")
# ib2 = InlineKeyboardButton(text='Лед-класс', callback_data="")
# ib3 = InlineKeyboardButton(text='3', callback_data='ygj')
# ikb.add(ib1, ib2)
# await callback.message.answer(text='Какий тип занятия был?',
# reply_markup=ikb)


# @dp.callback_query_handler(text="dislike")
# async def ikb_cd_handler(callback: types.CallbackQuery):
# await callback.message.answer(text="Это нормально, отдыхать тоже важно!")


@dp.message_handler(commands=['help'])  # штука для приема комманд
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text=HELP_COMMAND)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text="Добро пожаловать",
                           reply_markup=kb)
    await message.delete()


# @dp.message_handler(commands=['give'])  # отрпавка эмодзи Get sticker id бот для айди стикеров
# async def help_command(message: types.Message):
# await bot.send_sticker(message.from_user.id, sticker="")
# await message.delete()


# @dp.message_handler(commands=['image'])  # отправка фото
# async def send_image(message: types.Message):
# await bot.send_photo(message.from_user.id,
# photo='https://a.d-cd.net/55316c4s-960.jpg')
# await message.delete()


# @dp.message_handler(commands=['location'])  # отправка локации
# async def send_point(message: types.Message):
# await bot.send_location(message.from_user.id,
# latitude=58.638136,
# longitude=49.575228)
# await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
