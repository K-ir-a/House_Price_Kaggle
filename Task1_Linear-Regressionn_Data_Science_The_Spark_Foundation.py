#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[41]:


#Reading Data From Link
df = pd.read_csv("https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv")


# In[80]:


#Getting the content of dataset
df.head()


# In[43]:


#Shows the (rows, colums) of dataset
df.shape


# In[44]:


#Checks if null value present in dataset
df.isnull().sum()


# In[45]:


#Plotting the distribution of scores
df.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show


# In[46]:


#Preparing the data
X = df.iloc[:,:-1].values
y = df.iloc[:,1].values


# In[57]:


#Here we split the data in test and train sample with 80% data for training and 20% for testing 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# In[67]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print("Training Complete")


# In[68]:


#Plotting the regression line
line = regressor.coef_*X+regressor.intercept_

#plotting for test data 
plt.scatter(x,y)
plt.plot(X, line);
plt.show()


# In[69]:


#Making Prediction
print(X_test) #Testing data 
y_pred = regressor.predict(X_test)#Predicting the score


# In[70]:


predicted_value = pd.DataFrame({"Actual Value" : y_test,"Predicted Value": y_pred})
predicted_value


# In[77]:


hours = [[9.2]]
own_pred = regressor.predict(hours)
print("No of Hours = {}".format(hours))
print("Predicted Score = {}".format(own_pred[0]))     


# In[79]:


#Evaluating Performance of Algorithm
from sklearn import metrics
print('Mean Absolute Eroor:', metrics.mean_absolute_error(y_test, y_pred))


# In[ ]:




