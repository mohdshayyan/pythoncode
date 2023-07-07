import pandas as pd
idx=['Physics','Biology','English','Chemistry']
data={'A':[67,89,90,95],'B':[20,50,60,94],'C':[70,80,90,60],'D':[80,90,59,85]}
df=pd.DataFrame(data,index=idx)
print(df)
df.to_csv('Pd')
