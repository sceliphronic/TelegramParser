from aiogram import Bot, Dispatcher, executor, types
from config import token
from main import weather

bot=Bot(token=token)
dp=Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.reply(weather())

if __name__ == '__main__':
    executor.start_polling(dp)