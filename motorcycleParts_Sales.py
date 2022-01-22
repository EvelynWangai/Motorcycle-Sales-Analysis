#!/usr/bin/env python
# coding: utf-8

# In[24]:


# Importing packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reading the data
df = pd.read_csv('data/sales_data.csv', parse_dates=['date'])

# Take a look at the first datapoints
df.head()


# In[3]:


# QUESTION 1: WHAT ARE THE TOTAL SALES FOR EACH PAYMENT METHOD
df.groupby('payment')[['total']].sum()


# In[4]:


# QUESTION 2: WHAT IS THE AVERAGE UNIT PRICE FOR EACH PRODUCT LINE
df.groupby('product_line')[['unit_price']].mean()


# In[5]:


# QUESTION 3: CREATE PLOTS TO VISUALIZE FINDINGS FOR QUESTION 1
total_sales = df.groupby('payment')[['total']].sum()
total_sales.plot(kind = 'bar')
plt.title("Transfer Method of Payment has the highest Total Sales")
plt.show()


# In[6]:


## QUESTION 3.1: CREATE PLOTS TO VISUALIZE FINDINGS FOR QUESTION 2
avg_unitPrice = df.groupby('product_line')[['unit_price']].mean()
avg_unitPrice.plot(kind = 'bar')
plt.title("Engine is the most expensive part with a Unit Price Average of 60.09")
plt.show()


# In[7]:


#QUESTION 4:Investigate further (e.g., average purchase value by client type, total purchase value by product line, etc.)

#4.1 total purchase value by product line
df.groupby('product_line')[['total']].sum()


# In[9]:


productline_sales = df.groupby('product_line')[['total']].sum()
productline_sales.plot(kind = 'bar')
plt.title("Suspension & Traction parts has the highest number of Sales")
plt.show()


# 4.1 Warehouse sales grouped by the months - Which warehouse had the highest sales

# In[35]:


# Get the month from the date column
df['month'] = df['date'].dt.month


# In[33]:


## What month had the highest sales
df.groupby(['month'])[['total']].sum()


# In[36]:


# distribution of sales across the warehouses
df.groupby(['warehouse'])[['total']].sum()


# In[37]:


#distribution of sales by month in each warehouse
df.groupby(['month','warehouse'])[['total']].sum()


# In[38]:


##Breakdown of each product line sales in each warehouse
sales_table = pd.pivot_table(df, values = 'total', index = ['warehouse'], columns = ['product_line'], aggfunc = np.sum)
sales_table


# In[39]:


## How Many Products were SOLD
df.groupby(['month'])[['quantity']].sum()


# In[40]:


# distribution of quantity sales across the warehouses
df.groupby(['warehouse'])[['quantity']].sum()


# In[67]:


## Product line breakdown by sales and quantity
df.groupby('product_line')[['total', 'quantity']].sum()


# In[68]:


## Breakdown of each product line quantity sales in each warehouse
quantitySales_table = pd.pivot_table(df, values = 'quantity', index = ['warehouse'], columns = ['product_line'], aggfunc = np.sum)
quantitySales_table


# Summary of Findings
# 
# - By Payment Method, Transfer had the highest transactions totaling to 159,642. Cash transactions were the least.
# 
# - In the product lines, the engine is the most expensive part with an average unit price of 60
# 
# - When we look at the total sales of each product line; Suspension & traction parts take the lead with 73K sales
# 
# - If we drill down per month; August has the highest amount of sales (100K) with 3191 products sold followed by June with 95K sales and 3160 products sold. July had the least amount of sales (93K)
# 
# - If we look at warehouses, the Central Warehouse is doing really well. It has the highest total amount of purchases(142K). The West warehouse has the least total amount of purchases(47K)
# 

# In[ ]:




