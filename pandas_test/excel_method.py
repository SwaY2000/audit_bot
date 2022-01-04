import pandas as pd

def create_list_excel(days: int, name_list: str='sheet_name'):
    print(name_list)
    days = int(days)
    with pd.ExcelWriter('excel_py.xlsx', mode='a', if_sheet_exists='replace', engine='openpyxl') as writer:
        test_excel = pd.DataFrame({'Дата': [f'{day} день' for day in range(1, days+1)],
                                   'Объем партии': [0 for _ in range(1, days+1)],
                                   'Комментарий для \"Объем партии\"': ['-' for _ in range(1, days + 1)],
                                   'Цена за партию': [0 for _ in range(1, days+1)],
                                   'Комментарий для \"Цена за партию\"': ['-' for _ in range(1, days + 1)],
                                   'Сумма за выход': [0 for _ in range(1, days+1)],
                                   'Комментарий для \"Сумма за выход\"': ['-' for _ in range(1, days + 1)],
                                   'Затраты производство и коммунальные': [0 for _ in range(1, days+1)],
                                   'Комментарий для \"Затраты производство и коммунальные\"': ['-' for _ in range(1, days + 1)],
                                   'З/п сотрудников': [0 for _ in range(1, days + 1)],
                                   'Комментарий для \"З/п сотрудников\"': ['-' for _ in range(1, days + 1)],
                                   'Обслуживание и ремонт оборудования': [0 for _ in range(1, days + 1)],
                                   'Комментарий для \"Обслуживание и ремонт оборудования\"': ['-' for _ in range(1, days + 1)],
                                   'Оборудования': [0 for _ in range(1, days + 1)],
                                   'Комментарий для \"Оборудования\"': ['-' for _ in range(1, days + 1)],
                                   'Склад': [0 for _ in range(1, days + 1)],
                                   'Комментарий для \"Склад\"': ['-' for _ in range(1, days + 1)],
                                   'Остаток': [0 for _ in range(1, days + 1)],
                                   'Комментарий для \"Остаток\"': ['-' for _ in range(1, days + 1)],
                                   }).set_index('Дата', drop=False)
        test_excel.to_excel(writer, sheet_name=name_list, index=False)
        print(test_excel)
        writer.save()
        return

def read_column_header(name_list: str='sheet_name'):
    """This is method for read header column and delete in datafreame column 'Comment'"""
    with pd.ExcelWriter('excel_py.xlsx', mode='a', if_sheet_exists='replace', engine='openpyxl') as writer:
        change_cell = pd.read_excel(writer, sheet_name=name_list, engine='openpyxl')
        change_cell = change_cell.columns.tolist()
        for header in change_cell:
            if header[:11] == 'Комментарий':
                change_cell.remove(header)
        writer.save()
    return change_cell

def read_column_header_comment(header_column: str, name_list: str='sheet_name'):
    """This is method for read header column and delete in datafreame column 'Comment'"""
    with pd.ExcelWriter('excel_py.xlsx', mode='a', if_sheet_exists='replace', engine='openpyxl') as writer:
        change_cell = pd.read_excel(writer, sheet_name=name_list, engine='openpyxl')
        change_cell = change_cell.columns.tolist()
        print(change_cell)
        for header in change_cell:
            if header == f'Комментарий для "{header_column}"':
                header_column = f'Комментарий для "{header_column}"'
                writer.save()
                return header_column
        writer.save()
    raise ValueError(f'This is column not found "Комментарий для "{header_column}"')

def change_cell(y_cell: int, x_cell, sequence, name_list: str='sheet_name'):
    """This is method create for change cell with help pandas"""
    with pd.ExcelWriter('excel_py.xlsx', mode='a', if_sheet_exists='replace', engine='openpyxl') as writer:
        change_cell = pd.read_excel(writer, sheet_name=name_list, engine='openpyxl').set_index(read_column_header()[0], drop=False)
        change_cell.loc[f'{y_cell} день', x_cell] = sequence
        change_cell.to_excel(writer, sheet_name=name_list, index=False)
        writer.save()
        print('Change saved')
        writer.save()
        return

def read_all(name_list: str='sheet_name'):
    """This is method create for change cell with help pandas"""
    with pd.ExcelWriter('excel_py.xlsx', mode='a', if_sheet_exists='replace', engine='openpyxl') as writer:
        change_cell = pd.read_excel(writer, sheet_name=name_list, engine='openpyxl').set_index(read_column_header()[0], drop=False)
        writer.save()
        return change_cell