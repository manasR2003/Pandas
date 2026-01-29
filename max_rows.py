import pandas as pd
print(pd.options.display.max_rows)

#pd.options.display.max_rows=70      ----> it will print first and last 5 rows because that max rows is 70 but in csv file there is more than 70.
pd.options.display.max_rows=100  #it will print all the rows because in csv file there is less than 100 rows
df=pd.read_csv('data.csv')
print(df)