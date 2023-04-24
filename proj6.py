'''Write a Pandas program to get the first 3 rows of a given
DataFrame.'''
import pandas as pd
import numpy as np
exam_data = {'name': ['Manish', 'Dhiraj','Man', 'Dhir'],
 'score': [12.5, 91,2.5, 9]}
df = pd.DataFrame(exam_data )
print(df)
print("First three rows of the data frame:")
print(df.iloc[:3])
#or we can use following to get first 3 rows of DataFrame
#print(df.head(3))

