'''Write a Pandas program to create and display a DataFrame from a
specified dictionary with index labels.'''
import pandas as pd
import numpy as np
exam_data = {'name': ['Manish', 'Dhiraj'],
 'score': [12.5, 9]}
labels = ['NAME', 'SCORE']
df = pd.DataFrame(exam_data , index=labels)
print(df)
