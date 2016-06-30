# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, render
from django.template import RequestContext
from EFactor.forms import PostFormEFactor, PostForm

from django.shortcuts import redirect, render_to_response
from django.shortcuts import redirect, render_to_response
from EFactor.forms import UserCreationForm
from django.forms.formsets import formset_factory
from functools import partial, wraps
from ast import literal_eval
import math, json

# Create your views here.
def DataRetrieval(request):
#retrieve mandatory context
    context = RequestContext(request)
    context_dict = {}
   # TrackFormSet = formset_factory(PostFormEFactor)
         # if this is a POST request we need to process the form data
    #gather the forms.py stuff
    #print(request.encoding)
    #print("encoding above")
    MemberFormSet = formset_factory(wraps(PostFormEFactor)(partial(PostFormEFactor)))
    if request.method == 'POST':

        t = request.POST
        #print(t)
        #get the request info so form1 offcourse
        formset = MemberFormSet(request.POST)
        #print(formset)

        reactant_namelist = []
        reactant_gramlist = []
        listInList = []
        # create a form instance and populate it with data from the request:
        #formset = (request.POST)
        #print(type(formset))
        #print(formset)
        if formset.is_valid():
            for f in formset:
            #cleaning up the data like which form it is etc.
                cd = f.cleaned_data
                names = cd.get('name')

                reactant_namelist.append(names)
                grams = cd.get('grams')
                #check the values of input wether there can be converted (checking for empty fields)
                try:
                #make it explicit that names is strings to prevent unicode issues
                    listInList.append([str(names),float(grams)])
                    reactant_gramlist.append(grams)
                except:
                    rsid = request.POST.get('snp_id')
                    print(rsid)

                    #there are empty fields so return to the page
                    return redirect("../",request)
                #names = cd.


        #print(formset.values())
        #print(reactant_namelist)
        #print(reactant_gramlist)
        #print(listInList)
        return render(request, 'EFactor/ReactantValidate.html',  {'listInList': listInList, 'moleculeType': 'reactant'})

    else:



        return render(request, 'EFactor/Form.html', context_dict)

def DataRetrieval2(request):
    context = RequestContext(request)
    context_dict = {}
   # TrackFormSet = formset_factory(PostFormEFactor)
         # if this is a POST request we need to process the form data
    #gather the forms.py stuff
    MemberFormSet = formset_factory(wraps(PostFormEFactor)(partial(PostFormEFactor)))
    if request.method == 'POST':

        t = request.POST

        reactantData = (request.POST.getlist('reactantData'))

        list = reactantData[0]

        xReactantData = literal_eval(list)
        print(xReactantData)
        numberOfReactants = (request.POST.get('numberOfReactants'))
        print(numberOfReactants)
        #get the request info so form1 offcourse
        formset = MemberFormSet(request.POST)


        product_namelist = []
        product_gramlist = []
        listInList = []
        # create a form instance and populate it with data from the request:
        #formset = (request.POST)
        #print(type(formset))
        #print(formset)
        if formset.is_valid():
            for f in formset:
            #cleaning up the data like which form it is etc.
                cd = f.cleaned_data
                names = cd.get('name')

                product_namelist.append(names)
                grams = cd.get('grams')
                #check the values of input wether there can be converted (checking for empty fields)
                try:
                #make it explicit that names is strings to prevent unicode issues
                    listInList.append([str(names),float(grams)])
                    product_gramlist.append(grams)
                except:
                    rsid = request.POST.get('snp_id')
                    #
                    # print(rsid)
                    #there are empty fields so return to the page
                    return redirect("../",request)
                #names = cd.


        #print(formset.values())
        #print(reactant_namelist)
        #print(reactant_gramlist)
        #print(listInList)
        return render(request, 'EFactor/auxValidate2.html',  {'listInList': listInList, 'moleculeType': 'product', 'numberOfReactants':numberOfReactants, 'reactantData':xReactantData})

    else:



        return render(request, 'EFactor/Form.html', context_dict)

