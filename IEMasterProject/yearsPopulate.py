import os
import sys
import django
#stuff for newer django !





#interface
yearsList = [
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



def populate():
	#below an example to fill in 1 entry
	#add_data("America", "US", 80.5)

    for x in yearsList:
        add_data(x)



#function that adds the data (offcourse)
def add_data(years_list):
    e, created = years.objects.get_or_create(years=years_list)

    return e


# Start execution here!
if __name__ == '__main__':
    print ("Starting IEMasterProject population script...")
	
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IEMasterProject.settings')
    django.setup()
    from ExioVisuals.models import years
    populate()
