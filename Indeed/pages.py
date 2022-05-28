# =============================================================================
import pandas as pd
import re
import numpy as np
from bs4 import BeautifulSoup
import requests

# =============================================================================

from requests_html import HTMLSession
import nest_asyncio
import time

#Start Html Session to disguise html bot headers
nest_asyncio.apply()
s = HTMLSession()

#Read CSV file
df = pd.read_csv('jobs21-31pages.csv', sep=',', skiprows=151, nrows=30, names=['Title','Company','Salary','Summary','Href'])

#List of key words to search for
key_words = ['SQL', ' R ', 'SAS', 'Java', ' C# ', 'Scala', 'Shell', 'Javascript', 'Matlab',
            'html', 'Ruby' 'Python', 'Matlab', 'PHP', 'DAX', ' M ', 'Machine Learning', 'Oracle',
            'Power BI', 'Excel', 'Tableau', 'GitHub', 'Jira', 'Azure', 'AWS', 'Jenkins',
            'Microsoft Azure', 'Azure', 'Alteryx','Qlik','DevOps',
            'Matplotlib', 'Pandas', 'Tensorflow', 'plotly', 'Spark', 'Tidyverse',
            'ETL', 'Relational Databases','Statistics', 'Data Modeling', 'Data Management',
            'Data Visualisation', 'Business Intelligence', 'Computer Science', 'Data Mining', 
            'Data Warehousing','CRM']

#Create an empty list to store all the found key words
words = []
total_words = []
count = 0

#Read through url from 'jobs.csv' and scrape pages to find key words
for row in df['Href']:#.head(51):
    time.sleep(3)
    url= row
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    r = s.get(url)
    

    for tag in soup():
        for attribute in ["style"]:
            del tag[attribute]
    ht= r.html.find('#jobDescriptionText', first=True).text #jobDescriptionText .jobsearch-JobComponent
    words = ht
    total_words.append(words)


#Create and merge pandas dataframes and store into csv file
df = pd.DataFrame(total_words)
df.to_csv('href 21-31p 150-179.txt')


















#df.loc["Total"] = df.sum() - FIND TOTAL OF ALL WORDS FOUND (IN PANDAS)

