import pandas as pd

df1 = pd.read_csv('href 1-10p 1-55.txt')
df2 = pd.read_csv('href 1-10p 56-104.txt')
df3 = pd.read_csv('href 1-10p 104-154.txt')
df4 = pd.read_csv('href 1-10p 155-164.txt')
df5 = pd.read_csv('href 11-20p 1-49.txt')
df6 = pd.read_csv('href 11-20p 50-99.txt')
df7 = pd.read_csv('href 11-20p 100-149.txt')
df8 = pd.read_csv('href 21-31p 1-50.txt')
df9 = pd.read_csv('href 21-31p 50-100.txt')
df10 = pd.read_csv('href 21-31p 101-149.txt')
df11 = pd.read_csv('href 21-31p 150-179.txt')

pdList = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11]  # List of your dataframes
new_df = pd.concat(pdList)

new_df.to_csv('All Files.txt')