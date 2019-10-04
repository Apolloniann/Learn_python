#!/usr/bin/env python
# coding: utf-8

# # Python Refresher 

# In[6]:


x = 5 


# In[7]:


def good_enough(x, guess): 
    return abs((guess * guess) - x) < 0.00000000001


def improve_guess(x, guess): 
    return (guess + x/guess)/2 

def sqrt(x, guess=0.0001): 
    if good_enough(x, guess): 
        return guess
    else: 
        return sqrt(x, improve_guess(x, guess)) 


# In[8]:


sqrt(guess=0.1, x=36)


# In[ ]:


x = 16 

if x < 5: 
    print("x is less than 5") 
elif x < 7: 
    print("x is less than 7") 
else: 
    print("x is greater than 7")


# In[ ]:


p = 0
while p < 10: 
    print(p)
    p += 1 


# In[ ]:





# In[ ]:


for i in range(10000000000000000000000000): 
    print(i)


# In[16]:


l = [1, 2, 4, 2, 2, 2] 
l.append(4)
print(l.remove(2))
print(l)


# In[17]:


for i in l: 
    print("Square root of " + str(i)  + ": ",     end="") 
    print(sqrt(i))


# In[32]:


d = { 1: "one", 
      2: "two" }



print(d[1]) 
print(list(d.items()))


# In[33]:


tuple(d.items())  # immutable 


# In[37]:


for k, v in d.items(): 
    print(k, "=", v)


# In[43]:


list(d.keys())


# In[54]:


a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 0, 3, 5, 5, ]

merged = list(zip(a, b))


# In[55]:


merged


# In[59]:


# Real world usecase of ZIP: combining column headers with row values 
# much more, along with usecases, here: https://stackoverflow.com/questions/2429692
fields = ["id", "name", "location"]
values = ["13", "bill", "redmond"]
print(list(zip(fields, values)))
print(dict(zip(fields, values)))


# In[ ]:




