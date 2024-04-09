import pandas as pd

# Replace 'your_file_path.pkl' with the actual path to your pickle file
file_path = 'data.pkl'

df = pd.read_pickle(file_path)

# Display the first few rows of the DataFrame
print(df.head())
