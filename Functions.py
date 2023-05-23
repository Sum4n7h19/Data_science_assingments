#!/usr/bin/env python
# coding: utf-8

# In[53]:


#Q1
#def keyword is used to create a function.

def odd_no(n):
    a=1
    for i in range(n):
        yield a
        a+=1
        


# In[57]:


n=[]
for j in odd_no(25):
    if j % 2 != 0:
        n.append(j)
print(n)


# In[63]:


#Q2
#*args and **kwargs are used to create a data with n no of elements.
#**kwargs is used for key value pairs and stored in dictonary.all types of data can be stored.
#*args is used to store all types of data in tuples.
def nth(*args,**kwargs):
    return args,kwargs
nth(1,3,[1,2,3],'oops',True,(9,8,7,4),a='vista',b=True,c=[1,2,3,4,5,6],d=(9,8,7,6,5))


# In[23]:


#Q3
# itreators are objects that contain a countable number of values.
def itr(n):
    a=[]
    my_iter=iter(n)
    for _ in range(5):
        b=next(my_iter)
        a.append(b)
    print(a)
itr([2, 4, 6, 8, 10, 12, 14, 16,18, 20])
        
            


# In[18]:


#Q4
#a generator function is function which has one or more yield statements in init.
#yield keyword is used generate a memory efficient functions.
def yel(n):
    a=1
    for i in range(n):
        yield a
        a+=1


# In[19]:


b=[]
for j in yel(5):
    b.append(j)
print(b)


# In[25]:


#Q5
def gen_prime():
    a=2
    b=[]
    
    while a<1000:
        l=True
        
        for i in b:
            if a%i==0:
                l=False
                break
        if l:
            b.append(a)
            yield a
        a+=1  


# In[26]:


prime20=gen_prime()
c=[]
for _ in range(20):
    d=next(prime20)
    c.append(d)
        
print(c)


# In[ ]:





# In[ ]:




