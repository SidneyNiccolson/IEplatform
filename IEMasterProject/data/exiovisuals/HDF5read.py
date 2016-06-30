import numpy as np
import h5py
 
with h5py.File('/home/chai/data/built_exio.hdf5','r') as hf:
    print('List of arrays in this file: \n', hf.keys())
    data = hf.get('Final_demand')
    np_data = np.array(data)
    print('Shape of the array dataset_1: \n', np_data.shape)
    print(np_data)

a = np.matrix([1,2,3,4])
print(a.shape)
print(a)
d = np.diagonal(a)
print (d)

a = np.array([1,2,3,4])
print(a)
d = np.diag(a)
# or simpler: d = np.diag([1,2,3,4])

#print(d)