import asyncio

from config import TG_API_TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


bot = Bot(token=TG_API_TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message) -> None:
    await message.answer('Привет! Меня зовут Пятница. Я твой финансовый менеджер. Чем могу помочь?')


@dp.message(Command('help'))
async def cmd_help(message: types.Message) -> None:
    await message.answer(
        'Вот чем я могу помочь:\
        \n1. Добавить новые расходы.\
        \n2. Удалить последние расходы.\
        \n3. Показать статистику.'
    )


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())