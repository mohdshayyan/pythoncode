'''Write a Pandas program to sort the DataFrame first by 'name' in
descending order, then by 'score' in ascending order.'''
import pandas as pd
import numpy as np
exam_data = {'name': ['Manish', 'Dhiraj','Man', 'Dhir'],
 'score': [12.5, 91,20.5, 19]}
df = pd.DataFrame(exam_data )
result_sort=df.sort_values(by=['name', 'score'], ascending=[True,
True])
print("Sort the data frame first by ‘name’ in descending order, then\
by ‘score’ in ascending order:")
print(result_sort)
