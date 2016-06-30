import os
import sys
import django
import numpy as np
#stuff for newer django !
#open the Exiobase file
def getfile():
    #open the file
    #*** > give the path to the file.
    f=open('data/productUpperLayer.csv', 'r')
    k=open('data/productLowerLayer.csv', 'r')
   
    #get the content
    F=f.read()
    K=k.read()
    #split (make an array where each element is determined by an enter)
    U = F.split('\n')
    I = K.split('\n')
    

   



    #Create empty list !!!!!!! THIS IS THE WORKING LIST OF LIST WE NEED FOR EVERYTHING !!
    L = []
    J = []

    #fill the empty list with the data (this time split even further by tabs)
    for line in U:
        L.append(line.split('#'))

    for line in I:
        J.append(line.split('#'))

    #remove last value (is empty)
    L.pop()
    J.pop()
    J.pop(0)
    #replace '\xa0' in csv file
    for x in L:
        x[0] = x[0].replace(u'\xa0', u' ')

    return L, J





def populate(data, lowerLayer):
	
    #generate tree for product parents

    keyListEurope = []
    #add_parent(1,"Total", "total")
    parentId = Product.objects.get(id=1)
    #create list to match products too
    matchList = []
    ka = []
    #manipulate the data so we can fill in the tree
    for i,x in enumerate(data):
        url = "/"+(x[0][:3])
        urlConstruct = (x[0][:3]).lower()
        id = i+2

        name = (x[0])
        matchList.append(str(id)+"#"+name+ "#"+(x[0][:3]))
        ka.append((x[0][:3]))
        lowerCaseProduct = name.lower()



        #add_child(parentId,id,name,(x[0][:3]))
    #parentId = Category.objects.get(id=1)
    #now create list out ot list of matchList
    #what we want
    #add_child(parentId,61,"Bla")

    matchListUsed = []
    for line in matchList:
        matchListUsed.append(line.split('#'))
    kas = []
    for line in ka:
        kas.append(line.split('#'))

    #print(matchListUsed)

    productList = []
    productListUsed = []
    bla = []

    #start parsing the children (products)
    for i,x in enumerate(lowerLayer):
        productTypeCode = (x[0])
        name = x[0]+" "+x[1]
        id = i+62
        #print(name)
        productList.append(productTypeCode+"#"+str(id)+"#"+name+ "#"+productTypeCode[:3])
        bla.append(productTypeCode[:3])
        #if productTypeCode first three values match something in matchListUsed do something
        #if any(productTypeCode[:3] for s in matchListUsed):
        #if we find a match do something


    for line in productList:
        productListUsed.append(line.split('#'))

    print(productListUsed)
    print(matchListUsed)

    for i,x in enumerate(productListUsed):


        for sublist in matchListUsed:
            kl = x[0][:3]

            #if there is a match in product code first 3 values with the list that we have
            if sublist[2] == kl:
                #print(str(sublist)+"$"+str(x))
                t =  ("Found it!", sublist)
                #parentId = Product.objects.get(id=sublist[0])
                print(sublist)
                #add_child(parentId,x[1],x[2],x[0])



'''
	#If there is a parent! retrieve the parent by object ID
	parentId = Category.objects.get(id=1)
	
	#Start adding the child to the parent!
	add_child(parentId,2,"Shai","shai","/cliff/shai")
	add_child(parentId,3,"Sidney","sidney","/cliff/sidney")
	add_child(parentId,4,"Neville","neville","/cliff/neville")

	#generate parent 2
	add_parent(5,"Martin", "martin", "/martin")
	parentId2 = Category.objects.get(id=5)
	add_child(parentId2,6,"Henna","henna","/martin/henna")
	
	print('Done!!')
'''

#function that adds the data (offcourse)
def add_child(parent, id, name, slug):
    e, created = Product.objects.get_or_create(parent=parent, id=id, name=name, slug=slug)

    return e

def add_parent(id,name, slug):
    e, created = Product.objects.get_or_create(id=id,name=name, slug=slug)

    return e


# Start execution here!
if __name__ == '__main__':
    print ("Starting IEMasterProject population script...")
	
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IEMasterProject.settings')
    django.setup()
    from ExioVisuals.models import Product
    upperLayer,lowerLayer = getfile()

    populate(upperLayer,lowerLayer)
