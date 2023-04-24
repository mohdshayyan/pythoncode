'''Write a Pandas program to delete DataFrame row(s) based on given
column value/condition.'''
import pandas as pd
import numpy as np
exam_data = {'name': ['Manish', 'Dhiraj','Man', 'Dhir'],\
 'score': [12.5, 91,20.5, 19]}
df = pd.DataFrame(exam_data )
df = df[df.score >= 20]
print("New DataFrame")
print(df)
