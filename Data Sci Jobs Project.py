#!/usr/bin/env python
# coding: utf-8

# # About Dataset
# ###### work_year: The year in which the data was recorded. This field indicates the temporal context of the data, important for understanding salary trends over time.
# 
# ###### job_title: The specific title of the job role, like 'Data Scientist', 'Data Engineer', or 'Data Analyst'. This column is crucial for understanding the salary distribution across various specialized roles within the data field.
# 
# ###### job_category: A classification of the job role into broader categories for easier analysis. This might include areas like 'Data Analysis', 'Machine Learning', 'Data Engineering', etc.
# 
# ###### salary_currency: The currency in which the salary is paid, such as USD, EUR, etc. This is important for currency conversion and understanding the actual value of the salary in a global context.
# 
# ###### salary: The annual gross salary of the role in the local currency. This raw salary figure is key for direct regional salary comparisons.
# 
# ###### salary_in_usd: The annual gross salary converted to United States Dollars (USD). This uniform currency conversion aids in global salary comparisons and analyses.
# 
# ###### employee_residence: The country of residence of the employee. This data point can be used to explore geographical salary differences and cost-of-living variations.
# 
# ###### experience_level: Classifies the professional experience level of the employee. Common categories might include 'Entry-level', 'Mid-level', 'Senior', and 'Executive', providing insight into how experience influences salary in data-related roles.
# 
# ###### employment_type: Specifies the type of employment, such as 'Full-time', 'Part-time', 'Contract', etc. This helps in analyzing how different employment arrangements affect salary structures.
# 
# ###### work_setting: The work setting or environment, like 'Remote', 'In-person', or 'Hybrid'. This column reflects the impact of work settings on salary levels in the data industry.
# 
# ###### company_location: The country where the company is located. It helps in analyzing how the location of the company affects salary structures.
# 
# ###### company_size: The size of the employer company, often categorized into small (S), medium (M), and large (L) sizes. This allows for analysis of how company size influences salary.

# In[51]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import plotly.express as px 
import seaborn as sns
from plotly.offline import iplot , plot 
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings("ignore")


# # Import Libraries and Load the dataset
# ## Check the data as well

# In[2]:


df = pd.read_csv(r"D:\BUSINESS ANALYSIS\GIT HUB PROJECTS\Data SCI jobs\jobs_in_data.csv")


# In[3]:


df.sample(5)


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[7]:


print(f"Number of Row : {df.shape[0]}\nNumber of Columns : {df.shape[1]}")


# In[8]:


# Check NaN Value
df.isna().sum()


# In[9]:


# Describe Numiric Data
df.describe().iloc[:,:2]


# In[11]:


# Describe all Data
df.describe(exclude=np.number)


# In[12]:


pd.DataFrame({'Count':df.shape[0],
              'Null':df.isnull().sum(),
              'Null %':df.isnull().mean() * 100,
              'Cardinality':df.nunique()
})


# In[13]:


# Check Duplicated rows
df.duplicated().any()


# # Clean Dataset And Getting Info again

# In[15]:


df.drop(['salary','company_location'],axis=1,inplace=True)


# In[16]:


# Delete Duplicated
df.drop_duplicates(inplace=True)


# In[17]:


# Check Duplicated rows
df.duplicated().any()


# In[18]:


print(f"Number of Row : {df.shape[0]}\nNumber of Columns : {df.shape[1]}")


# In[19]:


df.info() #Check the info again


# In[20]:


# Describe Numiric Data
df.describe().iloc[:,:2]


# In[21]:


# Describe all Data
df.describe(exclude=np.number)


# In[22]:


pd.DataFrame({'Count':df.shape[0],
              'Null':df.isnull().sum(),
              'Null %':df.isnull().mean() * 100,
              'Cardinality':df.nunique()
})


# In[23]:


df.sample(5)


# # Work Year

# In[24]:


print(f"Top Year for Number of Employees '{df['work_year'].value_counts().idxmax()}' with value '{df['work_year'].value_counts().max()}'")
print(f"Least Year for Number of Employees '{df['work_year'].value_counts().idxmin()}' with value '{df['work_year'].value_counts().min()}'")


# In[25]:


iplot(px.line(x = df['work_year'].value_counts().index,
              y = df['work_year'].value_counts().values,
              markers=True,
              labels={'x':'Year','y':'Number of Employees'},
              title='Years of Work',
              line_shape="linear",
              color_discrete_sequence=['#cc2114'],
              template='plotly_dark'
              ))


# # Job Title

# In[26]:


df_job_title_USD = df.groupby('job_title')['salary_in_usd'].sum()


# In[27]:


print(f"Top Year for Number of Employees '{df_job_title_USD.idxmax()}' with Salary '{df_job_title_USD.max()}'")
print(f"Least Year for Number of Employees '{df_job_title_USD.idxmin()}' with Salary '{df_job_title_USD.min()}'")


