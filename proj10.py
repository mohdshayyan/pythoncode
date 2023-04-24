'''Write a Pandas program to change the name 'Manish' to 'Anish' in
name column of the data frame.'''
import pandas as pd
import numpy as np
exam_data = {'name': ['Manish', 'Dhiraj','Man', 'Dhir'],\
 'score': [12.5, 91,20.5, 19]}
df = pd.DataFrame(exam_data )
df['name'] = df['name'].replace('Manish', 'Anish')
print(df)
