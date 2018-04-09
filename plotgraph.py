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
#All
plt.figure(1)
for i in range(20,61):
    plt.plot(i,ageCountAll[i],'ro')
plt.ylabel("number of people")
plt.xlabel("Age (year)")
plt.title("all people")

#Bad
plt.figure(2)
for i in range(20,61):
    plt.plot(i,ageCountBad[i],'ro')
plt.ylabel("number of people")
plt.xlabel("Age (year)")
plt.title("badheath people")

#Good
plt.figure(3)
for i in range(20,61):
    plt.plot(i,ageCountGood[i],'ro')
plt.ylabel("number of people")
plt.xlabel("Age (year)")
plt.title("goodheath people")


plt.show()



