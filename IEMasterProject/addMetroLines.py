import simplejson as json

def getfile():
    #open the file
    #*** > give the path to the file.
    f=open('data/unparsed_metro.geojson', 'r')
   
    #get the content
    F=f.read()
    #split (make an array where each element is determined by an enter)
    # U = F.split('\n')
    

   


    return F

t = getfile()
l = []

parsed_json = json.loads(t)
print(parsed_json)
for feature in parsed_json['features']:
    test = str(feature)
    if "'Plusnet_OV': 5.0" in test:
        feature['properties']['popupContent'] = '<legend>MetroLine</legend><div class="container" ><table class="table table-hover table-nonfluid" ><thead><tr><th>Total km.</th><th>Amount of Fe</th></tr></thead><tbody><tr><td>42.5</td><td>4591</td></tr> </tbody></table></div>'
        feature['properties']['colors'] = '#00ff00'
        l.append(feature)
    # for property in feature['properties']:
    #    test = str(property)
     #   print(test)



print(l)
with open('data/MetroLines.geojson', 'w') as json_file:
    json.dump(l, json_file)