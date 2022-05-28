import requests
from bs4 import BeautifulSoup
import pandas as pd

#Create function to load and parse page using BeautifulSoup
def extract(page):
    print(page)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
    url = f'https://au.indeed.com/jobs?q=data%20analyst&l=Australia&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

#Create function which gets all text information from Indeed using specific search keywords
def transform(soup):
    #Find all information using BeautifulSoup starting from specific classes to get the href link
    divs = soup.find_all('div', class_ = 'slider_container')
    a_tags = soup.find_all('a', class_ = 'jcs-JobTitle', href=True)
    
    #Loop through all text, get the href link and add to a list
    for a_tag_id in a_tags:
        if 'job_' in str(a_tag_id.get('id')):
            href_id = str(a_tag_id.get('id').replace('job_', 'jk='))
            href = "https://au.indeed.com/viewjob?" + href_id
        elif 'sj_' in str(a_tag_id.get('id')):
            href_id = str(a_tag_id.get('id').replace('sj_', 'jk='))
            href = "https://au.indeed.com/viewjob?" + href_id
        else:
            href = "Could not find link"
        
        job = {
            'Href': href
            }
        #Append information to list
        jobhref.append(job)
        #Find title, company name,summary and store information to a list
        for item in divs:
            title = item.find('h2').text.strip()
            company = item.find('span', class_ = 'companyName').text.strip()
            summary = item.find('table', class_ = 'jobCardShelfContainer').text.strip().replace('\n', '')
            
            # Find salary amount and store to a list
            try:
                salary = item.find('div', class_ = 'salary-snippet').text.strip()
            except:
                salary = ''
            #Create job dictionary
            job = {
                    'Title': title,
                    'Company': company,
                    'Salary': salary,
                    'Summary': summary,
                }

            joblist.append(job)
    return


joblist = []
jobhref = []

#Url pages numbers goes up in increments of 10 #TOO CHANGE TO 330
for i in range(210, 330, 10):
    pages = extract(i)
    transform(pages)

#Create and merge pandas dataframes and store into csv file
df = pd.DataFrame(joblist)
df2 = pd.DataFrame(jobhref)
result = pd.merge(df, df2, left_index=True, right_index=True)
print(result)
result.to_csv('jobs21-31pages.csv')