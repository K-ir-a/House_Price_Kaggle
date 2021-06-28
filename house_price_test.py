#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#Reading data from using panda
test_df= pd.read_csv("house_price_test.csv")


# In[3]:


#First five column from Dataset
test_df.head()


# In[4]:


#Show the sum of null values a column contain
test_df.isnull().sum()


# In[5]:


#To use if above query doesn't show all rows
obj1 = test_df.isnull().sum()
for key,value in obj1.iteritems():
    print(key," ", value)


# In[6]:


#Shows null values in pictorial form
sns.heatmap(test_df.isnull(), yticklabels=False, cbar=False)


# In[ ]:


#Missing values of columns are handled.
#Mean() is used for numeric values and Mode() is used for object values
#Drop command is used to drop the whole column in which missing values are more than 50%


# In[7]:


test_df['LotFrontage'] = test_df['LotFrontage'].fillna(test_df['LotFrontage'].mean())


# In[8]:


test_df['MSZoning'] = test_df['MSZoning'].fillna(test_df['MSZoning']).mode()[0]


# In[9]:


test_df.drop('Alley',axis=1, inplace=True)


# In[10]:


test_df.shape


# In[11]:


test_df['Utilities'] = test_df['Utilities'].fillna(test_df['Utilities']).mode()[0]


# In[12]:


test_df['Exterior1st'] = test_df['Exterior1st'].fillna(test_df['Exterior1st']).mode()[0]
test_df['Exterior2nd'] = test_df['Exterior2nd'].fillna(test_df['Exterior2nd']).mode()[0]


# In[13]:


test_df['MasVnrType'] = test_df['MasVnrType'].fillna(test_df['MasVnrType']).mode()[0]
test_df['MasVnrArea'] = test_df['MasVnrArea'].fillna(test_df['MasVnrArea']).mean()
test_df['BsmtFinType1']= test_df['BsmtFinType1'].fillna(test_df['BsmtFinType1']).mode()[0]
test_df['BsmtFinType2']= test_df['BsmtFinType2'].fillna(test_df['BsmtFinType2']).mode()[0]


# In[14]:


test_df['BsmtCond'] = test_df['BsmtCond'].fillna(test_df['BsmtCond']).mode()[0]
test_df['BsmtQual'] = test_df['BsmtQual'].fillna(test_df['BsmtQual']).mode()[0]
test_df['BsmtExposure'] =test_df['BsmtExposure'].fillna(test_df['BsmtExposure'].mode()[0])


# In[15]:


test_df['BsmtFinSF1'] = test_df['BsmtFinSF1'].fillna(test_df['BsmtFinSF1'].mean())
test_df['BsmtFinSF2'] = test_df['BsmtFinSF2'].fillna(test_df['BsmtFinSF2'].mean())
test_df['BsmtUnfSF'] = test_df['BsmtUnfSF'].fillna(test_df['BsmtUnfSF'].mean())
test_df['TotalBsmtSF'] = test_df['TotalBsmtSF'].fillna(test_df['TotalBsmtSF'].mean())
test_df['BsmtFullBath'] = test_df['BsmtFullBath'].fillna(test_df['BsmtFullBath'].mean())
test_df['BsmtHalfBath'] = test_df['BsmtHalfBath'].fillna(test_df['BsmtHalfBath'].mean())          


# In[16]:


test_df['KitchenQual']= test_df['KitchenQual'].fillna(test_df['KitchenQual']).mode()[0]
test_df['Functional']= test_df['Functional'].fillna(test_df['Functional']).mode()[0]


# In[17]:


test_df['FireplaceQu']= test_df['FireplaceQu'].fillna(test_df['FireplaceQu']).mode()[0]
test_df['GarageType']= test_df['GarageType'].fillna(test_df['GarageType']).mode()[0]
test_df['GarageFinish']= test_df['GarageFinish'].fillna(test_df['GarageFinish']).mode()[0]


# In[18]:


test_df.drop(['GarageYrBlt'],axis=1,inplace=True)


# In[19]:


test_df['GarageCars'] = test_df['GarageCars'].fillna(test_df['GarageCars'].mean()) 
test_df['GarageArea'] = test_df['GarageArea'].fillna(test_df['GarageArea'].mean()) 


# In[20]:


test_df['GarageCond'] = test_df['GarageCond'].fillna(test_df['GarageCond']).mode()[0]
test_df['GarageQual'] = test_df['GarageQual'].fillna(test_df['GarageQual']).mode()[0]


# In[21]:


test_df.drop(['PoolQC','Fence','MiscFeature'],axis=1,inplace=True)


# In[22]:


test_df['SaleType'] = test_df['SaleType'].fillna(test_df['SaleType']).mode()[0]


# In[23]:


test_df.drop(['Id'],axis=1,inplace=True)


# In[24]:


#shows the shape i.e (rows ,columns)
test_df.shape


# In[26]:


# As we can see all missing values are handled properly
sns.heatmap(test_df.isnull(), yticklabels=False, cbar=False)


# In[25]:


#Shows the datatype of variables
test_df.info()


# In[63]:


#We have converted our file into 'CorrectedTest.csv' to use in Fianl code.
test_df.to_csv('CorrectedTest.csv', index=False)


# In[ ]:




