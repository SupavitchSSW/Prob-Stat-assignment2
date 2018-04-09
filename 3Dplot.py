'''
==============
3D scatterplot
==============

Demonstration of a basic scatterplot in 3D.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import csv

def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100

#read file
f = open("badhealth.csv")
l = list(csv.reader(f))
l.pop(0)
num=[]
badh=[]
age=[]
for i in range(len(l)):
    num.append(l[i][0])
for i in range(len(l)):
    badh.append(l[i][1])
for i in range(len(l)):
    age.append(l[i][2])

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
for j in range(len(l)):
    xs = int(num[j])
    ys = int(age[j])
    zs = int(badh[j])
    #ax.scatter(xs, ys, zs, c=c, marker=m)
    ax.scatter(xs, ys, zs)


ax.set_xlabel('numVisit')
ax.set_ylabel('age')
ax.set_zlabel('badh')

plt.show()
