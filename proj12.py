'''Write a Pandas program to rename columns of a given DataFrame.'''
import pandas as pd
import numpy as np
exam_data = {'name': ['Manish', 'Dhiraj','Man', 'Dhir'],\
 'score': [12.5, 91,20.5, 19]}
df = pd.DataFrame(exam_data )
df = df.rename(columns={'name': 'NAME', 'score': 'SCORE'})
print("New DataFrame after renaming columns:")
print(df)
