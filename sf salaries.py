#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df=pd.read_csv("Salaries.csv",low_memory=False)
df


# In[4]:


df.info()


# In[5]:


df.columns=df.columns.str.strip()


# In[8]:


df["EmployeeName"]=df["EmployeeName"].str.lower()
df["JobTitle"]=df["JobTitle"].str.lower()
df


# In[9]:


df.info()


# In[13]:


df["BasePay"]=pd.to_numeric(df["BasePay"],errors="coerce")
df["OvertimePay"]=pd.to_numeric(df["OvertimePay"],errors="coerce")
df["OtherPay"]=pd.to_numeric(df["OtherPay"],errors="coerce")
df["Benefits"]=pd.to_numeric(df["Benefits"],errors="coerce")
df.info()


# In[15]:


df.isnull().sum()


# In[25]:


df["BasePay"]=df["BasePay"].fillna(0)
df["OvertimePay"]=df["OvertimePay"].fillna(0)
df["OtherPay"]=df["OtherPay"].fillna(0)
df["Benefits"]=df["Benefits"].fillna(0)
df["Status"]=df["Status"].fillna("unknown")
df


# # Average for basepay

# In[28]:


df["BasePay"].mean()


# # The highest paid employee

# In[29]:


df['TotalPayBenefits'].max()


# In[31]:


MaxEm=df["TotalPayBenefits"]==df['TotalPayBenefits'].max()


# In[36]:


df[MaxEm][["EmployeeName","TotalPayBenefits"]]


# In[ ]:




