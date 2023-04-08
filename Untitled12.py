#!/usr/bin/env python
# coding: utf-8

# In[5]:


print ('Хай')
a = int (input('Введите первое число: '))
b = int (input('Введите второе число: '))

v = int (input('Какую операцию Вы хотите выполнить? /n 1 Сложение и Вычитание /n 2 Умножение и Деление /n 3 Процент и Деление с остатком'))

if v==1:
    a = int (input('Введите первое число: '))
    b = int (input('Введите второе число: '))
    
    a=int(input())
    b=int(input())
    
    print(a + b)
    print(a - b)

if v==2:
    a = int (input('Введите первое число: '))
    b = int (input('Введите второе число: '))
    
    a=int(input())
    b=int(input())
    
    print(a * b)
    print(a / b)
    
if v==3:
    a = int (input('Введите первое число: '))
    b = int (input('Введите второе число: '))
    
    a=int(input())
    b=int(input())
    
    print(a % b)
    print(a // b)
input()


# 
# b=int(input())
# 
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a // b)
