from aiogram import Bot, Dispatcher, executor, types



TOKEN_API = "6295255406:AAGvAPhL6qj3-kuxqvDe46b4uaDdOyhJ9Ds" #автризационный токен
HELP_COMMAND = """
/help - список комманд
/start - начать работу с ботом
"""
#parser_mode="HTML" тип чтения сообщений
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
async  def on_startup(_):
    print('Бот запущен')


@dp.message_handler(commands=['help']) # штука для приема комманд
async  def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)
@dp.message_handler(commands=['start'])
async  def help_command(message: types.Message):
    await message.reply(text="Добро пожаловать")
    await message.delete()
@dp.message_handler(commands=['give']) #отрпавка эмодзи Get sticker id бот для айди стикеров
async  def help_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="")
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
