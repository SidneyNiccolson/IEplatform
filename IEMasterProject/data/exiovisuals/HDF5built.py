import numpy as np, h5py, scipy.io

#metacode


#create hdf file
#create a new file and this object serves a the first starting point
f = h5py.File("/home/chai/data/built_exio.hdf5", "w")
#create year ranges and totals
year =  [
            "1995",
            "1996",
        "1997",
        "1998",
        "1999",
        "2000",
        "2001",
        "2002",
        "2003",
        "2004",
        "2005",
        "2006",
        "2007",
        "2008",
         "2009",
        "2010",
        "2011",
            ];
year = np.arange(1995,2012)

#create regions and sectors ranges
nt = 17
nr = 49
ns = 200

#create hdf dataset with dimension nt * nr * ns * nr * ns * nr for footprint of consumption
#and a smaller one for emissions of final demand just with nt * ns
#total of two datasets
footprint_dset = f.create_dataset('Footprint', (nt, nr, ns, nr, ns, nr), dtype = 'f')
finalDemand_dset = f.create_dataset('Final_demand', (nt,ns),dtype='f')
#populate

print("*** Starting script ***")
#run loop for year
for x,i in enumerate(year):
#read stuff from matlab binary

    print("*** Loading file of year: "+ str(i)+ " ***")
    mat = scipy.io.loadmat('/home/chai/data/sys_leo_%s.mat' % i) #%insert i in name

    print("*** Retrieving arrays y,b,h,leo ***")

    y = mat['io']['y'];
    leo = mat['io']['leo'];
    b = mat['io']['b'];
    h = mat['io']['h'];



    print(y.shape[0][0])
    print(leo.shape)
    print(b.shape)
    print(h.shape)
#populating the final demand emissions database
    print("*** Populating final demand emissions db of year: "+ str(i)+ " ***")


    #finalDemand_dset[i,:] = h
    #try to fill in the final demand dataset with at coordinate x the array h
    #finalDemand_dset[x,:] = k
'''
#nested make calculations by country of demand
    print("*** Populating footprint db of year: "+ str(i)+ " ***")
    for j in np.arange(nr):

#populating the footprint database
        bDiag = np.diag(b)
        #bla = np.diag(y)
        #ts = bla[:j]

        #yDiag = np.diag(y[:,j])

        #f = bDiag * leo * ts
        #footprint_dset[i,:,:,:,:,j] = np.reshape(f,[nt,nr,ns,nr,ns])



#################
#for the future
#querying breakdown of footprint by a specific final country, by all consumption goods, across all import regions, for agriculture in europe in a given year.

#first query
#tmp = footprint_dset[1,1:28,1:5,:,:,2]
#sum over dimensions not to be displayed
#tmp = tmp.sum(axis=2).sum(axis=3).sum(axis=4)
'''
#depending on the query household emissions might be required
