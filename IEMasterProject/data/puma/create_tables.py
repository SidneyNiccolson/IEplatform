



#open csv file
def getfile(file):
    #open the file
    #*** > give the path to the file.
    f=open(file, 'r',encoding='utf-8', errors='ignore')

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

    return L
#parse csv file
#add HTML elements
def parseFile(content):
    html = '<div class="container" ><table class="table table-hover" ><thead><tr>'
    #create header of table
    header = (content[0])
    for x in header:
        html = html+'<th>%s</th>' % x
    html = html + '</tr></thead>'

    #remove header
    content.pop(0)
    #print(content[2])
    #create body
    html = html + '<tbody>'
    for i,x in enumerate(content):
        try:

            objectNames = (x[0])
            print(x[4])
            stock = x[1]
            averageWeight = x[2]
            averageContent = x[3]
            source = x[4]
            html = html + '<tr>'
            html = html + '<td>%s' % objectNames + '</td>'
            html = html + '<td>%s' % stock + '</td>'
            html = html + '<td>%s' % averageWeight + '</td>'
            html = html + '<td>%s' % averageContent + '</td>'
            html = html + '<td>%s' % source + '</td>'
            html = html + '</tr>'
            print(html)
        except:
            pass
        #
    html = html + '</tbody></table></div>'
    print(html)

    #for x in content:
     #   print(x[0])




#main function
contents = getfile('/home/chai/Documents/public'
                   '.csv')
parseFile(contents)