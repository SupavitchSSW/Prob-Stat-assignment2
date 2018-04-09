import numpy as np
import matplotlib.pyplot as plt
import csv

#read file
f = open("badhealth.csv")
l = list(csv.reader(f))

#delete col name
l.pop(0)

#split data to list
ageCountAll = []
ageCountBad = []
ageCountGood = []
for i in range(100):
    ageCountAll.append(0)
    ageCountBad.append(0)
    ageCountGood.append(0)
for i in range(len(l)):
    x = int(l[i][2])
    ageCountAll[x] += 1
    if l[i][1] == '1':
        ageCountBad[x] += 1
    else:
        ageCountGood[x] += 1

j=[]
for i in range(100):
    j.append(i)
x = np.array(j)
#show histogram
#all
plt.figure(1)
plt.bar(x, height= ageCountAll)
plt.ylabel("number of people")
plt.xlabel("Age (year)")
plt.title("all people")
plt.axis([10, 70, 0, 60])
plt.grid(True)

#all
plt.figure(2)
plt.bar(x, height= ageCountBad)
plt.ylabel("number of people")
plt.xlabel("Age (year)")
plt.title("badheath people")
plt.axis([10, 70, 0, 60])
plt.grid(True)

#all
plt.figure(3)
plt.bar(x, height= ageCountGood)
plt.ylabel("number of people")
plt.xlabel("Age (year)")
plt.title("goodheath people")
plt.axis([10, 70, 0, 60])
plt.grid(True)



plt.show()