from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def download_inline():
    choice_column = InlineKeyboardMarkup(row_width=2)
    for day, day_number in zip(range(28, 32), range(28, 32)):
        number_column = InlineKeyboardButton(text=str(day), callback_data=str(day_number))
        choice_column.insert(number_column)
    return choice_column