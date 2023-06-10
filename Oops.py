#!/usr/bin/env python
# coding: utf-8

# In[165]:


"""Q1.A "Class" is like an object constructor.or a blueprint for creating object.
To create a Class.use the keyword class."""
"""where addint is class and a and b are objects"""
class addint:
    a=5
    b=10
        


# In[166]:


obj1=addint


# In[167]:


print(addint.a+addint.b)


# In[168]:


"""Q2.The four pillars of oops are 
*Inheritence
*Polymorphism
*Encapsulation
*Abstraction"""


# In[169]:


"""Q3.The __init__() function assigns a values to object properties or other operations that are necessary todo when the
object is being is created"""


# In[170]:


"""Q4.self is used to access the attribute and methods in oops."""


# In[171]:


"""Q5.Inheritance allows us to inherit properties from one class to another class"""
"""There are five types of inheritence."""
#Single inheritance
class Person:
    
    def __init__(self,First_name,Last_name):
        self.First_name=First_name
        self.Last_name=Last_name
        
    def Enter_name(self):
        print(self.First_name,self.Last_name)
        


# In[172]:


class person_name(Person):
    
    pass
        


# In[185]:


name=person_name("Sharath","Kumar")
name.Enter_name()


# In[174]:


#Mutiple inheritance
class mother:
    
    def mom(self,mother_name):
        self.mother_name
    
class father:
    
    def dad(self,father_name):
        self.father_name

class parents(mother,father):
    
    def parent(self):
        print("mother=",self.mother_name)
        print("father=",self.father_name)
        pass


# In[175]:


name=parents()
name.mother_name="Saritha"
name.father_name="Mahesh"
name.parent()


# In[176]:


#Multilevel inheritance
class grandfather:

    def grandpa(self, grandfather_name):
        self.grandfather_name
        


class father(grandfather):

    def dad(self, father_name, grandfather_name):
        self.father_name
        


class son(father):

    def son(self, son_name, grandfather_name, father_name):
        self.son_name
        
        
class family(son,father,grandfather):
    def family_tree(self):
        print("Grandpa=", self.grandfather_name)
        print("father=", self.father_name)
        print("Son=", self.son_name)
        pass


# In[177]:


name = family()
name.grandfather_name = "Shankarapa"
name.father_name = "Mahesh"
name.son_name = "Sumanth"


# In[178]:


name.family_tree()


# In[179]:


#hierarchical inheritance
class queen:
    
    def queen_bee(self):
        print("This is the Queen bee ruler of the hive")
       
        
class drone(queen):
    
    def drone_bee(self):
        print("This is the the Drone bee only male in the hive")
        
class worker(queen):
    
    def worker_bee(self):
        print("This is the Worker bee we are the worker who prduce honey for the Queen")
    


# In[180]:


bee_hive_1=drone()
bee_hive_2=worker()
bee_hive_1.queen_bee()
bee_hive_1.drone_bee()
bee_hive_2.queen_bee()
bee_hive_2.worker_bee()


# In[187]:


#Hybrid inheritance
class company:
    def company(self,company):
        self.company=company
    
    
class investors(company):
    def investors(self,invest):
        self.invest=invest
      
    
class resources(investors,company):
    def resource(self,requirements):
        self.resources=requirements
        
        
class management(investors,company):
    
    def management(self,management):
        self.management=management
        
        

class worker(management,resources):
    def worker(self,worker):
        self.worker=worker  


# In[188]:


class Accounts(worker,management,resources,investors,company): 
   
   def company_detail(self):
       print("Company profit=",self.company)
       print("Investors profits=",self.invest)
       print("Expenses on resources=",self.resources)
       print("Mangement salary=",self.management)
       print("Workers salary=",self.worker)
       pass
   
       
       


# In[189]:


profit=Accounts()
profit.company=10000
profit.invest=8000
profit.resources=3000 
profit.management=4000
profit.worker=3000


# In[190]:


profit.company_detail()


# In[ ]:




