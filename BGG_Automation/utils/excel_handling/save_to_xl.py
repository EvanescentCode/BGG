import pandas as pd


class SaveToXl:
    @staticmethod
    def save_to_xl(data):
        df = pd.DataFrame(data, columns=['Rank', 'Title', 'Link', 'Geek Rating', 'Avg Rating', 'Num Voters'])
        print(df)
        df.to_excel("C:\\python-selenium\\BGG\\BGG_Automation\\data\\data.xlsx", index=False)
