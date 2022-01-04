from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from pandas_test.excel_method import read_all, read_column_header


def choice_column_header_client():
    choice_column = InlineKeyboardMarkup(row_width=2)
    for name_column, number_column in zip(read_column_header()[1:], range(1, len(read_column_header()[1:]))):
        number_column = InlineKeyboardButton(text=name_column, callback_data=str(number_column))
        choice_column.insert(number_column)
    return choice_column

def choice_yes_or_not():
    choice_column = InlineKeyboardMarkup(row_width=2)
    number_column = InlineKeyboardButton(text='Да', callback_data='yes')
    choice_column.insert(number_column)
    number_column = InlineKeyboardButton(text='Нет', callback_data='not')
    choice_column.insert(number_column)
    return choice_column

# def choise_day():
#     choice_column = InlineKeyboardMarkup(row_width=2)
#     for name_column, number_column in zip(excel_method.read_column_header()[:1], range(1, len(excel_method.read_column_header()[1:]))):
#         number_column = InlineKeyboardButton(text=name_column, callback_data=str(number_column))
#         choice_column.insert(number_column)
#     return choice_column

def choice_day(name_iter_column: str):
    choice_column = InlineKeyboardMarkup(row_width=2)
    dataframe = read_all()
    for element, number_element in zip(dataframe[name_iter_column], range(1, len(dataframe[name_iter_column])+1)):
        element = InlineKeyboardButton(text=element, callback_data=str(number_element))
        choice_column.insert(element)
    return choice_column