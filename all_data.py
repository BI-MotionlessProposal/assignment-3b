from osmread import parse_file, Node
import pandas as pd
import numpy as np

complete_data = './boliga_all.csv'
df = pd.read_csv(complete_data)
df.head()
df[['price']].head()
data = [df.zip_code,df.price,df.sell_date]

df2 = pd.DataFrame({'sell_date': df.sell_date, 'zip_code': df.zip_code, 'price': df.price},
                  columns=['sell_date', 'zip_code', 'price'])
df2.head()
print(df2)