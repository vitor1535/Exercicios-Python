import random
import math
import time

vetor = []

while (True):
    num = int(input('Insira um numero'))

    if (not (num in vetor)):       
        vetor.append(num) 
        
    if (num == 999):
        vetor.pop()
        break
    
vetor.sort()
print(vetor)