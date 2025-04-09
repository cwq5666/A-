import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
###三门问题的模拟
# 假设三门分别是0，1，2
n = 1000000
a = 0
b = 1
c = 2
P = 0
#假设奖品在0门

#每次都改门
for i in range(n):
    A = np.random.randint(0,3)
    if A != 0:
        P += 1
print(P/n)
        
        
    
    
