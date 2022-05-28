# Scrape Indeed Locations
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Create function to load and parse page using BeautifulSoup
def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
    url = f'https://au.indeed.com/jobs?q=data%20analyst&l=Australia&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def location(soup):
    #Find all information using BeautifulSoup from the drop down menu to get the location
    divs = soup.find_all('div', class_ = 'yosegi-FilterPill-pillList')
    
    #Find each state and how many jobs are in each state
    for item in divs:
        location_list = item.find('ul',{'id':'filter-loc-menu'})
        
        for location_item in location_list:
            state = location_item.find('a',{'class':'yosegi-FilterPill-dropdownListItemLink'}).text.strip()
            state_dict = { 'State': state }
            state_list.append(state_dict)
    return
            
def education(soup):
    #Find all information using BeautifulSoup from the drop down menu to get the how many jobs require a degree
    divs = soup.find_all('div', class_ = 'yosegi-FilterPill-pillList')
    
    #Find each education level and how many jobs require which level of education
    for item in divs:
        education_list = item.find('ul',{'id':'filter-taxo1-menu'})
        
        for education_item in education_list:
            degree = education_item.find('a',{'class':'yosegi-FilterPill-dropdownListItemLink'}).text.strip()
            education_dict = { 'Education': degree }
            degree_list.append(education_dict)
    
    return

state_list = []
degree_list = []

#Url pages numbers goes up in increments of 10 #TOO CHANGE TO 330
for i in range(0, 10, 10):
    pages = extract(i)
    location(pages)
    education(pages)
    
#Create pandas dataframes and store into csv file
state_df = pd.DataFrame(state_list)
degree_df = pd.DataFrame(degree_list)

state_df.to_csv('locations.csv')
degree_df.to_csv('degree.csv')






















