import numpy as np,time, scipy.io, h5py

#metacode


#create hdf file
#create a new file and this object serves a the first starting point


f = h5py.File("/home/chai/data/built_exio.hdf5", "w")

#create log file
log = open('/home/chai/data/log.txt', 'w')


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
year = np.arange(1995,1996)

#create regions and sectors ranges
#number of years
nt = 17
#number of regions
nr = 49
#number of sectors
ns = 200
#number of final demand categories
nf = 7


#create hdf dataset with dimension nt * nr * ns * nr * ns * nr for footprint of consumption
#and a smaller one for emissions of final demand just with nt * ns
#total of two datasets

footprint_dset = f.create_dataset('Footprint', (nt, nr, ns, nr, ns, nr), dtype = 'f')
finalDemand_dset = f.create_dataset('Final_demand', (nt,nr),dtype='f')

#populate

print("*** Starting script ***")
log.write("*** Starting script ***\n")
#run loop for year
for i, x in enumerate(year):
#read stuff from matlab binary
    print("*** Loading file of year: "+ str(x)+ " ***")
    log.write("*** Loading file of year: "+ str(x)+ " ***\n")
    t0 = time.time()
    mat = scipy.io.loadmat('/home/chai/data/sys_leo_%s.mat' % x) #%insert i in name

    print("*** Retrieving arrays y,b,h,leo ***")
    log.write("*** Retrieving arrays y,b,h,leo ***\n")


    y = mat['io']['y'][0][0];
    leo = mat['io']['leo'][0][0];
    b = mat['io']['b'][0][0];
    h = mat['io']['h'][0][0];
#THIS IS A FIX BECAUSE EMISSIONS FROM HOUSEHOLDS
#ITERATE OVER FINAL DEMAND CATEGORIES!!!!
    h = np.reshape(h, (nr, nf))[:,0]
    t1 = time.time()
    total = t1-t0
    print("Loading time taken: "+str(total))
    log.write("Loading time taken: "+str(total)+ "\n")

    t0 = time.time()
#populating the final demand emissions database
    print("*** Populating final demand emissions db of year: "+ str(x)+ " ***")
    log.write("*** Populating final demand emissions db of year: "+ str(x)+ " ***\n")
    #X =  x+1
    print("shape of y:")
    print(y.shape)
    print("shape of leo:")
    print(leo.shape)
    print("shape of b:")
    print(b.shape)
    print("shape of h:")
    print(h.shape)

    #try to fill in the final demand dataset with at coordinate i the array h
    finalDemand_dset[i,:] = h

    t1 = time.time()
    total = t1-t0
    print("Final demand population time taken: "+str(total))
    log.write("Final demand population time taken: "+str(total)+"\n")
#nested make calculations by country of demand
    print("*** Populating footprint db of year: "+ str(x)+ " ***")
    log.write("*** Populating footprint db of year: "+ str(x)+ " ***\n")
#diagonal direct impact vector
    bDiag = np.diag(b[0])



    #print(bDiag[0][0])
    #0.0000000000001 sort of to check for zero's
    accuracy = 1e-16
    test = []

    #print(len(test))


    t0 = time.time()
#iterating over import region
    for j in np.arange(nr):

        yDiag = np.diag(y[:,j])



        #do the multiplication of leontief times the y diagonal
        dotLy = np.dot(leo,yDiag)
        foot = np.dot(bDiag, dotLy)
        #print(bDiag)
        #foot = bDiag * leo * yDiag
        foot_tmp = np.reshape(foot,[nr,ns,nr,ns])
        #print(foot_tmp[0][0][1][1])
        #print(foot[0 + ns * 0][1 + ns * 1])
        #check if foot_tmp[i1][j1][i2][j2] is equal
        # to foot[j1 + ns * i1][j2 + ns * i2]	

		#if check holds then paste into dset	

        footprint_dset[i,:,:,:,:,j] = foot_tmp
    t1 = time.time()
    total = t1-t0
    print("Product b, Leo and y time taken: "+str(total))
    log.write("Product b, Leo and y + Populating footprint dataset time taken: "+str(total)+"\n")
    #memory cleanup
    del(h)
    del(b)
    del(y)
    #del(dotLy)
    #del(foot)
    del(yDiag)
    f.close()
'''
Validation TEST!!
    for i in range(9800):
        #This is the validation wether the diagonal elements in bDiag are the same as the vector of b
        if bDiag[i][i]!=b[0][i]:
            print("problem")
            print("at position: " + str(i)+ "original is: " + str(b[0][i]) + "Diagonal is: " + str(bDiag[i][i]))
        #This is the validation wether everything outside the diagonal are zero's
        for j in range(9800):
            if j!=i:
                if abs(bDiag[i][j])>accuracy:
                    print("problem")

                    print("at position: " + str(i)+  "Zero is: " + str(bDiag[i][j]))

'''
'''

#################
#for the future
#querying breakdown of footprint by a specific final country, by all consumption goods, across all import regions, for agriculture in europe in a given year.

#first query
#tmp = footprint_dset[1,1:28,1:5,:,:,2]
#sum over dimensions not to be displayed
#tmp = tmp.sum(axis=2).sum(axis=3).sum(axis=4)
'''
#depending on the query household emissions might be required


