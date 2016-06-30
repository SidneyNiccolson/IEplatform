import numpy as np,time, scipy.io, h5py, os, psutil, resource, pdb, subprocess
from memory_profiler import profile
from threading import Thread
#metacode

@profile
def finished():
#start merging importing regions to one file called <year>_combined.hdf5
    ssst0 = time.time()
    year = np.arange(1995,2012)
    path = "/home/sidney/experiments/"
    for i, x in enumerate(year):
        for j in range(49):
            #yearStr = ' '.join(map(str,year))
            #print(i)
            #print(j)
            print(x)
            subprocess.call(['h5copy', '-i', path+str(x)+"_region"+str(j)+"_Footprint.hdf5",'-s', '/Footprint', '-o', str(x)+'_combined.hdf5', '-d', '/region'+str(j)])

            #subprocess.call(['h5copy', '-i', '{0}','-s', '/Footprint', '-o', '{1}_combined.hdf5', '-d', '/region{2}'.format(path+str(x$

            print("Success in combining files")
                #pdb.set_trace()
                #del(bDiagVector)
                #del(yDiagVector)

            #f.close()
        #remove the region filed, as at this point there is a combined file of them
        crop = 'rm -rf '+ path+str(x)+'_region*'
        print(crop)
        subprocess.call(str(crop), shell=True)

    ssst1 = time.time()
    ssstotal = ssst1-ssst0
    print("\ntotal time of merging files: "+str(ssstotal))
    #f.flush()

    #f.close()
    #log.close()


    print("finished")

def mult_diag(d, mtx, left=True):
    """Multiply a full matrix by a diagonal matrix.
    This function should always be faster than dot.

    Input:
      d -- 1D (N,) array (contains the diagonal elements)
      mtx -- 2D (N,N) array

    Output:
      mult_diag(d, mts, left=True) == dot(diag(d), mtx)
      mult_diag(d, mts, left=False) == dot(mtx, diag(d))
    """
    if left:
        return (d*mtx.T).T
    else:
        return d*mtx


#create hdf file
#create a new file and this object serves a the first starting point


    #group = f.create_group('a_group')
#f = h5py.File("/home/chai/data/built_exio.hdf5", "w")
@profile
def populate():
    #create log file



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
    #path = "/home/chai/data/"
    path = "/home/sidney/experiments/"
    #year = np.arange(1995,1996)
    #log = open('/home/sidney/experiments/properlog.txt', 'w')

    log = open(path+'v4_2log.txt', 'w')
    #create regions and sectors ranges
    #number of years
    nt = 17
    #number of regions
    nr = 49
    #number of sectors
    ns = 200
    #number of final demand categories
    nf = 1
    #households
    nh = 7
    #0.0000000000001 sort of to check for zero's
    accuracy = 1e-16

    #with h5py.File('/home/sidney/experiments/proper.hdf5','w') as f:
    #with h5py.File('/home/chai/data/v3built_exio.hdf5','w') as f:

    #create hdf dataset with dimension nt * nr * ns * nr * ns * nr for footprint of consumption
    #and a smaller one for emissions of final demand just with nt * ns
        
        #footprint_dset = f.create_dataset('Footprint', (nt, nr, ns, nr, ns, nr), dtype = 'f', compression="gzip", compression_opts=9)



