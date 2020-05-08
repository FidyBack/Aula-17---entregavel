from math import sqrt
import numpy as np
from matplotlib import pyplot as plt 

h = 15
k = 200
l = 0.3
per = 0.03*4
AreaSec = 0.03**2
m = sqrt(h*per/(k*AreaSec))
length = np.linspace(0, l, num=60)
tAmb = 300
tBase = 350
temp = []

for x in length:
    delta = np.cosh(m*(l-x)) + (h/(m*k))*np.sinh(m*(l-x))
    deltaBase = np.cosh(m*l) + (h/(m*k))*np.sinh(m*l)

    temp.append((delta*(tBase-tAmb)/deltaBase)+tAmb)

plt.title("Temperatura na Aleta") 
plt.plot(length,temp) 
plt.grid(True)
plt.show()

print("A temperatura em L/2 é: {}".format(temp[int(len(temp)/2)]))