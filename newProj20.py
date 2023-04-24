import pandas as pd
stu_XII={'Name':['Abhay','Bharat','Chandu','Dharmik','Ervin'],
             'Eng':[66,69,75,74,70],'Maths':[85,82,84,80,75],'IP':[95,82,63,84,90]}
df=pd.DataFrame(stu_XII)
df.loc[5]=['Manisha',67,89,45]
df.loc[6]=['Hemant',77,88,66]
print(df)
