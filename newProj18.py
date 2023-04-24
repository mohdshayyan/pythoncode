import pandas as pd
dt=({'English':[74,79,48,53,68],
         'Physics':[76,78,80,76,73],
         'Chemistry':[57,74,55,89,70],
         'Biology':[76,85,63,68,59],
         'IP':[82,93,69,98,79]})
df=pd.DataFrame(dt, index=['Akshit','Bharat','Chetan','Dhaval','Gaurang'])
df.drop(index='Chetan',inplace=True)
df.drop(['Dhaval','Gaurang'],inplace=True)

print(df)

