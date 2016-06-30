import numpy as np,time, scipy.io, h5py, os, psutil, resource,  pdb
from threading import Thread
from memory_profiler import profile
#metacode

@profile
def finished():
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
    log = open('/home/sidney/experiments/full_v3log.txt', 'w')


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
    #nr = 2
    #number of sectors
    ns = 200
    #ns = 3
    #number of final demand categories
    nf = 1
    #households
    nh = 7
    #0.0000000000001 sort of to check for zero's
    accuracy = 1e-16


    with h5py.File('/home/sidney/experiments/full_v3built_exio_temp1.hdf5','w') as f:

    #create hdf dataset with dimension nt * nr * ns * nr * ns * nr for footprint of consumption
    #and a smaller one for emissions of final demand just with nt * ns
        footprint_dset = f.create_dataset('Footprint', (nt, nr, ns, nr, ns, nr), dtype = 'f', compression="gzip", compression_opts=9)
        finalDemand_dset = f.create_dataset('Final_demand', (nt,nr),dtype='f')
    #total of two datasets

        #populate

        print("*** Starting script ***")
        log.write("*** Starting script ***\n")
        mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  / 1000
        print( "start of script the usage is (in MB):",mem)
        log.write("start of script the usage is (in MB):%s" % str(mem))
        #run loop for year
        for i, x in enumerate(year):
        #read stuff from matlab binary
            print("*** Loading file of year: "+ str(x)+ " ***")
            log.write("\n*** Loading file of year: "+ str(x)+ " ***\n")
            t0 = time.time()

            mat = scipy.io.loadmat('/data/exiovisuals/sys_leo_%s.mat' % x) #%insert i in name

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
            mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  / 1000
            print( "before calculating the usage is (MB):",mem)
            log.write("before calculating the usage is (MB):%s \n" % str(mem))

            '''
            foot = mult_diag(y[:,j],leo, left=False)
            foot = mult_diag(b[0],foot, left=True)
            st1 = time.time()
            stotal = st1-st0
            #this section of code is to truncate (put values below a treshold to zero's
            vpercent = 50
            vtot = sum(sum(abs(foot)))
            vmax = np.max(foot)
            for k in range(50):
                foot_tmp1 = foot * (foot > (vmax * 10 ** (-k)))
                vtmp = sum(sum(abs(foot_tmp1)))
                if (vtmp/vtot*1000 > vpercent):
                    ktmp = k
                    break
            print("ktmp")
            print(ktmp)
            foot = foot_tmp1
            del(foot_tmp1)
            log.write("Time taken for matrix/vector calc: " + str(stotal))
            log.flush()
            mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  / 1000
            print( "after calculating the usage is (MB):",mem)
            log.write("after calculating the usage is (MB):%s \n" % str(mem))

            #do the multiplication of leontief times the y diagonal
            #dotLy = np.dot(leo,yDiag)
            #foot = np.dot(bDiag, dotLy)
            #print(bDiag)
            #foot = bDiag * leo * yDiag

            foot_tmp = np.reshape(foot,[nr,ns,nr,ns])
            sum_foot_tmp = np.sum(foot_tmp)
            nonzero_foot_tmp = np.count_nonzero(foot_tmp)
            #print(foot_tmp[0][0][1][1])
            #print(foot[0 + ns * 0][1 + ns * 1])
            #check if foot_tmp[i1][j1][i2][j2] is equal
            # to foot[j1 + ns * i1][j2 + ns * i2]

            #if check holds then paste into dset
            print("populating at loop: "+str(x)+ "  populating at region: " +str(j))
            st0 = time.time()
            '''
            def myfunc(j, y, leo, b):
                st0 = time.time()
                foot = mult_diag(y[:,j],leo, left=False)
                foot = mult_diag(b[0],foot, left=True)
                st1 = time.time()
                stotal = st1-st0
                #this section of code is to truncate (put values below a treshold to zero's
                vpercent = 50
                vtot = sum(sum(abs(foot)))
                vmax = np.max(foot)
                for k in range(50):
                    foot_tmp1 = foot * (foot > (vmax * 10 ** (-k)))
                    vtmp = sum(sum(abs(foot_tmp1)))
                    if (vtmp/vtot*1000 < vpercent):
                        ktmp = k
                        break
                print("ktmp")
                print(ktmp)
                foot = foot_tmp1
                del(foot_tmp1)
                log.write("Time taken for matrix/vector calc: " + str(stotal))
                log.flush()
                mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  / 1000
                print( "after calculating the usage is (MB):",mem)
                log.write("after calculating the usage is (MB):%s \n" % str(mem))

                #do the multiplication of leontief times the y diagonal
                #dotLy = np.dot(leo,yDiag)
                #foot = np.dot(bDiag, dotLy)
                #print(bDiag)
                #foot = bDiag * leo * yDiag

                foot_tmp = np.reshape(foot,[nr,ns,nr,ns])
                sum_foot_tmp = np.sum(foot_tmp)
                nonzero_foot_tmp = np.count_nonzero(foot_tmp)
                #print(foot_tmp[0][0][1][1])
                #print(foot[0 + ns * 0][1 + ns * 1])
                #check if foot_tmp[i1][j1][i2][j2] is equal
                # to foot[j1 + ns * i1][j2 + ns * i2]

                #if check holds then paste into dset
                print("populating at loop: "+str(x)+ "  populating at region: " +str(j))
                st0 = time.time()
                #footprint_dset[i,:,:,:,:,z] = foot_tmp
                print(j)
                #print(time.sleep(5))
                st1 = time.time()
                stotal = st1-st0
                mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  / 1000
                print( "after writing the usage is (MB):",mem)
                log.write("\nTime taken of populating is: "+str(stotal)+"\n")
                log.write("after writing the usage is (MB):%s \n" % str(mem))
                #log.write("\nsum of abs values of foot: " + str(sum_foot_tmp))
                #log.write("\nnumber of nonzero's of foot: " + str(nonzero_foot_tmp)+"\n")
                print("past populating at:"+str(j))
                #log.write("A foot.shape example of last element in for loop: "+str(foot.shape)+"\n")
                #log.write("A foot_tmp.shape example of last element in for loop: "+str(foot_tmp.shape)+"\n")
                t1 = time.time()
                total = t1-t0
                print("Product b, Leo and y time taken + reshape: "+str(total))
                log.write("Product b, Leo and y + reshape: "+str(total)+"\n")

                #memory cleanup


            for j in range(50):
                t = Thread(target=myfunc, args=(j,y,leo,b))
                t.start()
            del(mat)

            del(h)
            del(b)
            del(y)
            #del(dotLy)
            #del(foot)
            #del(foot_tmp)


            #del(bDiagVector)
            #del(yDiagVector)

            #f.close()
            f.flush()

            f.close()
            log.close()

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



