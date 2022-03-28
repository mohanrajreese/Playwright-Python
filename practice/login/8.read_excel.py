from pandas import DataFrame
import pandas as pd
open_file = pd.read_excel('data.xlsx', sheet_name=0)
df = list(open_file['Country'])
print(df)