# In[28]:


iplot(px.bar(df_job_title_USD.sort_values(ascending=False)[:10],
             orientation='h',
             labels={'value':'Salary in USD','job_title':'Job Title'},
             title='Job Title with Salaries USD',
             template='plotly_dark',
             color=df_job_title_USD.index[:10],
             text_auto=True
))


# # Job Category In General

# In[29]:


df_job_category_general = df['job_category'].value_counts()
df_job_category_general


# In[30]:


print(f"Top Job in Needed in 4 Years ago '{df_job_category_general.idxmax()}' with Value '{df_job_category_general.max()}'")
print(f"Least Job in Needed in 4 Years ago '{df_job_category_general.idxmin()}' with Value '{df_job_category_general.min()}'")


# In[31]:


iplot(px.bar(df_job_category_general,
                 labels={'job_category':'Job Category'},
                 title=f"Needed of Jobs Category in 4 Years ago",
                 color_discrete_sequence=['#b3079c'],
                 template='plotly_dark',
                 text_auto=True
))


# # Job Category In Each Year

# In[32]:


df_job_category = df.groupby('work_year')['job_category'].value_counts()


# In[33]:


colors = ['#ccaa14','#8807b3','#07b324','#1007b3']
j = 0
for i in range(2020,2024):
    iplot(px.bar(df_job_category.get(i),
                 labels={'job_category':'Job Category','value':'Number of Employees'},
                 title=f"Needed of Jobs Category in {i}",
                 color_discrete_sequence=[colors[j]],
                 template='plotly_dark',
                 text_auto=True
                 ))
    j+=1


# # Salary Currency

# In[34]:


df_salary_currency = df['salary_currency'].value_counts()


# In[35]:


print(f"Most Prefered Currency is '{df_salary_currency.idxmax()}'")


# In[36]:


iplot(px.bar(df_salary_currency,
             template='plotly_dark',
             labels={'salary_currency':'Salary Currency','value':'Value'},
             title='Most Prefered Currency',
             text_auto=True,
             color_discrete_sequence=['#cce60e']

             ))


# # Salary in USD

# In[37]:


df_salary_in_usd = df.groupby(['work_year','job_title'])['salary_in_usd'].mean()


# In[38]:


colors = ['#4a289b', '#a53d3d', '#268e7e', '#e60e0e']
j = 0
for i in range(2020,2024):
    iplot(px.bar(df_salary_in_usd.get(i)[:10],
                 labels={'job_title':'Job Title','value':'Mean of Salary'},
                 title=f"Mean Salary of Jobs for Year in {i}",
                 color_discrete_sequence=[colors[j]],
                 template='plotly_dark',
                 text_auto=True,
                 orientation='h'
                 ))
    j+=1


# # Employee Residence

# In[39]:


df_employee_residence = df['employee_residence'].value_counts()


# In[40]:


print(f"Top Country is '{df_employee_residence.idxmax()}' with value '{df_employee_residence.max()}'")
print(f"Least Country is '{df_employee_residence.idxmin()}' with value '{df_employee_residence.min()}'")


# In[41]:


iplot(px.bar(df_employee_residence[:10],
             template='plotly_dark',
             labels={'employee_residence':'Name of Country','value':'Value'},
             title='Top Country in the World in Data Science',
             text_auto=True,
             color_discrete_sequence=['#dd0be0'],
))


# In[42]:


iplot(px.scatter_geo(df, 
                     locations='employee_residence',
                     locationmode='country names',
                     color='salary_in_usd',
                     hover_name='employee_residence',
                     title='Salary by Employee Residence',                    
))


# # Experience Level

# In[43]:


df_experience_level = df['experience_level'].value_counts()


# In[44]:


iplot(px.pie(values=df_experience_level.values,
             names=['Senior','Mid-level','Entry-level','Executive'],
             title='Experience Level for Data Analysts'
).update_traces(textinfo='percent+label'))


# # Employment Type
# 

# In[45]:


df_employment_type = df['employment_type'].value_counts()


# In[46]:


iplot(px.bar(df_employment_type,
             template='plotly_dark',
             labels={'employment_type':'Employment Type','value':'Value'},
             title='Type of Employment for Data Analysts',
             text_auto=True,
             color_discrete_sequence=['#dd0be0'],
))


# # Work Setting
# 

# In[47]:


df_work_setting = df['work_setting'].value_counts()


# In[48]:


iplot(px.pie(values=df_work_setting.values,
             names=['In-person','Remote','Hybrid'],
             title='Type of Work Setting',
).update_traces(textinfo='percent+label'))


# # Company Size

# In[49]:


df_company_size = df['company_size'].value_counts()


# In[50]:


iplot(px.pie(values=df_company_size.values,
             names=['M','L','S'],
             title='Size of Company',
).update_traces(textinfo='percent+label'))


# # Thank You