def DataRetrieval3(request):
    context = RequestContext(request)
    context_dict = {}
   # TrackFormSet = formset_factory(PostFormEFactor)
         # if this is a POST request we need to process the form data
    #gather the forms.py stuff
    MemberFormSet = formset_factory(wraps(PostFormEFactor)(partial(PostFormEFactor)))
    if request.method == 'POST':

        t = request.POST

        reactantData = (request.POST.getlist('reactantData'))
        auxData = (request.POST.getlist('auxData'))

        list = reactantData[0]
        list2 = auxData[0]

        xReactantData = literal_eval(list)
        xAuxData = literal_eval(list2)

        numberOfReactants = (request.POST.get('numberOfReactants'))
        numberOfAux = (request.POST.get('numberOfAux'))

        #get the request info so form1 offcourse
        formset = MemberFormSet(request.POST)


        product_namelist = []
        product_gramlist = []
        listInList = []
        # create a form instance and populate it with data from the request:
        #formset = (request.POST)
        #print(type(formset))
        #print(formset)
        if formset.is_valid():
            for f in formset:
            #cleaning up the data like which form it is etc.
                cd = f.cleaned_data
                names = cd.get('name')

                product_namelist.append(names)
                grams = cd.get('grams')
                #check the values of input wether there can be converted (checking for empty fields)
                try:
                #make it explicit that names is strings to prevent unicode issues
                    listInList.append([str(names),float(grams)])
                    product_gramlist.append(grams)
                except:

                    rsid = request.POST.get('snp_id')
                    #
                    # print(rsid)
                    #there are empty fields so return to the page
                    return redirect("../",request)


        #print(formset.values())
        #print(reactant_namelist)
        #print(reactant_gramlist)
        #print(listInList)
        return render(request, 'EFactor/solvValidate2.html',  {'listInList': listInList, 'moleculeType': 'solvent', 'numberOfReactants':numberOfReactants, 'reactantData':xReactantData, 'numberOfAux':numberOfAux, 'auxData':xAuxData})

    else:



        return render(request, 'EFactor/Form.html', context_dict)


def checkSNP(request):
    if 'rsid' in request.GET:

        rsid = request.GET['rsid']
        try:
            int(rsid)
        except:
            return redirect("../",request)
        ArticleFormSet = formset_factory(PostFormEFactor)
        formset = ArticleFormSet()

        value = int(rsid)
        if value == 0 or value > 30 or value < 1:
            return redirect("../",request)

        formset = formset_factory(wraps(PostFormEFactor)(partial(PostFormEFactor)), extra=value)

        # array = request.GET['array']

        return render(request, 'EFactor/reactantForm.html', {'snp_id': rsid, 'formset':formset})
    else:
        return HttpResponse('You entered a value that is not allowed or did not fill in all data, return to the previous page!')




def create_user2(request):
    #MemberFormSet = formset_factory(wraps(PostFormEFactor)(partial(PostFormEFactor)))
    if request.method == 'POST':

        #get the r equest info so form1 offcourse
        formset = (request.POST)

        #

        # print(formset)
        #print(formset.getlist('listInList'))
        print("what goingon2")
        #print(formset)
        reactantData = (request.POST.getlist('reactantData'))

        test = reactantData[0]

        xReactantData = literal_eval(test)


        #print(type(reactantData.encode('ascii')))

        #t = (map(literal_eval, reactantData))
        #x = (map(literal_eval, t))


        #print(reactantData)
        if not reactantData:
            #print("TEST")
            st =  "None entered"
            return render(request, 'EFactor/inputAm.cleaned_dataountAuxiliaries.html', {'reactantData': xReactantData})
        else:

             #this may cause errors later not so sure about the encoding part of web pages

            return render(request, 'EFactor/inputAmountAuxiliaries.html', {'reactantData': xReactantData, 'Tag': len(xReactantData) })

    else:
        #handle the new form after the reactants namely solvents
        return HttpResponse('You entered a value that is not allowed or did not fill in all data, return to the previous page!')


