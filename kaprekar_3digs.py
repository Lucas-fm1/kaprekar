#!/usr/bin/env python
# coding: utf-8

# In[7]:


res = input('Insira o número de 3 dígitos:\n(obs: não podem ser todos iguais!)\n')

it = 0
while (res != 495):
    x = [int(a) for a in str(res)]
    for j in range(len(x)):
        for i in range(len(x)-1):
            if(x[i]<x[i+1]):
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp

    aux = int(res)
    if(aux<100):
        big = 100*x[0] + 10*x[1]
        sma =  10*x[1] +  1*x[0]
    else:
        big = 100*x[0] + 10*x[1] + x[2]
        sma = 100*x[2] + 10*x[1] + x[0]
        
    res = big-sma

    print('\n\n ', big)
    print('-',f'{sma:03}')
    print('------')
    print(' ',f'{res:03}')
    it = it+1
    
print('\nNúmero de iterações:', it)


# In[ ]:




