import pandas as pd

#d=['A','B','C','D','E','F','G','H']
#s=pd.Series(d)
#s=pd.Series(d,index=[10,20,30,40,50,60,70,80])
# print(s)
# print(s[20])
# print(s[[20,30,40]])

d={'S1':'Manas','S2':'Ranjan','S3':'Hota','S4':'Laxmipriya','S5':'Das'}
students=pd.Series(d)
students2=pd.Series(d,index=['S1','S4'])
print(students)
print(students2)
print(students2['S1'])
print(students[['S1','S4']])
