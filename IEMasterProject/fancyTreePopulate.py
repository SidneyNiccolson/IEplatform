import os
import sys
import django
#stuff for newer django !





def populate():
	
	#generate parent 1
	add_parent(1,"Cliff", "cliff", "/cliff")
	
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


#function that adds the data (offcourse)
def add_child(parent, id, name, slug, url):
    e, created = Category.objects.get_or_create(parent=parent, id=id, name=name, slug=slug, url=url)

    return e

def add_parent(id,name, slug, url):
    e, created = Category.objects.get_or_create(id=id,name=name, slug=slug, url=url)

    return e


# Start execution here!
if __name__ == '__main__':
    print ("Starting IEMasterProject population script...")
	
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IEMasterProject.settings')
    django.setup()
    from ExioVisuals.models import Category
    populate()
