#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1
#using the #(Hash) symbol 
'''You can use single ('') or double ("") quotation marks to comment'''


# In[3]:


#Q2
#variables are used to contain or store variables 
a="One piece"
b=33
c=33.56
#to assign a variable 
d=int(input("Enter a integer"))#only takes an integer
e=input("Enter a string:")#only takes a string as variable


# In[5]:


#Q3
#To convert one data type to anotyher there are inbuilt functions
z=23
print(type(z))
x=str(z)
print(type(x))
y=float(z)
print(type(y))


# Q4
# open a text editor-->create a new file in .py format-->write a python code (ex:print("hello world)) -->save the file and exit text editor-->open command line-->Navigate to the correct directory-->once you are in correct directory enter the command pyhton file_name.py-->the code will execute in the python interpreter
# 

# In[8]:


#Q5
my_list=[1,2,3,4,5]
sub_list=my_list[1:3]
print(sub_list)


# In[11]:


#Q6
#a complex number a number which has both a real number and imaginary number
#ex:2+3i
#In python we have a bulit in function complex() or 
comp=3j
print(comp)
print(type(comp))
#or
p=3
q=complex(p)
print(q)
print(type(q))


# In[1]:


#Q7
age=int(input("Enter your age: "))
#or
age2=25
print(age,"\n",age2)


# In[2]:


#Q8
price=9.99
print(price)
print(type(price))


# In[3]:


#Q9
name=input("Enter your name: ")
print(name)


# In[7]:


#Q10
a="Hello World"
b=a[6:]
print(b)


# In[10]:


#Q11
Is_student=input("Enter t for true f for false: ").lower()
if Is_student=='t':
    print(True)
else:
    print(False)


# In[ ]:




