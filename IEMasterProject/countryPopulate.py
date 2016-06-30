import os
import sys
import django
#stuff for newer django !
#open the Exiobase file
def getfile():
    #open the file
    #*** > give the path to the file.
    f=open('data/countries.csv', 'r')
   
    #get the content
    F=f.read()
    #split (make an array where each element is determined by an enter)
    U = F.split('\n')
    

   



    #Create empty list !!!!!!! THIS IS THE WORKING LIST OF LIST WE NEED FOR EVERYTHING !!
    L = []

    #fill the empty list with the data (this time split even further by tabs)
    for line in U:
        L.append(line.split('#'))
    #remove regional classification for tree
    L.pop()
    L.pop()
    L.pop()
    L.pop()
    L.pop()
    L.pop()
    return L





def populate(data):
	
    #generate tree for Europe
    print(data)
    keyListEurope = []
    dataList = [["Name", "Code", "Id", "Parent_Id"]]
    entry = ["Total", "total",1, "NULL"]
    dataList.append(entry)

    #add_parent(1,"Total", "total", "/total")
    parentId = Country.objects.get(id=1)
    entry = ["Europe","WE",2,1]
    dataList.append(entry)

    entry = ["Middle-East","WM",3,1]
    dataList.append(entry)

    entry = ["America","WL",4,1]
    dataList.append(entry)

    entry = ["Asia-Pacific","WA",5,1]
    dataList.append(entry)

    entry = ["Africa","WF",6,1]
    dataList.append(entry)

    #add_child(parentId,2,"Europe", "europe", "/europe")
    #add_child(parentId,3,"Middle-East", "middleEast", "/middleEast")
    #add_child(parentId,4,"America", "america", "/america")
    #add_child(parentId,5,"Asia-Pacific", "Asia-Pacific", "/asiaPacific")

    europeId = Country.objects.get(id=2)
    middleEastId = Country.objects.get(id=3)
    americaId = Country.objects.get(id=4)
    asiaPacificId = Country.objects.get(id=5)
    for i,x in enumerate(data):

        # if country is europe
        if x[4] == "Europe":
            #give them their respective IDs for the database
            id = i+7
            countryName = (x[1])
            lowerCaseCountry = x[1].lower()
            countryCode = x[0]
            path= "europe/"+lowerCaseCountry
            #print(path)
            entry = [countryName,countryCode,id,2]
            dataList.append(entry)

            #add the children
            #add_child(europeId,id,countryName,countryCode,path)
        # if country is middle east
        if x[3] == "WM":
            #give them their respective IDs for the database
            id = i+7
            countryName = (x[1])
            lowerCaseCountry = x[1].lower()
            countryCode = x[0]
            path= "middleEast/"+lowerCaseCountry
            #print(path)
            entry = [countryName,countryCode,id,3]
            dataList.append(entry)
            #add the children
            #add_child(middleEastId,id,countryName,countryCode,path)
# if country is middle east
        if x[3] == "WL":
            #give them their respective IDs for the database
            id = i+7
            countryName = (x[1])
            lowerCaseCountry = x[1].lower()
            countryCode = x[0]
            path= "america/"+lowerCaseCountry
            entry = [countryName,countryCode,id,4]
            dataList.append(entry)
            #print(path)
            #add the children
            #add_child(americaId,id,countryName,countryCode,path)
# if country is middle east
        if x[3] == "WA":
            #give them their respective IDs for the database
            id = i+7
            countryName = (x[1])
            lowerCaseCountry = x[1].lower()
            countryCode = x[0]
            path= "asiaPacific/"+lowerCaseCountry
            #print(path)
            entry = [countryName,countryCode,id,5]
            dataList.append(entry)
            #add the children
            #add_child(asiaPacificId,id,countryName,countryCode,path)
        if x[3] == "WF":
            #give them their respective IDs for the database
            id = i+7
            countryName = (x[1])
            lowerCaseCountry = x[1].lower()
            countryCode = x[0]
            path= "asiaPacific/"+lowerCaseCountry
            #print(path)
            entry = [countryName,countryCode,id,6]
            dataList.append(entry)
            #add the children
            #add_child(asiaPacificId,id,countryName,countryCode,path)
    print(dataList)

    import csv

    with open("/home/chai/Dropbox/IE/SoftwareDev/IEMasterProject/data/countryTree_exiovisuals.csv", "w") as f:
        writer = csv.writer(f,delimiter='#')
        writer.writerows(dataList)
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
def add_child(parent, id, name, slug, url):
    e, created = Country.objects.get_or_create(parent=parent, id=id, name=name, slug=slug, url=url)

    return e

def add_parent(id,name, slug, url):
    e, created = Country.objects.get_or_create(id=id,name=name, slug=slug, url=url)

    return e


# Start execution here!
if __name__ == '__main__':
    print ("Starting IEMasterProject population script...")
	
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IEMasterProject.settings')
    django.setup()
    from ExioVisuals.models import Country
    data = getfile()
    populate(data)
