from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

from help_file import dp, bot
from keyboards.admin_kb import download_inline
from pandas_test.excel_method import create_list_excel

ADMIN_ID = '387353019'

class FSMAdmin(StatesGroup):
    day_admin = State()

async def download(message: types.Message):
    """This is method send document for admin"""
    await message.reply_document(open('excel_py.xlsx', 'rb'))
    return

async def create_new_document(message: types.Message):
    """This is method download document and create new document"""
    inline_create = download_inline()
    try:
        await message.reply_document(open('excel_py.xlsx', 'rb'))
    except:
        pass
    await message.reply('Выберите сколько дней будет в документе', reply_markup=inline_create)
    await FSMAdmin.next()

async def inline_create(callback_query: types.CallbackQuery, state: FSMContext):
    create_list_excel(callback_query.data)
    # async with state.proxy() as cell:
    #     cell['day'] = callback_query.data
    await state.finish()
    await callback_query.message.edit_text('Создан новый документ')
    return




def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(download, commands=['download'])
    dp.register_message_handler(create_new_document, commands=['create'], state=None)
    dp.register_callback_query_handler(inline_create, state=FSMAdmin.day_admin)