def create_user3(request):
    #MemberFormSet = formset_factory(wraps(PostFormEFactor)(partial(PostFormEFactor)))
    if request.method == 'POST':

        #get the r equest info so form1 offcourse
        formset = (request.POST)

        #

        # print(formset)
        #print(formset.getlist('listInList'))
        print("what goingon3")



        #print(formset)
        reactantData = (request.POST.getlist('reactantData'))

        test = reactantData[0]
        auxData = (request.POST.getlist('auxData'))
        xReactantData = literal_eval(test)

        test2 = auxData[0]
        xAuxData = literal_eval(test2)
        print(xReactantData)
        print(xAuxData)
        #print(type(reactantData.encode('ascii')))

        #t = (map(literal_eval, reactantData))
        #x = (map(literal_eval, t))

        #print(reactantData)
        if not xReactantData:
            #print("TEST")
            st =  "None entered"
            return render(request, 'EFactor/inputAmountAuxiliaries.html', {'reactantData': xReactantData, 'Tag': len(xReactantData)})
        else:

             #this may cause errors later not so sure about the encoding part of web pages

            #return render(request, 'EFactor/inputAmountAuxiliaries.html', {'reactantData': xReactantData, 'Tag': len(xReactantData) })
                return render(request, 'EFactor/inputAmountSolvent.html', {'reactantData':xReactantData,'Tag': len(xReactantData),'auxData':xAuxData, 'Tag2': len(xAuxData) })

    else:
        #handle the new form after the reactants namely solvents
        #return HttpResponse('you are here')

                return HttpResponse('You entered a value that is not allowed or did not fill in all data, return to the previous page!')


def create_user4(request):
    #MemberFormSet = formset_factory(wraps(PostFormEFactor)(partial(PostFormEFactor)))
    if request.method == 'POST':

        #get the r equest info so form1 offcourse
        formset = (request.POST)

        #

        # print(formset)
        #print(formset.getlist('listInList'))
        print("what goingon4")
        #print(formset)
        reactantData = (request.POST.getlist('reactantData'))
        test = reactantData[0]
        auxData = (request.POST.getlist('auxData'))
        solvData = (request.POST.getlist('solvData'))
        xReactantData = literal_eval(test)

        test2 = auxData[0]
        test3 = solvData[0]
        xAuxData = literal_eval(test2)
        xSolvData = literal_eval(test3)


        ArticleFormSet = formset_factory(PostFormEFactor)
        formset = ArticleFormSet()
        #amount of products

        #also retrieve the post request with relevant data




        formset = formset_factory(wraps(PostFormEFactor)(partial(PostFormEFactor)), extra=1)

        #print(reactantData)
        if not xReactantData:
            #print("TEST")
            st =  "None entered"
            return render(request, 'EFactor/inputAmountSolvent.html', {'reactantData':xReactantData,'Tag': len(xReactantData),'auxData':xAuxData, 'Tag2': len(xAuxData) })
        else:

             #this may cause errors later not so sure about the encoding part of web pages

            #return render(request, 'EFactor/inputAmountAuxiliaries.html', {'reactantData': xReactantData, 'Tag': len(xReactantData) })
                return render(request, 'EFactor/prodForm.html', {'formset':formset,'reactantData':xReactantData,'Tag': len(xReactantData),'auxData':xAuxData, 'Tag2': len(xAuxData), 'Tag3':len(xSolvData), 'solvData':xSolvData })

    else:
        #handle the new form after the reactants namely solvents
        #return HttpResponse('you are here')

                return HttpResponse('You entered a value that is not allowed or did not fill in all data, return to the previous page!')


