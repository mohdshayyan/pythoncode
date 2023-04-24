'''Write a Pandas program to select the rows the score is between 15
and 20 (inclusive)'''
import pandas as pd
import numpy as np
exam_data = {'name': ['Manish', 'Dhiraj','Man', 'Dhir'],
 'score': [12.5, 91,20.5, 19]}
df = pd.DataFrame(exam_data )
print(df)
print("Rows where score between 15 and 20 (inclusive):")
print(df[df['score'].between(15, 20)])

