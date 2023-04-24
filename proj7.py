'''Write a Pandas program to count the number of rows and columns
of a DataFrame.'''
import pandas as pd
import numpy as np
exam_data = {'name': ['Manish', 'Dhiraj','Man', 'Dhir'],
 'score': [12.5, 91,2.5, 9]}
df = pd.DataFrame(exam_data )
total_rows=len(df.axes[0])
total_cols=len(df.axes[1])
print("Number of Rows: "+str(total_rows))
print("Number of Columns: "+str(total_cols))
