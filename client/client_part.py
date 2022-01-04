from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.types.callback_query import CallbackQuery

from help_file import dp, bot
from keyboards.client_kb import choice_column_header_client, choice_yes_or_not, choice_day
from pandas_test.excel_method import read_column_header_comment, change_cell, read_column_header


class FSMAdmin(StatesGroup):
    day = State()
    essence = State()
    sequence = State()
    yes_or_no_comment = State()
    comment = State()
    add_change = State()

async def start_change(message: types.Message):
    inline_choose_day = choice_day('Дата')
    await FSMAdmin.next()
    await message.reply('Выберите за какой день вы хотите сделать запис', reply_markup=inline_choose_day)

async def callback_change_day(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as cell:
        cell['day'] = callback_query.data
    inline_choose_essence = choice_column_header_client()
    await FSMAdmin.next()
    await callback_query.message.edit_text('Какую колонку хотите заполнить?', reply_markup=inline_choose_essence)

async def callback_change_essence(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as cell:
        for name_column, number_column in zip(read_column_header()[1:], range(1, len(read_column_header()[1:]))):
            print(callback_query.data, number_column)
            if str(number_column) == callback_query.data:
                cell['essence'] = name_column
                print(name_column)
                break
    await callback_query.message.edit_text('Отправьте значение для заполнения')
    await FSMAdmin.next()

async def change_sequence(message: types.Message, state: FSMContext):
    async with state.proxy() as cell:
        cell['sequence'] = message.text
    await FSMAdmin.next()
    inline_choose_yes_not = choice_yes_or_not()
    await message.reply('Хотите добавить комментарий?', reply_markup=inline_choose_yes_not)

async def callback_yes_or_not(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == 'yes':
        async with state.proxy() as cell:
            cell['yes_or_no_comment'] = callback_query.data
        await callback_query.message.edit_text('Введите комментарий к записи')
        await FSMAdmin.next()
    elif callback_query.data == 'not':
        async with state.proxy() as cell:
            inline_choose_yes_not = choice_yes_or_not()
            cell['yes_or_no_comment'] = callback_query.data
            await FSMAdmin.next()
            cell['comment'] = '-'
            await FSMAdmin.next()
            await callback_query.message.edit_text(f"""Отлично, Вы хотите заполнить:
            Cтолбец:{cell['essence']}
            За днем: {cell['day']} день
            Таким значение: {cell['sequence']}
            Без комментария
            Все верно, заполняем?""", reply_markup=inline_choose_yes_not)

async def change_comment(message: types.Message, state: FSMContext):
    async with state.proxy() as cell:
        inline_choose_yes_not = choice_yes_or_not()
        cell['comment'] = message.text
        await message.answer(f"""Отлично, Вы хотите заполнить:
        Cтолбец:{cell['essence']}
        За день: {cell['day']} день
        Таким значение: {cell['sequence']}
        Комментарий: {cell['comment']}
        Все верно, заполняем?""", reply_markup=inline_choose_yes_not)
        await FSMAdmin.next()

async def callback_add_change(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == 'yes':
        async with state.proxy() as cell:
            change_cell(cell['day'], cell['essence'], cell['sequence'])
            change_cell(cell['day'], read_column_header_comment(cell['essence']), cell['comment'])
            await callback_query.message.edit_text('Изменения внесены')
            await state.finish()
            return
    elif callback_query.data == 'not':
        await state.finish()
        await callback_query.message.edit_text('Изменения не внесены')
        return

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_change, commands=['entry'], state=None)
    dp.register_callback_query_handler(callback_change_day, state=FSMAdmin.day)
    dp.register_callback_query_handler(callback_change_essence, state=FSMAdmin.essence)
    dp.register_message_handler(change_sequence, state=FSMAdmin.sequence)
    dp.register_callback_query_handler(callback_yes_or_not, state=FSMAdmin.yes_or_no_comment)
    dp.register_message_handler(change_comment, state=FSMAdmin.comment)
    dp.register_callback_query_handler(callback_add_change, state=FSMAdmin.add_change)


