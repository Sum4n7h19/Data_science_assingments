#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1
a=[1,'sam',(1,2,3),3.1421]
print(a)
z=type(a[0])
y=type(a[1])
x=type(a[2])
v=type(a[3])
print(z,y,x,v)


# In[2]:


#Q2
va1=''
va2='[ DS , ML , Python]'
va3=[ 'DS' , 'ML' , 'Python']
va4=1.
print(type(va1),type(va2),type(va3),type(va4))


# In[3]:


#Q3
# / = means division
#ex:
b=10/5
print(b)
# % = means modulus which gives the remainder of a divident
#ex:
c=6%5
print(c)
# // = means Floor division means dividing and rounding down to the nearest integer
#ex:
d=10//6
print(d)
# ** = Gives the power of a no with respect to the oyher
# ex:
e=3**6
print(e)


# In[4]:


#Q4
f=[1,'sam',(1,2,3),3.1421,True,{'name':'sumanth'},{1,2,3},'a',(22/7)]
for i in f:
    print(type(i))


# In[16]:


#Q5
x=10
y=3
count=0
while x % y:
    count+=1
    x=x//y
if x > 0:
    print(f"{x} is divisible by {y} {count} no of times.")
else:
    print(f"{x} is not divisivle by {y}")


# In[6]:


#Q6
list1=[]
for i in range(1,25+1):
    list1.append(i)
print(list1)

for j in list1:
    if j % 3 == 0:
        print(f"the {j} no are divisible by 3")
    else:
        print(f"the {j} no are not divisible by 3")


# In[26]:

#Q6
#Mutable data types are data whose values can be changed or a data whose parameters are not defined. 
#ex:Lists and dictonary
list2=[1,2,3]
print(list2)
list2.append(4)
print(list2)

#Immutable data types are data whose values can't be changed or whose parameters are clearly defined.
#ex:set,tuples,int,float and string.
num1=3.1426
num2=num1
num1=num2+1
print(num1)
print(num2)

#Another example with string
s="cat "
y=s
s=s+'meow'
print(s)
print(y)

#but some immutable can be changed by converting them into the same class objects

num=str(num2)+s
print(num)


# In[ ]:




