import pandas as pd
df=pd.read_csv('data.csv')
print(df.head())  #it will print first 5rows because of default value from the top.
print(df.head(10))  #it will print based on the arguments from the top.

print(df.tail())  #it will print from the last 5 rows as default.
print(df.tail(10)) #it will print rows from the last based on the arguments.

print(df.info())