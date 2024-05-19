import asyncio
import expenses

from config import TG_API_TOKEN
from aiogram import F, Bot, Dispatcher, types
from aiogram.filters.command import Command


bot = Bot(token=TG_API_TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def send_welcome(message: types.Message) -> None:
    '''Функция отправляет приветствие'''
    buttons = [
        [
            types.KeyboardButton(text='Команды'),
            types.KeyboardButton(text='Справка'),
        ]
    ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer('Привет! Меня зовут Пятница. Я твой финансовый менеджер. Чем могу помочь?', reply_markup=keyboard)


@dp.message(F.text.lower() == 'команды')
async def send_commands(message: types.Message) -> None:
    '''Функция отправляет список команд'''
    answer = 'Эта штука пока не работает. Но скоро тут будут все команды доступные для бота.'
    await message.answer(answer)
        

@dp.message(F.text.lower() == 'справка')
async def send_help(message: types.Message) -> None:
    '''Функция отправляет небольшую справку'''
    answer = 'Чтобы добавить расход напиши сумму и предмет траты. Например: 150 такси. ' + \
    'Сохраняется сумма, дата и категория расхода. Список всех категорий и других команд для бота можешь найти в меню.'
    await message.answer(answer)


@dp.message(Command('statstoday'))
async def send_statistics_today(message: types.Message) -> None:
    '''Функция отправляет статистику за сегодня, то есть общую сумму расходов'''
    answer = expenses.get_statistics_today()
    await message.answer(answer)


@dp.message(Command('listtoday'))
async def send_list_today(message: types.Message) -> None:
    '''Функция отправляет список расходов за сегодня'''
    answer = expenses.get_list_expenses_today()
    await message.answer(answer)


@dp.message()
async def add_expense(message: types.Message):
    '''Функция добавляет расход'''
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