import simplejson as json

def getfile():
    #open the file
    #*** > give the path to the file.
    f=open('data/Stadsdelen.geojson', 'r')
   
    #get the content
    F=f.read()
    #split (make an array where each element is determined by an enter)
    # U = F.split('\n')
    

   


    return F

t = getfile()


parsed_json = json.loads(t)
print(parsed_json)
for feature in parsed_json['features']:
    #print(feature)
    for property in feature['properties']['Stadsdeel_']:
        print(property)
        #Centrum
        if property == "A":
            #feature['popupContent'] = 'ADDED_VALUE'
            #add popucontent and its value
            feature['properties']['popupContent'] = '<legend>Centrum</legend><iframe width="259" height="403" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/1YvxRBPGpbFR8uUIIOFlArMz_5EiT8jjl84yldxBxFxg/pubchart?oid=1206100476&amp;format=interactive"></iframe>'
            feature['properties']['colors'] = '#808080'
        #Westpoort
        if property == "B":
            #feature['popupContent'] = 'ADDED_VALUE'
            #add popucontent and its value
            feature['properties']['popupContent'] = '<legend>West-Poort</legend><iframe width="265" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/1YvxRBPGpbFR8uUIIOFlArMz_5EiT8jjl84yldxBxFxg/pubchart?oid=1848626517&amp;format=interactive"></iframe>'
            feature['properties']['colors'] = '#79c19e'
        #West
        if property == "E":
            #feature['popupContent'] = 'ADDED_VALUE'
            #add popucontent and its value
            feature['properties']['popupContent'] = '<legend>West</legend><iframe width="262.5" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/1YvxRBPGpbFR8uUIIOFlArMz_5EiT8jjl84yldxBxFxg/pubchart?oid=391658714&amp;format=interactive"></iframe>'
            feature['properties']['colors'] = 'red'
        #Nieuw-West
        if property == "F":
            #feature['popupContent'] = 'ADDED_VALUE'
            #add popucontent and its value
            feature['properties']['popupContent'] = '<legend>Nieuw-West</legend><iframe width="264.5" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/1YvxRBPGpbFR8uUIIOFlArMz_5EiT8jjl84yldxBxFxg/pubchart?oid=370814143&amp;format=interactive"></iframe>'
            feature['properties']['colors'] = '#ee7f6f'
        #Zuid
        if property == "K":
            #feature['popupContent'] = 'ADDED_VALUE'
            #add popucontent and its value
            feature['properties']['popupContent'] = '<legend>Zuid</legend><iframe width="265" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/1YvxRBPGpbFR8uUIIOFlArMz_5EiT8jjl84yldxBxFxg/pubchart?oid=823082966&amp;format=interactive"></iframe>'
            feature['properties']['colors'] = '#e9d25e'
        #Oost
        if property == "M":
            #feature['popupContent'] = 'ADDED_VALUE'
            #add popucontent and its value
            feature['properties']['popupContent'] = '<legend>Oost</legend><iframe width="264.5" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/1YvxRBPGpbFR8uUIIOFlArMz_5EiT8jjl84yldxBxFxg/pubchart?oid=261871013&amp;format=interactive"></iframe>'
            feature['properties']['colors'] = '#437fa9'
        #Noord
        if property == "N":
            #feature['popupContent'] = 'ADDED_VALUE'
            #add popucontent and its value
            feature['properties']['popupContent'] = '<legend>Noord</legend><iframe width="258.5" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/1YvxRBPGpbFR8uUIIOFlArMz_5EiT8jjl84yldxBxFxg/pubchart?oid=855358084&amp;format=interactive"></iframe>'
            feature['properties']['colors'] = 'green'
        #Zuidoost
        if property == "T":
            #feature['popupContent'] = 'ADDED_VALUE'
            #add popucontent and its value
            feature['properties']['popupContent'] = '<legend>Zuidoost</legend><iframe width="261.5" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/1YvxRBPGpbFR8uUIIOFlArMz_5EiT8jjl84yldxBxFxg/pubchart?oid=222152586&amp;format=interactive"></iframe>'
            feature['properties']['colors'] = '#b200b2'

with open('data/StadsdelenUpdated.geojson', 'w') as json_file:
    json.dump(parsed_json, json_file)