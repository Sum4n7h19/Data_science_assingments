#!/usr/bin/env python
# coding: utf-8

# In[38]:


#Q1
l=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
list(sorted(l,key=lambda x:x[1]))


# In[39]:


#Q2
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x:x**2,l))


# In[40]:


#Q3
list(map(lambda x:str(x),l))


# In[41]:


#Q4
from functools import reduce
m=[]
for i in range(1,26):
    m.append(i)

a=reduce(lambda x,y:x*y,m)
print(a)


# In[42]:


#Q5
z=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
list(filter(lambda x:x if x%2==0 and x%3==0 else [],z))


# In[43]:


w=['python', 'php', 'aba', 'radar', 'level']
palin=list(filter(lambda x:x[::-1]==x,w))
print(palin)

