import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import math

# normal graph

# x = [1, 2, 3, 4]
# y = [2, 20, 35, 6]
# plt.plot(x, y)
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('first graph')
# plt.show()

# bar graph
# x = [1, 2, 3, 4]
# y = [2, 20, 35, 6]
# plt.bar(x, y)
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('first graph')
# plt.show()

# i = 1
# avi=[]

# while i < 100:
#   avi[i] = random.randint(0,75)
#   i += 1

# another way of doing it 

array = np.random.randint(75,size=100)
array = array.reshape(50,2)
x_axis = array[:,0]
y_axis = array[:,1]

# This will plot a scattered graph 
plt.scatter(x_axis,y_axis)
plt.xlabel("Sa nu X")
plt.ylabel("Sanla nu Y")
plt.title("tikomic")
plt.show()


# this will plot a histogram
fig,ax=plt.subplots(1,2,figsize=(13,5))
ax[0].hist(x_axis,color = 'b', label = 'x')
ax[1].hist(y_axis,color = 'g',label = 'y')
plt.show()




