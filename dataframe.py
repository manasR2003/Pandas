import pandas as pd
d={
    'Name':['Manas','Ranjan','Hota'],
    'Age':[22,33,44],
    'ID':[101,102,103]
}
#df=pd.DataFrame(d)
df=pd.DataFrame(d,index=['a','b','c'])
print(df.loc[['b','c']])
print(df.to_string())