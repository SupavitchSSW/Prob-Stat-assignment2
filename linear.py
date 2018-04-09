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

#show graph
x = []
for i in range(20,61):
    x.append(i)

#all
plt.figure(1)
y = ageCountAll[20:61]
fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit) 
plt.plot(x,y, 'bo', x, fit_fn(x), '--k')
plt.ylabel("number of people")
plt.xlabel("Age (year)")
plt.title("all people")


#good
plt.figure(2)
y = ageCountGood[20:61]
fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit) 
plt.plot(x,y, 'bo', x, fit_fn(x), '--k')
plt.ylabel("number of people")
plt.xlabel("Age (year)")
plt.title("goodheath people")

#bad
plt.figure(3)
y = ageCountBad[20:61]
fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit) 
plt.plot(x,y, 'bo', x, fit_fn(x), '--k')
plt.ylabel("number of people")
plt.xlabel("Age (year)")
plt.title("badheath people")

plt.show()
