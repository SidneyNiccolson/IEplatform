
import time, numpy as np
import csv

t0 = time.time()
#npB = np.fromfile('data/exiovisuals/sys_1995_b.dat', count=-1, sep=" ")
#npY = np.fromfile('data/exiovisuals/sys_1995_y.dat', count=-1, sep=" ")
#np1= np.fromfile('/home/chai/data/sys_1995_leo.dat',  count=-1, sep="   ")
#answer =npB*np1*npY

d = np.loadtxt("/home/chai/data/sys_1995_leo.dat", delimiter= "\t")
print (d[0][2])


t1 = time.time()
total = t1-t0
print(total)
'''
with open() as f:
    reader = csv.reader(f, delimter="\t")
    d = list(reader)


#print(answer)
#print(len(npY))
#print(len(np1))


#matrix that has values up to 15 with 3 columns and 5 rows
#data =  np.arange(15).reshape(5, 3)
#vector has value 6 , 7 ,8 so 1 column and 3 rows
#data1 = np.array([[6, 7, 8]])
npY = npY.reshape(1, -1)

npB = npB[None, :]
np1 = np1.reshape((-1, 9800))
#print(npB.shape)
#print(npY.shape)

print(np1*npB)
print("-----------")
#print(data1.shape)
#print(data.shape)


t1 = time.time()
total = t1-t0
print(total)

'''