def auxiliaries(request):
    if request.method == 'POST':
        #print(request.POST)
        #print("above")
        reactantData = (request.POST.getlist('reactantData'))
        #print(reactantData)
        rsid = (request.POST.get('rsid2'))
        numberOfReactants = (request.POST.get('numberOfReactants'))
        list = reactantData[0]

        xReactantData = literal_eval(list)



        xReactantData = literal_eval(list)
        try:
            int(rsid)

        except:
            return redirect("../",request)

        ArticleFormSet = formset_factory(PostFormEFactor)
        formset = ArticleFormSet()
        #amount of products
        value =  int(rsid)
        #also retrieve the post request with relevant data
        if  value > 30 or value < 0:
                return redirect("../",request)



        formset = formset_factory(wraps(PostFormEFactor)(partial(PostFormEFactor)), extra=value)



        return render(request, 'EFactor/auxForm.html', {'snp_id2': rsid, 'formset':formset, 'numberOfReactants':numberOfReactants, 'reactantData': xReactantData})
    return HttpResponse('You entered a value that is not allowed or did not fill in all data, return to the previous page!')

def solvents(request):
    if request.method == 'POST':
        #print(request.POST)
        #print("above")
        reactantData = (request.POST.getlist('reactantData'))
        #print(reactantData)
        rsid = (request.POST.get('rsid2'))
        numberOfReactants = (request.POST.get('numberOfReactants'))

        list = reactantData[0]
        auxData = (request.POST.getlist('auxData'))
        #print(reactantData)
        rsid = (request.POST.get('rsid2'))
        numberOfAux = (request.POST.get('numberOfAuxiliaries'))
        list2 = auxData[0]
        xReactantData = literal_eval(list)
        xAuxData = literal_eval(list2)

        try:
            int(rsid)
        except:
            return redirect("../",request)


        ArticleFormSet = formset_factory(PostFormEFactor)
        formset = ArticleFormSet()
        #amount of products
        value =  int(rsid)
        if  value > 30 or value < 0:
                return redirect("../",request)

        #also retrieve the post request with relevant data




        formset = formset_factory(wraps(PostFormEFactor)(partial(PostFormEFactor)), extra=value)



        return render(request, 'EFactor/solventForm.html', {'snp_id2': rsid, 'formset':formset, 'numberOfReactants':numberOfReactants, 'reactantData': xReactantData, 'numberOfAux': numberOfAux, 'xAuxData': xAuxData})
    return HttpResponse('You entered a value that is not allowed or did not fill in all data, return to the previous page!')



def create_user(request):



    return render_to_response("EFactor/inputAmountReactantForm.html",request)

def home(request):



    return render_to_response("EFactor/home.html",request)

def dropTest(request):
    if request.method == 'POST':
        form = (request.POST)
        print(form)

        answer = (request.POST.getlist('reactant'))
        reactantData = (request.POST.getlist('reactantData'))

        list = reactantData[0]

        xReactantData = literal_eval(list)
        names=[]
        grams=[]
        for x in xReactantData:
            names.append(x[0])
            grams.append(x[1])

        xdata = names
        ydata = grams
        chartdata = {'x': xdata, 'y': ydata}
        charttype = "pieChart"
        chartcontainer = 'piechart_container'
        data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
    }
}
    return render_to_response('EFactor/home.html', data)
