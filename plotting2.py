import pandas as pd

import matplotlib.pyplot as plt

df=pd.read_csv('data4.csv')
df.plot(kind='scatter', x='Duration', y='Pulse')
plt.title('graph of pandas')
plt.show()

df['Duration'].plot(kind='hist')
plt.show()