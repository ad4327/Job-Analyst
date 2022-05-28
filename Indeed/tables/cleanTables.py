import pandas as pd

df = pd.read_csv('../html text/href 1-55')
df2 = pd.read_csv('../html text/href 56-104')

print(df)


# =============================================================================
# def clean_data(file):
#     df = pd.read_csv(file)
#     
#     df = df.drop('Unnamed: 0', 1)
#     df = df.sum()
#     
#     return df
#     
# 
# clean_data('Visualisation Key Words.csv')
# df = pd.DataFrame()
# =============================================================================
#df.to_csv('visual_keyword_fix.csv')