def Calculation(request):
    MemberFormSet = formset_factory(wraps(PostFormEFactor)(partial(PostFormEFactor)))
    if request.method == 'POST':
        #RETRIEVE ALL DATA before we can calculate
        reactantData = (request.POST.getlist('reactantData'))
        test = reactantData[0]
        auxData = (request.POST.getlist('auxData'))
        solvData = (request.POST.getlist('solvData'))
        xReactantData = literal_eval(test)

        test2 = auxData[0]
        test3 = solvData[0]
        xAuxData = literal_eval(test2)
        xSolvData = literal_eval(test3)

        print(xReactantData)
        print(xAuxData)
        print(xSolvData)
        formset = MemberFormSet(request.POST)


        product_namelist = []
        product_gramlist = []
        listInList = []
        # create a form instance and populate it with data from the request:
        #formset = (request.POST)
        #print(type(formset))
        #print(formset)
        if formset.is_valid():
            for f in formset:
            #cleaning up the data like which form it is etc.
                cd = f.cleaned_data
                names = cd.get('name')
                product_namelist.append(names)
                grams = cd.get('grams')
                #check the values of input wether there can be converted (checking for empty fields)
                try:
                #make it explicit that names is strings to prevent unicode issues
                    listInList.append([str(names),float(grams)])
                    product_gramlist.append(grams)

                except:


                    rsid = request.POST.get('snp_id')
                    #
                    # print(rsid)
                    #there are empty fields so return to the page
                    return redirect("../",request)             #names = cd.
        else:
            return redirect("../",request)                 #names = cd.

        #just get the product in grams and the name seperate (its a list I know but never mind this as this is not the full version)
        for x in listInList:
            name_of_product = x[0]
            grams_of_product = x[1]

        #get all reactants in grams, for calculation measures
        reactantResult = calcIndividual(xReactantData,grams_of_product,"**All Reactants")
        auxResult = calcAuxSolv(xAuxData,grams_of_product,"**All auxiliaries")
        solvResult = calcAuxSolv(xSolvData,grams_of_product,"**All solvents")

        #to lazy to create a function for this
        reactantWeight = []
        auxWeight = []
        solvWeight = []
        for x in xReactantData:
            reactantWeight.append(x[1])
        for x in xAuxData:
            auxWeight.append(x[1])
        for x in xSolvData:
            solvWeight.append(x[1])

        totalGrams = sum(reactantWeight)+sum(auxWeight)+sum(solvWeight)

        totalResult = (totalGrams)/grams_of_product

        print(reactantResult)
        print(auxResult)
        print(solvResult)
        print("basg")

        return render_to_response("EFactor/results.html", {'total':totalResult,'reactantResults': reactantResult, 'numberOfReactants': len(xReactantData),'auxResults':auxResult, 'numberOfAux': len(xAuxData), 'solvResults':solvResult, 'numberOfSolv':len(xSolvData) })

    else:
        return HttpResponse('You entered a value that is not allowed or did not fill in all data, return to the previous page!')


def calcIndividual(listData, productInGrams, type):
    gramsListData = []
    for x in listData:
        p = float(x[1])
        gramsPretty = (math.ceil( p*10)/10)
        print(gramsPretty)
        gramsListData.append(gramsPretty)


    totalType = (sum(gramsListData))




        #EFACTOR REACTANT TOTAL
    totalEfactorType = (totalType-productInGrams)/productInGrams
    totalEfactorType = (math.ceil( totalEfactorType*10)/10)

    answers = [type+'#'+str(totalType)+'#'+str(totalEfactorType)]


    for x in listData:
        eFactor = (float(x[1])-float(productInGrams))/productInGrams


        p = float(x[1])
        gramsPretty = (math.ceil( p*10)/10)
        eFactor =  (gramsPretty-productInGrams)/productInGrams
        eFactor = (math.ceil( eFactor*10)/10)
            #make list and for later a csv kind of thing:
        csvRows = x[0]+ '#' + str(gramsPretty)+'#' + str(eFactor)
        answers.append(csvRows)

    results =[]
         # make a list in list with country and year
    for line in answers:
        results.append(line.split('#'))


    return results

