#用蒙特卡罗方法求π的近似值
import random
import matplotlib.pyplot as plt
import numpy as np
p = 1000000
a = 0
#确定这个⚪
r = 1
x_0,y_0 = 1,1

for i in range(p):
    x = np.random.rand()*2
    y = np.random.rand()*2
    #判断是否在⚪内
    if (x-x_0)**2+(y-y_0)**2 < r**2:
        a += 1
print(4*a/p)
        


