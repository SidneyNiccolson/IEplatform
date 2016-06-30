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
    f=open('data/countryTree_exiovisuals.csv', 'r')

   
    #get the content
    F=f.read()

    #split (make an array where each element is determined by an enter)
    U = F.split('\n')

    

   



    #Create empty list !!!!!!! THIS IS THE WORKING LIST OF LIST WE NEED FOR EVERYTHING !!
    data = []


    #fill the empty list with the data (this time split even further by tabs)
    for line in U:
        data.append(line.split('#'))






    return data




    #***generate tree for products
def populate(data):


    print("***Adding products***")
    #add total parent
    #add_parent(data[0][2], data[0][0], data[0][1])
    #remove total from data
    data.pop(0)


    #add children now
    for x in data:
        try:
            parent_id = Country.objects.get(id=x[3])
            id = x[2]

            name = x[0]
            print(name)
            code = x[1]
            lvl = x[5]
            print(lvl)
            print(code)
            #add_child(parent_id, id, name, code)

        except:
            pass


    #go through the data
    print('***Done!! All countries have been added***')

#function that adds the data (offcourse)
def add_child(parent, id, name, slug):
    e, created = Country.objects.get_or_create(parent=parent, id=id, name=name, slug=slug)

    return e

def add_parent(id,name, slug):
    e, created = Country.objects.get_or_create(id=id,name=name, slug=slug)

    return e



# Start execution here!
if __name__ == '__main__':
    print ("Starting IEMasterProject population script...")
	
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IEMasterProject.settings')
    django.setup()
    from ExioVisuals.models import Country
    print("***Opening file****")
    #open the file
    data = getfile()
    #remove first entry
    data.pop(0)
    print("***Header removed****")
    #invoke function to populate the database
    populate(data)


