#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df=pd.read_excel("C:\\Users\\DELL\\Downloads\\Cricketforcast.xlsx")


# In[5]:


df.head()


# In[7]:


df.shape


# # Data Preprocessing

# In[15]:


df.isnull().any()


# In[16]:


df.isnull().sum()


# In[20]:


df['Outlook'].mode()


# In[21]:


df['Outlook']=df['Outlook'].fillna('Sunny')


# In[28]:


df['Tempearature'].mode()


# In[29]:


df['Tempearature']=df['Tempearature'].fillna('Mild')


# In[30]:


df.isnull().sum()


# In[32]:


df.columns


# # Encoding

# In[45]:


from sklearn.preprocessing import LabelEncoder


# In[46]:


df[['Outlook']]=LabelEncoder().fit_transform(df['Outlook'])


# In[47]:


df[['Tempearature']]=LabelEncoder().fit_transform(df['Tempearature'])


# In[48]:


df[['Humidity']]=LabelEncoder().fit_transform(df['Humidity'])


# In[49]:


df[['Windy']]=LabelEncoder().fit_transform(df['Windy'])


# In[50]:


df[['Play']]=LabelEncoder().fit_transform(df['Play'])


# # EDA

# In[51]:


import seaborn as sns


# In[52]:


tc=df.corr()


# In[53]:


tc


# In[55]:


sns.pairplot(tc)


# # Define x and y

# In[60]:


df.columns


# In[61]:


x=df[['Outlook', 'Tempearature', 'Humidity', 'Windy']]


# In[62]:


x


# In[63]:


y=df[['Play']]


# In[64]:


y


# # Model development

# In[65]:


from sklearn.model_selection  import train_test_split


# In[69]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)


# In[70]:


x_train


# In[71]:


y_train


# In[72]:


from sklearn.linear_model import LogisticRegression


# In[73]:


model=LogisticRegression()


# In[74]:


LogisticRegression()


# In[75]:


model.fit(x_train,y_train)


# In[76]:


y_pred=model.predict(x_test)


# In[77]:


y_pred


# In[78]:


from sklearn import metrics


# In[79]:


cm=metrics.confusion_matrix(y_test,y_pred)


# In[80]:


cm


# In[83]:


metrics.accuracy_score(y_test,y_pred)


# In[84]:


metrics.recall_score(y_test,y_pred)


# In[ ]:




