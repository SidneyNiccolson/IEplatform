import os
import sys
import django
import numpy as np




from string import ascii_uppercase
from collections import OrderedDict

od = OrderedDict((ch, idx) for idx, ch in enumerate(ascii_uppercase, 2))

#stuff for newer django !
#open the Exiobase file
def getfile():
    #open the file
    #*** > give the path to the file.

    #*************************************NACE
    #OPEN NACE DATASET FOR SECTION DATA
    f=open('/home/chai/Downloads/NACE_1_1_20160503_160520.csv', 'r')

   
    #get the content
    F=f.read()

    #split (make an array where each element is determined by an enter)
    U = F.split('\n')

    

   



    #Create empty list !!!!!!! THIS IS THE WORKING LIST OF LIST WE NEED FOR EVERYTHING !!
    L = []


    #fill the empty list with the data (this time split even further by tabs)
    for line in U:
        L.append(line.split('#'))



    #remove last value (is empty)
    L.pop()
    #print(L)
    #replace '\xa0' in csv file
    #for x in L:
    #    x[0] = x[0].replace(u'\xa0', u' ')
    # we only need the data from headers "code" and "description"
    toplayers=[]
    validation1 = []
    sectionIdentification = []
    for i,x in enumerate(L):
        try:
            #this is for retrieving the parents and the code of the product So we can create lower layers
            parent = x[3].replace('"','')[:1]
            childClass = x[2]

            try:
                converted = int(parent)

            except:
                if parent != "":
                    validation1.append(parent)
                    sectionIdentification.append((childClass.replace('"','')+"#"+parent.replace('"','')))
                pass
            #this is for layer construction below of the layer after total which is the 2nd layer
            if len(x[2])==3:
                toplayers.append(x[2].replace('"','')+"#"+x[4].replace('"',''))

        except:
            pass

    validation1 = list(set(validation1))
    SectionIdentification = []
    topLayers = []
    for line in toplayers:
        topLayers.append(line.split('#'))
    for line in sectionIdentification:
        SectionIdentification.append(line.split('#'))
    SectionIdentification.pop(0)
    sectionIdentifier = []
    for x in SectionIdentification:
        try:
            int(x[0])
            sectionIdentifier.append(x)
        except:
            pass


    print("The amount of sections in 2nd level: "+str(len(topLayers)))
    print("The amount of sections in 2nd level used for 3rd level (validation): "+str(len(validation1)))

    #***********************END OF NACE PARSING

    #**********************3rd layer
    f2=open('data/productUpperLayer.csv', 'r')
      #get the content
    F2=f2.read()
    U2 = F2.split('\n')

    L2 = []
    #fill the empty list with the data (this time split even further by tabs)
    for line in U2:
        L2.append(line.split('#'))
    L2.pop()



    for x in L2:
        x[0] = x[0].replace(u'\xa0', u' ')
    #******ENd of 3rd layer

    #******* 4th layer
    k=open('data/productLowerLayer.csv', 'r')
    K=k.read()
    I = K.split('\n')
    J = []

    for line in I:
        J.append(line.split('#'))
    J.pop()
    J.pop(0)

    return topLayers, L2, sectionIdentifier, J




    #***generate tree for products
def populate(topLayer, thirdlayer, sectionIdentifier, fourthLayer):
	


    keyListEurope = []
    #setup the parent here,this is manual, because its not taken from a file.
    add_parent(1,"Total", "total")
    parentId = Product.objects.get(id=1)


    #create list to match products too
    matchList = []
    ka = []
    #manipulate the data so we can fill in the tree
    #this one below is for Sections of 17 which is the 2nd layer
    for i,x in enumerate(topLayer):
        url = "/"+(x[0][:3])
        urlConstruct = (x[0][:3]).lower()
        id = i+2

        name = (x[1])

        lowerCaseProduct = name.lower()



        add_child(parentId,id,name,(x[0]))

    matchList = []
    #the one below is for the 3rd layer
    for i,x in enumerate(thirdlayer):
        id = i +19
        name = (x[0])
        matchList.append(str(id)+"#"+name+ "#"+(x[0][:3]))
        #if there is a match with the 2nd layer add a child
        for sublist in sectionIdentifier:
            productCodes = sublist[0]
            sectionCodes = sublist[1]
            #print(sublist)
            kl = x[0][:3]
            kl2 = kl[1:]
            #to clarify: the following if condition: If productCodes of thirdLayer matches with 2nd layer sectionCode its a match
            if kl2 == productCodes:
                #when the match is there retrieve the ID of the section so we can add them as parent
                #use the dictionary of ID's and subsections to do it
                if (sectionCodes) in od:

                    parentId = Product.objects.get(id=od.get(sectionCodes))


                    add_child(parentId,id,x[0],(x[0][:3]))

    #the one below is for the 4th layer
    matchListUsed = []
    for line in matchList:
        matchListUsed.append(line.split('#'))
    productList = []
    productListUsed = []
    bla = []
     #start parsing the children (products)
    for i,x in enumerate(fourthLayer):
        productTypeCode = (x[0])
        name = x[0]+" "+x[1]
        #as the last id of thirdlayer is 78 we set 78
        id = i+79
        #print(name)
        productList.append(productTypeCode+"#"+str(id)+"#"+name+ "#"+productTypeCode[:3])
        bla.append(productTypeCode[:3])
    for line in productList:
        productListUsed.append(line.split('#'))

    for i,x in enumerate(productListUsed):


        for sublist in matchListUsed:
            kl = x[0][:3]

            #if there is a match in product code first 3 values with the list that we have
            if sublist[2] == kl:
                #print(str(sublist)+"$"+str(x))
                t =  ("Found it!", sublist)
                parentId = Product.objects.get(id=sublist[0])
                print(sublist)
                add_child(parentId,x[1],x[2],x[0])
    '''
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
        print(name)
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
                parentId = Product.objects.get(id=sublist[0])
                add_child(parentId,x[1],x[2],x[0])



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
    topLayer,thirdlayer, sectionIdentifier, fourthLayer = getfile()

    populate(topLayer, thirdlayer, sectionIdentifier, fourthLayer)


