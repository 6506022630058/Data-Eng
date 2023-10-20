import pandas as pd
import numpy as np
from numpy.random import randn

data = np.array([[1,2,3],[4,5,6]])
r = np.array(['r1','r2'])
c = np.array(['c1','c2','c3'])
df = pd.DataFrame(data,index=r,columns=c)
print(df)

print('-'*50)

arr = randn(5,4)
df = pd.DataFrame(arr,index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)
print('-'*50)
print(df[['W','X']])

print('-'*50)
df['new'] = df['W'] + df['Y']
print(df)

print('-'*50)
df2 = df.drop('new',axis=1)
print(df2)

print('-'*50)

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl',
                  'Sarah'],'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
print(df)
by_comp = df.groupby('Company')
print('-'*50)
print(by_comp.mean('Company'))

print('-'*50)

long_series = pd.Series(np.random.randn(1000))
print(long_series.head())
print('-'*50)
print(long_series.tail())