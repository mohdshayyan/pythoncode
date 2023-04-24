'''Write a Pandas program to insert a new column in existing
DataFrame.'''
import pandas as pd
import numpy as np
exam_data = {'name': ['Manish', 'Dhiraj','Man', 'Dhir'],\
 'score': [12.5, 91,20.5, 19]}
df = pd.DataFrame(exam_data )
medium = ['english','hindi','hindi','english']
df['Medium'] = medium
print("\nNew DataFrame after inserting the 'medium' column")
print(df)
