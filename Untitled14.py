#!/usr/bin/env python
# coding: utf-8

# In[12]:


import matplotlib.pyplot as plt
x=["Эпл","Самсунг","Хонор"]
y=[1016,516,54]
plt.bar(x,y)
plt.plot(x,y, color="blue")
plt.xlabel("Наиминование компаний")
plt.ylabel("Кол-во продаж")
plt.title("Объём продаж")
plt.grid ()
plt.text(4, 70, "тренд")
plt.show


# In[ ]:




