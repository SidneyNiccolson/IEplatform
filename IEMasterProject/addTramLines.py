import simplejson as json

def getfile():
    #open the file
    #*** > give the path to the file.
    f=open('data/unparsed_tram_allOVdata.geojson', 'r')
   
    #get the content
    F=f.read()
    #split (make an array where each element is determined by an enter)
    # U = F.split('\n')
    

   


    return F

t = getfile()
l = []

parsed_json = json.loads(t)

for feature in parsed_json['features']:
    test = str(feature)
    #print(test)
    if "'OPERATOR': 'GVB'" in test and "'TRANSPORTM': 'TRAM'" in test:
        feature['properties']['popupContent'] = '<legend>TramLine</legend><div class="container" ><table class="table table-hover table-nonfluid" ><thead><tr><th>Total km.</th><th>Amount of Fe</th></tr></thead><tbody><tr><td>200</td><td>23882</td></tr> </tbody></table></div>'
        feature['properties']['colors'] = 'blue'
        l.append(feature)
    '''
    if "'Plusnet_OV': 0.0" in test and "'Comfornet_': 1.0" in test and "'Plusnet_Vo': 0.0" in test and "'Plusnet_Au': 0.0" in test and "'Plusnet_Fi': 1.0" in test and "'Corridor_A': 0.0" in test:

        feature['properties']['popupContent'] = '<legend>TramLine</legend>'
        feature['properties']['colors'] = '#000000'
        l.append(feature)'''
    # for property in feature['properties']:
    #    test = str(property)
     #   print(test)



with open('data/TramLines.geojson', 'w') as json_file:
    json.dump(l, json_file)