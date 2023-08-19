#!/usr/bin/env python
# coding: utf-8

# Q1: Create Your own filter and reduce function same as real filter and
# reduce function?

# In[1]:


from functools import reduce


# In[2]:


def sum(a,b):
    return a+b
list_1=[10,15,25,10,40]
reduce(sum,list_1)


# Q2: Move Files from one folder to another folder. By using Python. And
# create empty files using python.

# In[22]:


import os
def create_empty_files(folder, file_names):
    # Loop through each file name and create an empty file in the folder
    for file_name in file_names:
        # Get the full path of the file
        file_path = os.path.join(folder, file_name)

        # Create an empty file
        open(file_path, 'w').close() 


# Q3: Delete files if the files are present in the folder otherwise pass.

# In[3]:


import os

file_path = r"C:\Users\SUBHAM KUMAR\OneDrive\Documents\anshu programming\area of circle.ipynb"
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("The system cannot find the file specified")


# Q4: Open the Json file and extract the name of the students.

# In[4]:


import json


# In[5]:


import json

with open('task1.json') as f:
    data= json.load(f)
print(data)


# In[6]:


print(json.dumps(data,indent=2))


# In[ ]:





# Q5: Create a class which contains all the above functions and import this
# class for use. (OOPS Concept)

# In[34]:


from functools import reduce

class CustomFunctions:
    def __init__(self, iterable):
        self.iterable = iterable
    
    def custom_filter(self, func):
        filtered_list = []
        for item in self.iterable:
            if func(item):
                filtered_list.append(item) 
        return filtered_list

    def custom_reduce(self, func, initial=None):
        iterator = iter(self.iterable)
        if initial is None:
            value = next(iterator)
        else:
            value = initial
        for item in iterator:
            value = func(value, item)
        return value


# In[35]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
custom_functions = CustomFunctions(numbers)

# Use custom_filter() method
filtered_numbers = custom_functions.custom_filter(lambda x: x % 2 == 0)
print(filtered_numbers)

# Use custom_reduce() method
sum_of_numbers = custom_functions.custom_reduce(lambda x, y: x + y)
print(sum_of_numbers)


# In[7]:


# define a class
class Bike:
    name = ""
    gear = 0

# create object of class
bike1 = Bike()

# access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")


# Q6: Scrape mobile name, mobile price and reviews from first 20 page of
# flipkart.

# In[8]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[16]:





# In[35]:


import pandas as pd
import requests
from bs4 import BeautifulSoup



Product_name = []
Prices = []
Description = []
Reviews = []



for i in range(2,12):
    url = "https://www.flipkart.com/search?q=mobiles+5g&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_5_0_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_5_0_na_na_na&as-pos=5&as-type=HISTORY&suggestionId=mobiles+5g%7CMobiles&requestId=a6e8b2d1-caaf-43b6-8967-ac1afc6c4a1a&page="+str(i)
    
    r = requests.get(url)
    
    soup = BeautifulSoup(r.text,"lxml")
    box = soup.find("div",class_="_1YokD2 _3Mn1Gg")
    
    names = box.find_all("div",class_="_4rR01T")
    
    
    for i in names:
        name = i.text
        Product_name.append(name)
        
    prices = box.find_all("div",class_="_30jeq3 _1_WHN1")
    
    for i in prices:
        name = i.text
        Prices.append(name)
        
        
    desc = box.find_all("ul",class_="_1xgFaf")
    
    
    for i in desc:
        name = i.text
        Description.append(name)
        
    reviews = box.find_all("div",class_= "_3LWZlK")
    
    
    for i in reviews:
        name = i.text
        Reviews.append(name)

#print(len(Reviews)


# In[36]:


df = pd.DataFrame({"Product_Name":Product_name,"Prices":Prices,"Description":Description,"Reviews":Reviews})


# In[37]:


df


# In[40]:


df.to_csv("C:/151ND750/filpkart_mobile_review.csv")


# In[4]:


pip install selenium


# In[17]:





# In[ ]:




