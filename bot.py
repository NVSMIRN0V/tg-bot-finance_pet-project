import asyncio
from multiprocessing.connection import answer_challenge
import expenses

from config import TG_API_TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


bot = Bot(token=TG_API_TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message) -> None:
    await message.answer('Привет! Меня зовут Пятница. Я твой финансовый менеджер. Чем могу помочь?')


@dp.message(Command('statstoday'))
async def send_statistics_today(message: types.Message) -> None:
    answer = expenses.get_statistics_today()
    await message.answer(answer)


@dp.message(Command('listtoday'))
async def send_statistics_today(message: types.Message) -> None:
    answer = expenses.get_list_expenses_today()
    await message.answer(answer)


@dp.message()
async def add_expense(message: types.Message):
    try:
        expense = expenses.add(message.text)
    except:
        await message.answer('Ошибка.') 
        return 
    await message.answer(f'Расход {expense.amount} на {expense.category} успешно добавлен.')


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())