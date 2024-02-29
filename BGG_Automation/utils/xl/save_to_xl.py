import pandas as pd
import openpyxl


class SaveToXl:
    df = pd.DataFrame([['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3']], index=[1, 2, 3],
                      columns=['A', 'B', 'C'])

    print(df)
