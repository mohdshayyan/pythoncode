import pandas as pd

# Read CSV file into a DataFrame
df = pd.read_csv('input.csv')

# Display the contents of the DataFrame
print("Original DataFrame:")
print(df)

# Perform operations on the data
# For example, let's calculate the sum of the 'Marks' column
total_marks = df['Marks'].sum()
print("Total Marks:", total_marks)

# Add a new column to the DataFrame
df['Grade'] = ['A' if mark >= 80 else 'B' if mark >= 60 else 'C' if mark >= 40 else 'D' for mark in df['Marks']]

# Write the modified DataFrame to a new CSV file
df.to_csv('output.csv', index=False)

# Display the modified DataFrame
print("\nModified DataFrame:")
print(df)
