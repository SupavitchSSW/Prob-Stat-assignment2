import numpy as np
import matplotlib.pyplot as plt
import csv

#read file
f = open("badhealth.csv")
l = list(csv.reader(f))

#delete col name
l.pop(0)

ageAll = []
ageBad = []
ageGood = []

#read data
for i in range(len(l)):
    x = int(l[i][2])
    ageAll.append(x)
    if l[i][1] == '1':
        ageBad.append(x)
    else:
        ageGood.append(x)

#sort
ageAll.sort()
ageBad.sort()
ageGood.sort()

#mean
meanAll = sum(ageAll)/len(ageAll)
meanBad = sum(ageBad)/len(ageBad)
meanGood = sum(ageGood)/len(ageGood)

#mediam
a = len(ageAll)/2
if type(a) is int:
    mediamAll = ageAll[a]
else:
    mediamAll = (ageAll[int(a)] + ageAll[int(a)+1])/2

a = len(ageBad)/2
if type(a) is int:
    mediamBad = ageBad[a]
else:
    mediamBad = (ageBad[int(a)] + ageBad[int(a)+1])/2

a = len(ageAll)/2
if type(a) is int:
    mediamGood = ageGood[a]
else:
    mediamGood = (ageGood[int(a)] + ageGood[int(a)+1])/2

#arithmetic mean
max = 0
for i in range(20,61):
    if ageAll.count(i) > max:
        max = ageAll.count(i)
        arMeanAll = i

max = 0
for i in range(20,61):
    if ageBad.count(i) > max:
        max = ageBad.count(i)
        arMeanBad = i

max = 0
for i in range(20,61):
    if ageGood.count(i) > max:
        max = ageGood.count(i)
        arMeanGood = i

stdAll = np.std(ageAll)
stdBad = np.std(ageBad)
stdGood = np.std(ageGood)

print("All - Bad - Good\n","(mean)",meanAll,meanBad,meanGood,"\n","(mediam)",mediamAll,mediamBad,mediamGood,"\n","arithmetic mean",arMeanAll,arMeanBad,arMeanGood,"\n","Standard Deviation",stdAll,stdBad,stdGood)