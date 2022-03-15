#!/usr/bin/env python
# coding: utf-8

# In[95]:


res = input('Insira o número de 4 dígitos:\n(obs: não podem ser todos iguais!)')

it = 0
while (res != 6174):
    x = [int(a) for a in str(res)]
    for j in range(len(x)):
        for i in range(len(x)-1):
            if(x[i]<x[i+1]):
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp

    aux = int(res)
    if(aux<1000):
        big = 1000*x[0] + 100*x[1] + 10*x[2]
        sma = 100*x[2] + 10*x[1] + x[0]
    else:
        big = 1000*x[0] + 100*x[1] + 10*x[2] + x[3]
        sma = 1000*x[3] + 100*x[2] + 10*x[1] + x[0]
        
    res = big-sma

    print('\n\n ', big)
    print('-',f'{sma:04}')
    #print('-', sma)
    print('------')
    print(' ',f'{res:04}')
    it = it+1
    
print('\nNúmero de iterações:', it)


# In[ ]:




