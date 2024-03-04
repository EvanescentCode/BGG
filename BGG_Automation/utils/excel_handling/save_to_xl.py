import pandas as pd
from openpyxl.reader.excel import load_workbook


class SaveToXl:
    @staticmethod
    def save_to_xl(data):
        data_path = r'..\..\data\data.xlsx'
        df = pd.DataFrame(data, columns=['Rank', 'Title', 'Link', 'Geek Rating', 'Avg Rating', 'Num Voters'])
        today_date = pd.Timestamp.today().strftime(' %d.%m.%y %H-%M')
        data_workbook = load_workbook(data_path)
        writer = pd.ExcelWriter(data_path, engine='openpyxl', mode='a')
        writer.data_workbook = data_workbook
        df.to_excel(writer, index=False, sheet_name=f'{today_date}')
        writer.close()
