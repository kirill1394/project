from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
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
dp = Dispatcher(bot)
kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True) #!
b1 = KeyboardButton("/help")
b2 = KeyboardButton("/image")
b3 = KeyboardButton("/location")
kb.add(b1)
kb.add(b2)
kb.add(b3)
#kb.add(KeyboardButton("/help"))

async def on_startup(_):
    print('Бот запущен')


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


#@dp.message_handler(commands=['give'])  # отрпавка эмодзи Get sticker id бот для айди стикеров
#async def help_command(message: types.Message):
    #await bot.send_sticker(message.from_user.id, sticker="")
    #await message.delete()


@dp.message_handler(commands=['image'])  # отправка фото
async def send_image(message: types.Message):
    await bot.send_photo(message.from_user.id,
                          photo='https://a.d-cd.net/55316c4s-960.jpg')
    await message.delete()


@dp.message_handler(commands=['location'])  # отправка локации
async def send_point(message: types.Message):
    await bot.send_location(message.from_user.id,
                            latitude=58.638136,
                            longitude=49.575228)
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