def calcAuxSolv(listData, productInGrams, type):


    gramsListData = []
    for x in listData:
        p = float(x[1])
        gramsPretty = (math.ceil( p*10)/10)
        print(gramsPretty)
        gramsListData.append(gramsPretty)
    totalType = (sum(gramsListData))

        #EFACTOR REACTANT TOTAL
    totalEfactorType = (totalType)/productInGrams

    totalEfactorType = (math.ceil( totalEfactorType*10)/10)
    answers = [type+'#'+str(totalType)+'#'+str(totalEfactorType)]
    for x in listData:
        p = float(x[1])
        gramsPretty = (math.ceil( p*10)/10)
        eFactor = (gramsPretty)/productInGrams
        eFactor = (math.ceil( eFactor*10)/10)
            #make list and for later a csv kind of thing:
        csvRows = x[0]+ '#' + str(gramsPretty)+'#' + str(eFactor)
        answers.append(csvRows)

    results =[]
         # make a list in list with country and year
    for line in answers:
        results.append(line.split('#'))


    return results


#--------------------------------------------------OTHER PART OF ANALYSIS (CONCENTRATIONS)
def concentration(request):
    return render(request,"EFactor/ConcentrationFirst.html")

#build the form for all reactants,aux,solvents but first do some validation etc.
def buildForm(request):
    #make sure every variable is send through the HTTP get request
    if 'reactantAmount' and 'auxAmount' and 'solvAmount' in request.GET:
        #now get the variables out of there
        rReactant = request.GET['reactantAmount']
        rAux = request.GET['auxAmount']
        rSolv = request.GET['solvAmount']
        #convert to integers instead of strings
        try:
            int(rReactant)
            int(rAux)
            int(rSolv)
        #redirect to the page in case that non-integers where send
        except:
            return redirect("./",request)
        #convert again?!?
        rReactant = int(rReactant)
        rAux = int(rAux)
        rSolv = int(rSolv)
        #do check on amount of inputs (we dont want to0 much to render as that will break the app or the server maybe)
        if rReactant == 0 or rReactant > 30 or rReactant < 1:
            return redirect("./",request)
        if  rAux > 30 or rAux < 0:
                return redirect("./",request)
        if  rSolv > 30 or rSolv < 0:
                return redirect("./",request)

        #NOW that everything is validated, built the form
        reactant_formset = formset_factory(wraps(PostForm)(partial(PostForm)), extra=rReactant)
        reactForm = reactant_formset(prefix="reactant")
        aux_formset = formset_factory(wraps(PostForm)(partial(PostForm)), extra=rAux)
        auxForm = aux_formset(prefix="aux")
        solv_formset = formset_factory(wraps(PostForm)(partial(PostForm)), extra=rSolv)
        solvForm = solv_formset(prefix="solv")
        prod_formset = formset_factory(wraps(PostForm)(partial(PostForm)), extra=1)
        prodForm = prod_formset(prefix="prod")
        #send the data
        return render(request, 'EFactor/allForm.html', {'reactant_formset': reactForm,'aux_formset': auxForm,'solv_formset': solvForm, 'prod_formset':  prodForm })



    return HttpResponse("You are not allowed to enter this page directly, please return!")

