#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=int(input())
if (a>=1 and a<=2):
    print("Зима")
elif (a>=3 and a<=5):
    print("Весна")
elif (a>=6 and a<=8):
    print("Лето")
elif (a>=9 and a<=11):
    print("Осень")    
elif (a==12):
    print("Зима")
else:
    print("Введен неправильный месяц")


# In[ ]:


health=int(input())
if health <=0:
    print("Нет здоровья")
else:
    print("Есть здоровья")


# In[4]:


a=int(input())
b=int(input())
c=int(input())
d=((a+2)/(b+5))**4-0.001*c
print(d)


# In[ ]:




