import pandas as pd

def search (file, category):
    #Open the file and read the contents
    with open(file, encoding='utf-8') as f:
        lines = f.read()
        
        if category == visualisation:
            #Search for key words in the file
            for word in category:
                category_dict = { word: lines.count(word) }
                visualisation_count.append(category_dict)
        elif category == tech:
            #Search for key words in the file
            for word in category:
                category_dict = { word: lines.count(word) }
                tech_count.append(category_dict)
        elif category == packages:
            #Search for key words in the file
            for word in category:
                category_dict = { word: lines.count(word) }
                packages_count.append(category_dict)
        elif category == analytical:
            #Search for key words in the file
            for word in category:
                category_dict = { word: lines.count(word) }
                analytical_count.append(category_dict)
        else:
            print('Category not found')
            
    return


visualisation_count = []
tech_count = []
packages_count = []
analytical_count = []

visualisation = ['Power BI', 'Excel', 'Tableau', 'GitHub', 'Jira', 'Azure', 'AWS', 'Jenkins',
                  'Microsoft Azure', 'Azure', 'Alteryx','Qlik', 'DevOps', 'Dockers', 'Openstack', 'GCP',
                  'Kafka', 'PostgreSQL', 'ElasticSearch', 'Lucene', 'Kibana', 'Crystal Reports',
                  'Teradata', 'Oracle', 'DB2','MSSQL', 'MS SQL', 'RDBMS', 'MySQL', 'NoSQL', 'Google Cloud',
                  'Spotfire']

tech = ['SQL', ' R ', 'SAS', 'Java', ' C# ', 'C++', 'Scala', 'Shell', 'Javascript', 'Matlab',
              'HTML', 'Ruby', 'Python', 'Matlab', 'PHP', 'DAX', ' M ', 'Machine Learning',
              'SPSS', 'Artificial Intelligence']

packages = ['Matplotlib', 'Pandas', 'Numpy', 'Tensorflow', 'plotly', 'Spark', 'Tidyverse', 'Hive', 'Presto']

analytical = ['ETL', 'Relational Databases','Statistics', 'Data Modeling', 'Data Management',
              'Data Visualisation', 'Business Intelligence', 'Computer Science', 'Data Mining', 
              'Data Warehousing','CRM']


search('All Files.txt', visualisation)
search('All Files.txt', tech)
search('All Files.txt', packages)
search('All Files.txt', analytical)

#Replace null values with zero's
df_visualisation = pd.DataFrame(visualisation_count).fillna(0)
df_tech = pd.DataFrame(tech_count).fillna(0)
df_packages = pd.DataFrame(packages_count).fillna(0)
df_analytical = pd.DataFrame(analytical_count).fillna(0)

#Clean and total the data
#df_visualisation = df_visualisation.drop('Unnamed: 0', 1)
df_visualisation = df_visualisation.sum()

#df_tech = df_tech.drop('Unnamed: 0', 1)
df_tech = df_tech.sum()

#df_packages = df_packages.drop('Unnamed: 0', 1)
df_packages = df_packages.sum()

#df_analytical = df_analytical.drop('Unnamed: 0', 1)
df_analytical = df_analytical.sum()

df_visualisation.to_csv('Visualisation Key Words.csv')
df_tech.to_csv('Technology Key Words.csv')
df_packages.to_csv('Packages Key Words.csv')
df_analytical.to_csv('Analytical Key Words.csv')















# =============================================================================
#                 if lines.count(word) > 0:
#                     print(f"Word '{word}' appeared {lines.count(word)} time/s.")
# =============================================================================




#Categorise Data Scraped
# =============================================================================
# 
# tech = df[['SQL', ' R ', 'SAS', 'Java', ' C# ', 'Scala', 'Shell', 'Javascript', 'Matlab',
#              'html', 'Ruby' 'Python', 'Matlab', 'PHP', 'DAX', ' M ', 'Machine Learning', 'Oracle']]
# 
# visualisation = df[['Power BI', 'Excel', 'Tableau', 'GitHub', 'Jira', 'Azure', 'AWS', 'Jenkins',
#                  'Microsoft Azure', 'Azure', 'Alteryx','Qlik','DevOps']]
# 
# packages = df[['Matplotlib', 'Pandas', 'Tensorflow', 'plotly', 'Spark', 'Tidyverse']]
# 
# analytical = df[['ETL', 'Relational Databases','Statistics', 'Data Modeling', 'Data Management',
#              'Data Visualisation', 'Business Intelligence', 'Computer Science', 'Data Mining', 
#              'Data Warehousing','CRM']]
# 
# all_data = df[['SQL', ' R ', 'SAS', 'Java', ' C# ', 'Scala', 'Shell', 'Javascript', 'Matlab',
#         'html', 'Ruby' 'Python', 'Matlab', 'PHP', 'DAX', ' M ', 'Machine Learning', 'Oracle',
#         'Power BI', 'Excel', 'Tableau', 'GitHub', 'Jira', 'Azure', 'AWS', 'Jenkins',
#         'Microsoft Azure', 'Azure', 'Alteryx','Qlik','DevOps',
#         'Matplotlib', 'Pandas', 'Tensorflow', 'plotly', 'Spark', 'Tidyverse',
#         'ETL', 'Relational Databases','Statistics', 'Data Modeling', 'Data Management',
#         'Data Visualisation', 'Business Intelligence', 'Computer Science', 'Data Mining', 
#         'Data Warehousing','CRM']]
# =============================================================================









#(?i)

#total = df.sum()
#df.loc["Total"] = df.sum()
#df.append(df.sum().rename('Total'))
