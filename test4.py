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

df['new'] = df['W'] + df['Y']
print(df)

df2 = df.drop('new',axis=1)
print(df2)

print('-'*50)

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl',
                  'Sarah'],'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
print(df)