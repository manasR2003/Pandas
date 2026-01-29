import pandas as pd

df=pd.read_csv('data2.csv')

new_data=df.dropna()  #if you want to make changes in original dataframe then we have to use "inplace=True"

#print(new_data)

new_data2=df.fillna('Default')  #if you want to make changes in original dataframe then we have to use "inplace=True"

#print(new_data2)

#for perticular column value

new_data3=df.fillna({'name':'MANAS RANJAN','email':'No Email'})

#print(new_data3)

# Using mean(), median() and mode()

x=df['salary'].mean()
#print(x)
new_data4=df.fillna({'salary':x})
#print(new_data4)

y=df['salary'].median()
#print(y)
new_data5=df.fillna({'salary':y})
#print(new_data5)

z=df['salary'].mode()[0]
new_data6=df.fillna({'salary':z})
print(new_data6)

