import pandas as pd
import re

meetingStrings = [
    "appointment",
    "meet",
    "interview",
    "NSW"
]

text = "Fix me a meeting in 2 days"

#print(re.split('|'.join(r'(?:\b\w*'+re.escape(w)+r'\w*\b)' for w in meetingStrings), text, 1)[-1])

df = pd.read_csv('locations.csv')

df['State1'] = df['State'].str.split("\s+\(").str[0]

df['State Count'] = df['State'].str.split("\s+\(").str[1]

if df.loc[df['State'].str.contains('NSW')]:
    print('True')
    
else:
    print('fuck')
#print(df['State'])
#print(df['State1'])
#print(df['State Count'])