#total of two datasets

    #populate

    print("*** Starting script ***")
    log.write("*** Starting script ***\n")
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  / 1000
    print( "start of script the usage is (in MB):",mem)
    log.write("start of script the usage is (in MB):%s" % str(mem))
    #run loop for year
    sst0 = time.time()
    for i, x in enumerate(year):

    #read stuff from matlab binary
        print("*** Loading file of year: "+ str(x)+ " ***")
        log.write("\n*** Loading file of year: "+ str(x)+ " ***\n")
        t0 = time.time()

        mat = scipy.io.loadmat('/data/exiovisuals/sys_leo_%s.mat' % x) #%insert i in name
        #mat = scipy.io.loadmat('/data/exiovisuals/sys_leo_%s.mat' % x) #%insert i in name

        print("*** Retrieving arrays y,b,h,leo ***", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  / 1000)
        log.write("*** Retrieving arrays y,b,h,leo ***\n")


        y = mat['io']['y'][0][0];
        leo = mat['io']['leo'][0][0];
        b = mat['io']['b'][0][0];
        h = mat['io']['h'][0][0];

    #THIS IS A FIX BECAUSE EMISSIONS FROM HOUSEHOLDS
    #ITERATE OVER FINAL DEMAND CATEGORIES!!!!
        h = np.reshape(h, (nr, nh))[:,0]

        h = h.reshape(1,nr)
        mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  / 1000
        print( "after retrieval of arrays the usage is (MB):",mem)
        log.write("after retrieval of arrays the usage is (MB):%s \n" % str(mem))




        #truncation
        #y = y[0:nr*ns,0:nr*nf]
        #print(y.shape)
        #leo = leo[0:nr*ns,0:nr*ns]
        #b = b[0:1,0:nr*ns]
        #h = h[0:1,0:nr]
        #print("finished")



        t1 = time.time()
        total = t1-t0
        print("Loading time taken: "+str(total))
        log.write("Loading time taken: "+str(total)+ "\n")

        t0 = time.time()
    #populating the final demand emissions database
        print("*** Populating final demand emissions db of year: "+ str(x)+ " ***")
        log.write("*** Populating final demand emissions db of year: "+ str(x)+ " ***\n")
        #X =  x+1
        #print("shape of y:")
        #print(y.shape)
        #print("shape of leo:")
        #print(leo.shape)
        #print("shape of b:")
        #print(b.shape)
        #print("shape of h:")
        #print(h.shape)

         #create an empy combined file
        #fcombine = h5py.File('/home/chai/data/%s_combined.hdf5' % yearStr ,'w')
        #fcombine.create_dataset('finalDemand', (49),dtype='f')

        #f = h5py.File('/home/sidney/experiments/%s_finalDemand.hdf5' % year,'w')
        f = h5py.File(path+'%s_finalDemand.hdf5' % x ,'w')
        finalDemand_dset = f.create_dataset('Final_demand', (nt,nr),dtype='f')
        #try to fill in the final demand dataset with at coordinate i the array
        finalDemand_dset[i,:] = h


        t1 = time.time()
        total = t1-t0
        print("Final demand population time taken: "+str(total))
        log.write("Final demand population time taken: "+str(total)+"\n")
    #nested make calculations by country of demand
        print("*** Populating footprint db of year: "+ str(x)+ " ***")
        log.write("*** Populating footprint db of year: "+ str(x)+ " ***\n")
    #diagonal direct impact vector
        #bDiag = np.diag(b[0])



        #print(bDiag[0][0])

        #test = []

        #print(len(test))
        #print(bDiag.shape)
        #dgl = np.diag_indices(9800)
        #bDiagVector = bDiag[dgl]
        #print(leo.shape)
        t0 = time.time()
    #iterating over import region

        #yDiag = np.diag(y[:,j])
        #diagonal = np.diag_indices(9800)
        #print(diagonal)
        #yDiagVector = (yDiag[diagonal])
        def myfunc(j):




            mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  / 1000
            print( "before calculating the usage is (MB):",mem)
            log.write("before calculating the usage is (MB):%s \n" % str(mem))
            foot = mult_diag(y[:,j],leo, left=False)
            foot = mult_diag(b[0],foot, left=True)
            mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  / 1000
            print( "after calculating the usage is (MB):",mem)
            log.write("after calculating the usage is (MB):%s \n" % str(mem))
            vpercent = 99.9
            vtot = sum(sum(abs(foot)))
            vmax = np.max(foot)

            for k in range(50):
                foot_tmp1 = foot * (foot > (vmax * 10 ** (-1 * k)))
                vtmp = sum(sum(abs(foot_tmp1)))
                if (vtmp/vtot*100 > vpercent):
                    ktmp = k
                    break

            #ktmp = 8
            #foot_tmp1 = foot * (foot > (vmax * 10 ** (-1 * ktmp)))
            #vtmp = sum(sum(foot_tmp1))
            print("ktmp")
            log.write(str(ktmp)+ " "+ str(vtmp/vtot*100)+ " "+ str(100*vtmp / vtot))
            log.flush()
            print(ktmp)
            print(sum(sum(foot_tmp1)))
            foot = foot_tmp1

            foot_tmp = np.reshape(foot,[nr,ns,nr,ns])
            #sum_foot_tmp = np.sum(foot_tmp)
            #nonzero_foot_tmp = np.count_nonzero(foot_tmp)
            #do the multiplication of leontief times the y diagonal
            f2 = h5py.File(path+'{0}_region{1}_Footprint.hdf5'.format(x, j) ,'w')

            temperal = ('Footprint_dset_%s' % str(j))
            print(temperal)
            temperal = f2.create_dataset('Footprint', (nr, ns, nr, ns), dtype = 'f', compression="gzip", compression_opts=9 )

            temperal[:,:,:,:] = foot_tmp
            
        #do multithreading but do not do al 49 threads at the same time
        for j in range(10):
            t = Thread(target=myfunc, args=(j,))
            t.start()
            t.join()
        for j in range(10):
            j = j+10
            t = Thread(target=myfunc, args=(j,))
            t.start()
            t.join()
        for j in range(10):
            j = j+20

            t = Thread(target=myfunc, args=(j,))
            t.start()
            t.join()

        for j in range(10):
            j = j+30

            t = Thread(target=myfunc, args=(j,))
            t.start()
            t.join()

        for j in range(9):
            j = j+40
            t = Thread(target=myfunc, args=(j,))
            t.start()
            t.join()

        #total time of calculating and putting into a file:
        sst1 = time.time()
        sstotal = sst1-sst0
        log.write("\ntotal time of calculating and putting into a file: "+str(sstotal))

        f.flush()
        log.flush()
        #log.close()
        f.close()

        
populate()
finished()
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



    #################
    #for the future
    #querying breakdown of footprint by a specific final country, by all consumption goods, across all import regions, for agriculture in europe in a given year.

    #first query
    #tmp = footprint_dset[1,1:28,1:5,:,:,2]
    #sum over dimensions not to be displayed
    #tmp = tmp.sum(axis=2).sum(axis=3).sum(axis=4)
'''
    #depending on the query household emissions might be required