def calculateItAll(request):
    #Start retrieving all data from the request
    MemberFormSet = formset_factory(wraps(PostForm)(partial(PostForm)))

    #PREFIX IS THE WAY YOU CAN USE MULTIPLE FORMS
    if request.method == 'POST':

            formsetReactant = MemberFormSet(request.POST , prefix='reactant')


            formsetAux =  MemberFormSet(request.POST, prefix='aux')
            formsetSolv =  MemberFormSet(request.POST, prefix='solv')
            formsetProd =  MemberFormSet(request.POST, prefix='prod')

            #start retrieving it all in list in list form
            #listInList = []
            # create a form instance and populate it with data from the request:

            reactantList = []
            auxList = []
            solvList = []
            prodList = []
            if formsetProd.is_valid() and formsetReactant.is_valid() and formsetAux.is_valid()and formsetSolv.is_valid():
                for f in formsetReactant:
                    cd = f.cleaned_data
                    names = cd.get('name')
                    mm = cd.get('molarmass')
                    cc = cd.get('concentration')
                    try:
                #make it explicit that names is strings to prevent unicode issues
                        reactantList.append([str(names),float(mm), float(cc)])

                    except:
                    #there are empty fields so return to the page
                        return redirect("./",request)



                for f in formsetProd:
                    cd = f.cleaned_data
                    names = cd.get('name')
                    mm = cd.get('molarmass')
                    cc = cd.get('concentration')
                    try:
                #make it explicit that names is strings to prevent unicode issues
                        prodList.append([str(names),float(mm), float(cc)])

                    except:
                    #there are empty fields so return to the page
                        return redirect("./",request)
                for f in formsetAux:
                    cd = f.cleaned_data
                    names = cd.get('name')
                    mm = cd.get('molarmass')
                    cc = cd.get('concentration')
                    try:
                #make it explicit that names is strings to prevent unicode issues
                        auxList.append([str(names),float(mm), float(cc)])

                    except:
                    #there are empty fields so return to the page
                        return redirect("./",request)

                for f in formsetSolv:
                    cd = f.cleaned_data
                    names = cd.get('name')
                    mm = cd.get('molarmass')
                    cc = cd.get('concentration')
                    try:
                #make it explicit that names is strings to prevent unicode issues
                        solvList.append([str(names),float(mm), float(cc)])

                    except:
                    #there are empty fields so return to the page
                        return redirect("./",request)
                #do the calculatons noww!!
                reactant_convert = convert(reactantList)
                prod_convert = convert(prodList)
                aux_convert = convert(auxList)
                solv_convert = convert(solvList)
                #send them all to another function that will do calculations and render it as output
                dict = calc_and_render(reactant_convert,prod_convert,aux_convert,solv_convert)
                totalResult = (dict.get('totalResult'))
                reactantResult = (dict.get('reactantResult'))
                auxResult = (dict.get('auxResult'))
                solvResult = (dict.get('solvResult'))
                #formatting!!
                totalResult=(math.ceil(totalResult*10)/10)

                cleanedReactant = []


                return render_to_response("EFactor/results.html", {'total':totalResult,'reactantResults': reactantResult, 'numberOfReactants': len(reactantList),'auxResults':auxResult, 'numberOfAux': len(auxList), 'solvResults':solvResult, 'numberOfSolv': len(solvList) })

    else:
        return HttpResponse("You are not allowed to enter this page directly, please return!")
                    #print(k)



        #get the r equest info so form1 offcourse
        #formset = MemberFormSet(request.POST)

    return HttpResponse("You are not allowed to enter this page directly, please return!!!")

#convert all the mol masses and concentrations to grams (Assuming a Volume of 1 liter)
def convert(listData):
    #total Efactor


    gramsListData = []
    for x in listData:
        name = x[0]
        grams = x[1]*x[2]
        csvRows = name + '#' + str(grams)
        gramsListData.append(csvRows)


    results =[]
         # make a list in list with country and year
    for line in gramsListData:
        results.append(line.split('#'))


        #EFACTOR REACTANT TOTAL
    #totalEfactorType = (totalType-productInGrams)/productInGrams

    return results


def calc_and_render(reactant,product,aux,solv):
        for x in product:
            name_of_product = x[0]
            grams_of_product = float(x[1])
     #get all reactants in grams, for calculation measures
        reactantResult = calcIndividual(reactant,grams_of_product,"**All Reactants")
        auxResult = calcAuxSolv(aux,grams_of_product,"**All auxiliaries")
        solvResult = calcAuxSolv(solv,grams_of_product,"**All solvents")

        #to lazy to create a function for this
        reactantWeight = []
        auxWeight = []
        solvWeight = []
        for x in reactant:

            reactantWeight.append(float(x[1]))
        for x in aux:
            auxWeight.append(float(x[1]))
        for x in solv:
            solvWeight.append(float(x[1]))

        totalGrams = sum(reactantWeight)+sum(auxWeight)+sum(solvWeight)



        totalResult = (totalGrams)/grams_of_product



        return {"totalResult":totalResult,"reactantResult":reactantResult,"auxResult": auxResult,"solvResult": solvResult}
