#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
r=int(input())
pi=math.pi
t=2*pi*r
print(t)


# In[5]:


import math
math.e


# In[6]:


import math
math.pi


# In[13]:


import random
a=[1,5,90,234,"Блутус"]
e=random.choice(a)
print(e)


# In[18]:


import random
random.randrange(100)


# In[20]:


import random
random.random()


# In[21]:


import random
random.randint(1,10)


# In[23]:


import random
a=[1,5,90,234,"Блутус"]
e=random.shuffle(a)
print(a)


# In[25]:


import random
print("Добрый день, учащиеся!!")
a=["Ольга","Ольга","Ольга","Ольга"]
print("Победитель сегодняшнего розыграша:", random.choice(a))


# In[42]:


import random
print("Добро пожаловать!")
playerone=input("Введите имя первого игрока \n " )
playertwo=input("Введите имя второго игрока \n " )

a=[1,2,3,4,5,6,7,8,9,10]
b=[1,2,3,4,5,6,7,8,9,10]

Scoreone=0
Scoretwo=0

def throwDise():
    for j in range(5):
        random.shuffle(a)
        random.shuffle(b)
    return a[0] + b[0]

for j in range(3):
    result = throwDise()
    Scoreone += result
    print("Игрок",playerone,"выбросил: ",result)
    print("Сумма очков у игрока",playerone,":",Scoreone)
    
    z=input("Чтобы сделать следующий бросок - нажмите Enter \n ")
    result = throwDise()
    Scoretwo += result
    print("Игрок",playertwo,"выбросил: ",result)
    print("Сумма очков у игрока",playertwo,":",Scoretwo)
    z=input("Чтобы сделать следующий бросок - нажмите Enter \n ")
if (playerone>playertwo):
    print("Игрок",playerone,"ВЫИГРАЛ!!")
    print(playerone,"набрал",Scoreone,"очков")

elif (playertwo>playerone):
    print("Игрок",playertwo,"ВЫИГРАЛ!!")
    print(playertwo,"набрал",Scoretwo,"очков")
    
else:
    print("НИЧЬЯ")
    print(playerone,"набрал",Scoreone,"очков")
    print(playertwo,"набрал",Scoretwo,"очков")

