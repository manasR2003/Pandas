import pandas as pd

df=pd.read_csv('data3.csv')


for x in df.index:
    if df.loc[x,'Duration']>120:
        print(df.loc[x])
for x in df.index:
    if df.loc[x,'Duration']>120:
        df.loc[x,'Duration']=25
print(df.to_string())

#drop rows
for x in df.index:
    if df.loc[x,'Duration']>45:
        df.drop(x,inplace=True)
print(df.to_string())