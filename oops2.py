#!/usr/bin/env python
# coding: utf-8

# In[88]:


#Q1
class vehicle:
    
    def __init__(self,name_of_vehicle,max_speed,average_of_speed):
        self.name_of_vehicle=name_of_vehicle
        self.max_speed=max_speed
        self.average_of_speed=average_of_speed
        

    
        


# In[89]:


car=car
car.name_of_vehicle="Toyata"
car.max_speed=120
car.average_of_speed=60


# In[90]:


car.name_of_vehicle


# In[91]:


car.max_speed


# In[92]:


car.average_of_speed


# In[93]:


#Q2
class car(vehicle):
    
    def seating_capacity(self,capacity):
        return f"the {self.name_of_vehicle} has a seating capacity of {self.capacity}"
        pass


# In[94]:


car.seating_capacity=5 
car.seating_capacity


# In[101]:


#Q3
class stastistics:
    def stats(self):
        print("This is stastistics")
        
class programming:
    def python(self):
        print("this is python")

class domain_knowledge:
    def domain(self):
        print("this is the domain")
        
class machine_learning:
    def ML(self):
        print("this is machine learning")
        
class data_science(stastistics,programming,domain_knowledge,machine_learning):
    def data_sci(self):
        print("the combination of all the field is data science")
        pass


# In[103]:


data_sci=data_science()
data_sci.stats()
data_sci.python()
data_sci.domain()
data_sci.ML()
data_sci.data_sci()


# In[111]:


#Q4
class course:
    
    def __init__(self,course_fees,course_year,course_name):
        self.__course_fees=course_fees
        self.course_year=course_year
        self.course_name=course_name
        
    @property
    def course_fees_acess(self):
        return self.__course_fees
    
    @course_fees_acess.setter
    def course_fees_set(self,fees):
        self.__course_fees=course_fees
        
        
        


# In[112]:


course=course(46000,2022,"Masters in Science")


# In[116]:


course.course_year


# In[117]:


course.course_name


# In[119]:


course.course_fees_acess


# In[126]:


"""Q5. Method overriding is a feature in object-oriented programming where a subclass provides its own implementation 
of a method that is already defined in its superclass. The overridden method in the subclass is called instead of the 
superclass method when invoked on an instance of the subclass. Here's an example:"""
class Teacher:
    def greet(self):
        print("welcome")
        
class student:
    def greet(self):
        print("Welcome")


# In[127]:


teacher=Teacher()
Student=student()


# In[128]:


teacher.greet()
Student.greet()


# In[ ]:




