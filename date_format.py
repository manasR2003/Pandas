import pandas as pd

df=pd.read_csv('data3.csv')

df['Date']=pd.to_datetime(df['Date'],format='mixed')
df.dropna(subset=['Date'],inplace=True)

print(df.to_string())