import h5py
import numpy as np


#create a new file and this object serves a the first starting point
f = h5py.File("/home/chai/data/mytestfile.hdf5", "w")
'''
#create an HDF5 dataset
dset = f.create_dataset("mydataset", (100,), dtype='i')
print(dset)
print("dsgfs")


#fill in the data set with 100 values
dset[...] = np.arange(100)




#retrieve elements of dataset 0-100 retrieve each 10ths element each time
print(dset[0:100:11])

# print the name of the dataset
print(dset.name)
#print the hierarchy
print(f.name)

#create a subgroup
grp = f.create_group("subgroup")
print(grp.name)

#create a dataset within this subgroup
dset2 = grp.create_dataset("another_dataset", (50,), dtype='f')
print(dset2.name)

#create a subgroup and corresponding dataset at once
dset3 = f.create_dataset('subgroup2/dataset_three', (10,3,2), dtype='i')

print(dset3.shape)
'''
print("test1 creation of arrays with reshape----------------------")

leo = np.array([1,2,3,4]).reshape(2,2)
print("leo: ")
print(leo)
print("----")
b = np.array([7,8]).reshape(-1,2)
print("b shape: ")
print(b.shape)
print("b: ")
print(b)
print("----")
y = np.array([5,6]).reshape(2,-1)
print("y shape: ")
print(y.shape)
print("y: ")
print(y)
print("----")

print("b diag: ")
print(np.diag(b))
print("y diag: ")
print(np.diag(y))

result = np.diag(b) * leo * np.diag(y)
print("The result is: ")
print(result)


print("end of test1----------------------")

print("test2: creation of arrays without reshaping y and b vectors----------------------")


leo = np.array([1,2,3,4]).reshape(2,2)
print("leo: ")
print(leo)
print("----")
b = np.array([7,8])
print("b shape: ")
print(b.shape)
print("b: ")
print(b)
print("----")
y = np.array([5,6])
print("y shape: ")
print(y.shape)
print("y: ")
print(y)
print("----")

print("b diag: ")
print(np.diag(b))
print("y diag: ")
print(np.diag(y))

result = np.diag(b) * leo * np.diag(y)
print("The result is: ")
print(result[0][0])


print("end of test2----------------------")
'''
#each row will have the value of x
for x in liss:
    print(x)
    #put the values of t at coordinate x of rows
    t = 6
    dset[:,x] = t

for x in ts:
    print(x)
    t = 5
    #put the values of t at coordinate x in terms of rows
    dset[x,:] = t


print(ts)


with h5py.File('/home/chai/data/mytestfile.hdf5','r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    data = hf.get('MyDataset')
    np_data = np.array(data)
    print('Shape of the array dataset_1: \n', np_data.shape)
    print(np_data)

'''

#!!!Retrieve objects in the file
#datasetTest = f['dataset_three']
#for x in datasetTest:
#    print(x)

#check for datasets in file
#print("subgroup2/dataset_three" in f)

#There are also the familiar keys(), values(), items() and iter() methods, as well as get().

#Since iterating over a group only yields its directly-attached members, iterating over an entire file is accomplished with the Group methods visit() and visititems(), which take a callable:

#def printname(name):
#    print(name)
#f.visit(printname)