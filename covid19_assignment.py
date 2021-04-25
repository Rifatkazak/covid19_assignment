#!/usr/bin/env python
# coding: utf-8

# In[9]:


age = input("Are you a cigarette addict older than 75 years old-Yes or No? ").lower()
chronic = input("Do you have a severe chronic disease-Yes or No? ").lower()
immune = input("Is your immune system too weak-Yes or No? ").lower()

if not age == "yes" and not chronic == "yes" and not immune == "yes" :
    print("You are not in risky group")
else:
    print("You are in risky group")


# In[ ]:




