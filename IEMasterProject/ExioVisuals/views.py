from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate, login,logout
from ExioVisuals.models import GhgEmissions, Product, Country, Substance
from django.http import HttpResponseForbidden

from django.shortcuts import get_object_or_404
import random
import datetime,time
from ast import literal_eval
from django.forms.formsets import formset_factory
from ExioVisuals.forms import PostFormEFactor, reloadForm, modes, yearsSingleSelect, yearsMultipleSelect
from functools import partial, wraps
import json, simplejson
from django.shortcuts import render, get_object_or_404, redirect
from ExioVisuals.forms import ProductSelectionForm, CountrySelectionForm, SubstanceSelectionForm
from IEMasterProject.widgets import get_tree
from ExioVisuals.models import Selection
import numpy as np
import h5py



#number of years
nt = 17
#number of regions
nr = 49
#number of sectors
ns = 200
#number of final demand categories
nf = 1
#households
nh = 7
# Create your views here.
#Homepage code
def home(request):
    context = RequestContext(request)


    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    nb_element = 150
    xdata = range(nb_element)
    xdata = list(map(lambda x: start_time + x * 1000000000, xdata))
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = list(map(lambda x: x * 2, ydata))

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie1 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
    }
    extra_serie2 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
    }
    chartdata = {'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie1, 'kwargs1': { 'color': '#778899' },
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie2, 'kwargs2': { 'color': '#b22121' },
    }

    charttype = "lineChart"
    chartcontainer = 'linechart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y %H',
            'tag_script_js': True,
            'jquery_on_ready': False,
        },'sample_datas' : [
    {"value": 100, "name": "alpha"      },
    {"value": 70, "name": "beta"},
            {"value": 30, "name": "Test"},
            {"value": 10, "name": "bla"},

  ]
    }
    #print(data)
    return render_to_response('ExioVisuals/home.html', data, context)





    #return render_to_response('ExioVisuals/home.html', {'data': data})

    #retrieve mandatory context
def treemap(request):

    #treemap stuff
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    nb_element = 150
    xdata = range(nb_element)
    xdata = list(map(lambda x: start_time + x * 1000000000, xdata))
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = list(map(lambda x: x * 2, ydata))

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie1 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
    }
    extra_serie2 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
    }
    chartdata = {'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie1, 'kwargs1': { 'color': '#778899' },
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie2, 'kwargs2': { 'color': '#b22121' },
    }
    charttype = "lineChart"
    chartcontainer = 'linechart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y %H',
            'tag_script_js': True,
            'jquery_on_ready': False,
        },'sample_datas' : [
    {"value": 100, "name": "alpha"      },
    {"value": 80, "name": "beta"},
            {"value": 60, "name": "gamma"},
            {"value": 40, "name": "delta"},
             {"value": 20, "name": "epsilon"},

  ]
    }
    return render(request,'ExioVisuals/treemap.html', data)
#global tab code

def distributionView(request):

    #by default mode is :
    mode = 0
    #Retrieve skeleton of forms-------------------------------------------------------------
    formTree = ProductSelectionForm(request.POST or None)
    formTreeCountry = CountrySelectionForm(request.POST or None)
    formTreeSubstance = SubstanceSelectionForm(request.POST or None)

    print("wher")

    MemberFormSet = formset_factory(wraps(PostFormEFactor)(partial(PostFormEFactor)))

 #retrieve filter data!
    if request.method == 'POST':

        #First and foremost try to retrieve any mode (decomposition data)
        mode = (request.POST.get('y'))
        if mode != None:
            print("Entering mode:" +mode)
            if mode=="selectA":
                #call all the necessary forms
                modeFormSet = modes(initial={'selection': 'selectA'})
                yearsSelect = yearsSingleSelect(initial={'Year': '2011'})
                #normally we want to load data here that makes sense of the selected mode
                xdata, ydata = retrieveData()

                #set title,description, size
                title = "Absolute footprint of consumption split by consumed product category"
                description = ""

                countryDataReady = generateTrees(formTreeCountry)
                parsed_json = json.loads(countryDataReady)


                print(parsed_json)
                #print(countryDataReady)

                #parsed_json[0]['selected'] = True
                #countryDataReady = json.dumps(parsed_json)


                #countryDataReady = (countryDataReady.replace("'", '"'))
                #call pieChart function
                pieData = pieChart(xdata,ydata, title , description)
             #updata dictionary for filter options: form skeletons
                pieData.update({'modeForm':modeFormSet})

                pieData.update({'yearsMode1':yearsSelect})
                pieData.update({'sourceData': generateTrees(formTree)})
                pieData.update({'countryDataReady': countryDataReady})
                pieData.update({'substanceDataReady': generateTrees(formTreeSubstance)})
                notification = '<div class="alert alert-warning"><strong><span class="glyphicon glyphicon-alert" aria-hidden="true"></span></strong> Only single selection is possible, because of selected mode.</div>'
                #create select modes for fancyTree : so single select or multiple

                pieData.update({'mode_tree4': 1, 'warning_8':notification})
                pieData.update({'mode_tree': 3, 'warning_6':""})
                pieData.update({'mode_tree2': 1, 'warning_5':notification})
                pieData.update({'mode_tree3': 1, 'warning_7':notification})
                pieData.update({'mode_tree6': 1, 'warning_10':notification})
                #pieData.update({'warning': '<div class="alert alert-warning"><strong><span class="glyphicon glyphicon-alert" aria-hidden="true"></span></strong> Only single selection is possible, because of selected mode.</div>'})

                #send signal for popup
                popup = 1
                pieData.update({'popup': popup})
                pieData.update({'userSelectMode': "Absolute footprint of consumption split by consumed product category"})
                return render(request,"ExioVisuals/distribution.html", pieData)
            if mode=="selectB":
                #call all the necessary forms
                modeFormSet = modes(initial={'selection': 'selectB'})
                yearsSelect = yearsSingleSelect(initial={'Year': '2011'})
                #normally we want to load data here that makes sense of the selected mode
                xdata, ydata = retrieveData()

                #set title,description, size
                title = "Absolute footprint of consumption split by consuming region"
                description = ""

                countryDataReady = generateTrees(formTreeCountry)
                parsed_json = json.loads(countryDataReady)


                print(parsed_json)
                #print(countryDataReady)

                #parsed_json[0]['selected'] = True
                #countryDataReady = json.dumps(parsed_json)


                #countryDataReady = (countryDataReady.replace("'", '"'))
                #call pieChart function
                pieData = pieChart(xdata,ydata, title , description)
             #updata dictionary for filter options: form skeletons
                pieData.update({'modeForm':modeFormSet})

                pieData.update({'yearsMode1':yearsSelect})
                pieData.update({'sourceData': generateTrees(formTree)})
                pieData.update({'countryDataReady': countryDataReady})
                pieData.update({'substanceDataReady': generateTrees(formTreeSubstance)})
                notification = '<div class="alert alert-warning"><strong><span class="glyphicon glyphicon-alert" aria-hidden="true"></span></strong> Only single selection is possible, because of selected mode.</div>'
                #create select modes for fancyTree : so single select or multiple

                pieData.update({'mode_tree4': 1, 'warning_8':notification})
                pieData.update({'mode_tree': 1, 'warning_6':notification})
                pieData.update({'mode_tree2': 3, 'warning_5':""})
                pieData.update({'mode_tree3': 1, 'warning_7':notification})
                pieData.update({'mode_tree6': 1, 'warning_10':notification})
                #pieData.update({'warning': '<div class="alert alert-warning"><strong><span class="glyphicon glyphicon-alert" aria-hidden="true"></span></strong> Only single selection is possible, because of selected mode.</div>'})

                #send signal for popup
                popup = 1
                pieData.update({'popup': popup})
                pieData.update({'userSelectMode': "Absolute footprint of consumption split by consuming region"})
                return render(request,"ExioVisuals/distribution.html", pieData)
            if mode=="selectD":
                #call all the necessary forms
                modeFormSet = modes(initial={'selection': 'selectD'})
                yearsSelect = yearsSingleSelect(initial={'Year': '2011'})

                xdata, ydata = retrieveData()

                #set title,description, size
                title = "Absolute footprint of consumption split by country where impact occurs"
                description = ""

                countryDataReady = generateTrees(formTreeCountry)
                parsed_json = json.loads(countryDataReady)
                #start selecting some nodes of the tree (some countries)
                '''
                for i in parsed_json:
                    #print(i)
                    #i['children']['selected'] = "true"
                    for x in i['children']:
                        print(" gfgg")
                        for y in x['children']:
                            (y['selected']) = "true"

                print(parsed_json)
                for i in parsed_json:
                    #if i['title'] == "Total":
                    #    i['unselectable'] = True
                    #print(i)
                    #i['children']['selected'] = "true"
                    for x in i['children']:

                        if x['children'] != True:
                            x['unselectable'] = True
                        #for y in x['children']:
                         #   (y['selected']) = "true"
                '''
                print(parsed_json)
                #print(countryDataReady)

                #parsed_json[0]['selected'] = True
                #countryDataReady = json.dumps(parsed_json)


                #countryDataReady = (countryDataReady.replace("'", '"'))
                #call pieChart function
                pieData = pieChart(xdata,ydata, title , description)
             #updata dictionary for filter options: form skeletons
                pieData.update({'modeForm':modeFormSet})

                pieData.update({'yearsMode1':yearsSelect})
                pieData.update({'sourceData': generateTrees(formTree)})
                pieData.update({'countryDataReady': countryDataReady})
                pieData.update({'substanceDataReady': generateTrees(formTreeSubstance)})
                notification = '<div class="alert alert-warning"><strong><span class="glyphicon glyphicon-alert" aria-hidden="true"></span></strong> Only single selection is possible, because of selected mode.</div>'
                #create select modes for fancyTree : so single select or multiple

                pieData.update({'mode_tree4': 1, 'warning_8':notification})
                pieData.update({'mode_tree': 1, 'warning_6':notification})
                pieData.update({'mode_tree2': 1, 'warning_5':notification})
                pieData.update({'mode_tree3': 3, 'warning_7':""})
                pieData.update({'mode_tree6': 1, 'warning_10':notification})
                #send signal for popup
                popup = 1
                pieData.update({'popup': popup})
                pieData.update({'userSelectMode': "Absolute footprint of consumption split by country where impact occurs"})
                return render(request,"ExioVisuals/distribution.html", pieData)
            if mode=="selectC":
                #call all the necessary forms
                modeFormSet = modes(initial={'selection': 'selectC'})
                yearsSelect = yearsSingleSelect(initial={'Year': '2011'})
                #normally we want to load data here that makes sense of the selected mode
                xdata, ydata = retrieveData()

                #set title,description, size
                title = "Absolute footprint of consumption split by sector where impact occurs"
                description = ""

                countryDataReady = generateTrees(formTreeCountry)
                parsed_json = json.loads(countryDataReady)


                print(parsed_json)
                #print(countryDataReady)

                #parsed_json[0]['selected'] = True
                #countryDataReady = json.dumps(parsed_json)


                #countryDataReady = (countryDataReady.replace("'", '"'))
                #call pieChart function
                pieData = pieChart(xdata,ydata, title , description)
             #updata dictionary for filter options: form skeletons
                pieData.update({'modeForm':modeFormSet})

                pieData.update({'yearsMode1':yearsSelect})
                pieData.update({'sourceData': generateTrees(formTree)})
                pieData.update({'countryDataReady': countryDataReady})
                pieData.update({'substanceDataReady': generateTrees(formTreeSubstance)})
                notification = '<div class="alert alert-warning"><strong><span class="glyphicon glyphicon-alert" aria-hidden="true"></span></strong> Only single selection is possible, because of selected mode.</div>'
                #create select modes for fancyTree : so single select or multiple

                pieData.update({'mode_tree4': 3, 'warning_8':""})
                pieData.update({'mode_tree': 1, 'warning_6':notification})
                pieData.update({'mode_tree2': 1, 'warning_5':notification})
                pieData.update({'mode_tree3': 1, 'warning_7':notification})
                pieData.update({'mode_tree6': 1, 'warning_10':notification})
                #pieData.update({'warning': '<div class="alert alert-warning"><strong><span class="glyphicon glyphicon-alert" aria-hidden="true"></span></strong> Only single selection is possible, because of selected mode.</div>'})

                #send signal for popup
                popup = 1
                pieData.update({'popup': popup})
                pieData.update({'userSelectMode': "Absolute footprint of consumption split by sector where impact occurs"})
                return render(request,"ExioVisuals/distribution.html", pieData)
            if mode=="selectF":
                #call all the necessary forms
                modeFormSet = modes(initial={'selection': 'selectF'})
                yearsSelect = yearsMultipleSelect
                #normally we want to load data here that makes sense of the selected mode
                xdata, ydata = retrieveData()

                #set title,description, size
                title = "Absolute footprint of consumption split by year"
                description = ""

                countryDataReady = generateTrees(formTreeCountry)
                parsed_json = json.loads(countryDataReady)


                print(parsed_json)
                #print(countryDataReady)

                #parsed_json[0]['selected'] = True
                #countryDataReady = json.dumps(parsed_json)


                #countryDataReady = (countryDataReady.replace("'", '"'))
                #call pieChart function
                pieData = pieChart(xdata,ydata, title , description)
             #updata dictionary for filter options: form skeletons
                pieData.update({'modeForm':modeFormSet})

                pieData.update({'yearsMode1':yearsSelect})
                pieData.update({'sourceData': generateTrees(formTree)})
                pieData.update({'countryDataReady': countryDataReady})
                pieData.update({'substanceDataReady': generateTrees(formTreeSubstance)})
                notification = '<div class="alert alert-warning"><strong><span class="glyphicon glyphicon-alert" aria-hidden="true"></span></strong> Only single selection is possible, because of selected mode.</div>'
                #create select modes for fancyTree : so single select or multiple

                pieData.update({'mode_tree4': 1, 'warning_8':notification})
                pieData.update({'mode_tree': 1, 'warning_6':notification})
                pieData.update({'mode_tree2': 1, 'warning_5':notification})
                pieData.update({'mode_tree3': 1, 'warning_7':notification})
                pieData.update({'mode_tree6': 1, 'warning_10':notification})
                #pieData.update({'warning': '<div class="alert alert-warning"><strong><span class="glyphicon glyphicon-alert" aria-hidden="true"></span></strong> Only single selection is possible, because of selected mode.</div>'})

                #send signal for popup
                popup = 1
                pieData.update({'popup': popup})
                pieData.update({'userSelectMode': "Absolute footprint of consumption split by year"})
                return render(request,"ExioVisuals/timeseries.html", pieData)
        #************START RETRIEVING USER SELECTIONS*******************
        envP = (request.POST.getlist('ft_4[]'))
        envPtitles = []
        for x in envP:
            print("Environmental Pressure:")
            print(Substance.objects.get(pk=x))
            print(Substance.objects.values_list('name', flat=True).get(pk=x))
            name = (Substance.objects.values_list('name', flat=True).get(pk=x))
            envPtitles.append(name)


        print(request.POST)
        year = (request.POST.get('Year'))
        print("Year selected:")
        print(year)
        regP = (request.POST.getlist('ft_2[]'))
        regPdata = []
        regPtitles = []
        for x in regP:
            print("Region of production:")
            print(Country.objects.get(pk=x))
            print(Country.objects.values_list('name', flat=True).get(pk=x))
            name = Country.objects.values_list('name', flat=True).get(pk=x)
            local = Country.objects.values_list('local', flat=True).get(pk=x)
            lwst_level = Country.objects.values_list('lwst_level', flat=True).get(pk=x)
            # if its the lowest level we use the local data
            if lwst_level == True:

                regPdata.append(local)
                regPtitles.append(name)



        secP = (request.POST.getlist('ft_5[]'))
        secPdata = []
        secPtitles = []
        for x in secP:
            print("Sector of production:")
            print(Product.objects.get(pk=x))
            print(Product.objects.values_list('name', flat=True).get(pk=x))
            local = Product.objects.values_list('local', flat=True).get(pk=x)
            name = Product.objects.values_list('name', flat=True).get(pk=x)
            lwst_level = Product.objects.values_list('lwst_level', flat=True).get(pk=x)
            # if its the lowest level we use the local data
            if lwst_level == True:
                secPtitles.append(name)
                secPdata.append(local)
        regRS = (request.POST.getlist('ft_6[]'))
        regRSdata = []
        regRStitles = []
        for x in regRS:
            print("Region selling:")
            print(Country.objects.get(pk=x))
            print(Country.objects.values_list('name', flat=True).get(pk=x))
            local = Country.objects.values_list('local', flat=True).get(pk=x)
            name = Country.objects.values_list('name', flat=True).get(pk=x)
            lwst_level = Country.objects.values_list('lwst_level', flat=True).get(pk=x)
            # if its the lowest level we use the local data
            if lwst_level == True:
                regRStitles.append(name)
                regRSdata.append(local)

        secC = (request.POST.getlist('ft_3[]'))
        secCdata = []
        secCtitles = []
        for x in  secC:
            print("Product purchased:")
            print(Product.objects.get(pk=x))
            print(Product.objects.values_list('name', flat=True).get(pk=x))
            local = Product.objects.values_list('local', flat=True).get(pk=x)
            name = Product.objects.values_list('name', flat=True).get(pk=x)
            lwst_level = Product.objects.values_list('lwst_level', flat=True).get(pk=x)
            # if its the lowest level we use the local data
            if lwst_level == True:

                secCdata.append(local)
                secCtitles.append(name)

        regC = (request.POST.getlist('ft_1[]'))
        regCdata = []
        regCtitles = []
        for x in regC:
            print("Region of consumption:")
            print(Country.objects.get(pk=x))
            print(Country.objects.values_list('lvl', flat=True).get(pk=x))
            lvl = Country.objects.values_list('lvl', flat=True).get(pk=x)
            name = (Country.objects.values_list('name', flat=True).get(pk=x))
            print(Country.objects.values_list('local', flat=True).get(pk=x))
            local = Country.objects.values_list('local', flat=True).get(pk=x)

            lwst_level = Country.objects.values_list('lwst_level', flat=True).get(pk=x)
            # if its the lowest level we use the local data
            if lwst_level == True:
                regCtitles.append(name)
                regCdata.append(local)


        selectMode = (request.POST.get('selectMode'))
        print("Select mode is: ")
        print(selectMode)



        #START MAKING PLOT DATA
        if selectMode == "Absolute footprint of consumption split by country where impact occurs":
            plotType = "PieChart"
            #QUERY THE DATABASE
            plotData,regPtitles = queryhdf5(plotType,selectMode, envP, year, regPdata, secPdata,regRSdata, regCdata,secCdata, regPtitles)

            table = generateDesc(selectMode,envPtitles,year,regPtitles, secPtitles, regRStitles, regCtitles, secCtitles)

            pieData = pieChart(regPtitles,plotData,selectMode, table)
            modeFormSet = modes(initial={'selection': 'selectA'})
            pieData.update({'modeForm':modeFormSet})
        if selectMode == "Absolute footprint of consumption split by sector where impact occurs":
            plotType = "PieChart"
            #QUERY THE DATABASE
            plotData,secPtitles = queryhdf5(plotType,selectMode, envP, year, regPdata, secPdata,regRSdata, regCdata,secCdata, secPtitles)

            table = generateDesc(selectMode,envPtitles,year,regPtitles, secPtitles, regRStitles, regCtitles, secCtitles)

            pieData = pieChart(secPtitles,plotData,selectMode, table)
            modeFormSet = modes(initial={'selection': 'selectA'})
            pieData.update({'modeForm':modeFormSet})
        if selectMode == "Absolute footprint of consumption split by consumed product category":
            plotType = "PieChart"
            #QUERY THE DATABASE
            plotData,secCtitles = queryhdf5(plotType,selectMode, envP, year, regPdata, secPdata,regRSdata, regCdata,secCdata, secCtitles)

            table = generateDesc(selectMode,envPtitles,year,regPtitles, secPtitles, regRStitles, regCtitles, secCtitles)

            pieData = pieChart(secCtitles,plotData,selectMode, table)
            modeFormSet = modes(initial={'selection': 'selectA'})
            pieData.update({'modeForm':modeFormSet})
        if selectMode == "Absolute footprint of consumption split by consuming region":
            plotType = "PieChart"

            print(regCdata)
            print(regCtitles)
            #QUERY THE DATABASE
            plotData,regCtitles = queryhdf5(plotType,selectMode, envP, year, regPdata, secPdata,regRSdata, regCdata,secCdata, regCtitles)

            table = generateDesc(selectMode,envPtitles,year,regPtitles, secPtitles, regRStitles, regCtitles, secCtitles)

            pieData = pieChart(regCtitles,plotData,selectMode, table)
            modeFormSet = modes(initial={'selection': 'selectA'})
            pieData.update({'modeForm':modeFormSet})
            #special case if years is selected
        if selectMode == "Absolute footprint of consumption split by year":
    #year is now A list!!!
            year = (request.POST.getlist('Year'))

            plotType = "TimeSeries"


            #QUERY THE DATABASE
            plotData,yearTitles = queryhdf5(plotType,selectMode, envP, year, regPdata, secPdata,regRSdata, regCdata,secCdata, year)
            print(plotData)
            print(yearTitles)

            table = generateDesc(selectMode,envPtitles,year,regPtitles, secPtitles, regRStitles, regCtitles, secCtitles)
            pieData = {'graph':timeSeries(yearTitles,plotData)}
            pieData.update({'title':selectMode})
            pieData.update({'description':table})
            '''
            pieData = pieChart(regCtitles,plotData,selectMode, table)
            '''
            modeFormSet = modes(initial={'selection': 'selectF'})

            pieData.update({'modeForm':modeFormSet})

            return render(request,"ExioVisuals/timeseries.html",pieData)

        #json_data = json.dumps(dataReady)

        #pieData = json_data
        #popup = 0
        #pieData.update({'popup': popup})
        #for key in request.POST.get('ft_01[]'):
         #   print(key)
          #  value = request.POST[key]
           # print(value)

        #POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        if request.is_ajax():
            #Always use get on request.POST. Correct way of querying a QueryDict.
            email = request.POST.get('email')
            password = request.POST.get('password')
            mode = request.POST.get('radio')
            print(request.POST)
            print(email)
            data = {"email":email , "password" : password, "sign": "Dsdfs"}


            #Returning same data back to browser.It is not possible with Normal submit
            return JsonResponse(data)
        #as I use formsets this is mandatory
        formset = MemberFormSet(request.POST)
        #make sure every form is validMemberFormSet = formset_factory(wraps(PostFormEFactor)(partial(PostFormEFactor)))

        if formTree.is_valid() and formset.is_valid():

            #start retrieving formset data, which is all filter data except FancyTree
            for f in formset:

                print("total form below:")

                cd = f.cleaned_data
                print(cd)
                print("name:")
                names = cd.get('name')
                print(names)
                print("like:")
                like = cd.get('like')
                print(like)


            #select = form.values_list['like']

            #Retrieve FancyTree data!
            subject = formTree.cleaned_data['products']
            print(subject)
            test = subject.values_list('url', flat=True)
            print("below fancyTree data:")
            print(test)

            #emissionSelection = (request.POST.getlist('emission'))
            #countrySelection = (request.POST.getlist('country'))
            #print(countrySelection)
            #print(emissionSelection)
            dict = ({"bla":test, "names":names, "like": like})

            return render(request,"ExioVisuals/DepecratedHome.html", dict)
        else:

            return render(request,"ExioVisuals/distribution.html", pieData)






        #invoke retrieve data function (should take more filtering values of course).
    xdata, ydata = retrieveData()

        #set title,description, size
    title = "Global CO2 emission distribution"
    description = "This chart shows the GHG emission distribution per country in the world. You can click on a country name to filter out the corresponding country from the piechart. Double click to select only one country."

        #call pieChart function
    pieData = pieChart(xdata,ydata, title , description)





    #pieData.update(bla)
     #updata dictionary for filter options : FancyTree
    pieData.update({'formTree2': formTree})


    #start getting some form skeletons now!
    ArticleFormSet = formset_factory(PostFormEFactor)
    formset = ArticleFormSet()
    formset = formset_factory(wraps(PostFormEFactor)(partial(PostFormEFactor)), extra=1)
     #updata dictionary for filter options: form skeletons
    pieData.update({'formset2':formset})
    selectionForm = formset_factory(wraps(reloadForm)(partial(reloadForm)), extra=1)
    pieData.update({'selectionForm': selectionForm})



    pieData.update({'sourceData': generateTrees(formTree)})
    pieData.update({'countryDataReady': generateTrees(formTreeCountry)})
    pieData.update({'substanceDataReady': generateTrees(formTreeSubstance)})
    modeFormSet = modes(initial={'selection': 'selectA'})
    pieData.update({'modeForm':modeFormSet})


    return render(request,"ExioVisuals/distribution.html", pieData)

#function that trims the old tree data from mySQL to only get the source data which is what is used for rendering
def generateTrees(treeData):
    tree = str(treeData)
    trimTree = (tree.partition('[{')[-1].rpartition('}]')[0])
    rebuildTree = "[{"+trimTree+"}]"
    return rebuildTree

def timeseries(request):
    """
    lineChart page
    """
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    nb_element = 150
    xdata = range(nb_element)
    xdata = list(map(lambda x: start_time + x * 1000000000, xdata))
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = list(map(lambda x: x * 2, ydata))

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie1 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
    }
    extra_serie2 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
    }
    chartdata = {'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie1, 'kwargs1': { 'color': '#778899' },
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie2, 'kwargs2': { 'color': '#b22121' },
    }

    charttype = "lineChart"
    chartcontainer = 'linechart_container'  # container name
    data = {
        'charttype2': charttype,
        'chartdata2': chartdata,
        'chartcontainer2': chartcontainer,
        'extra2': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y %H',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }}
    return render(request,"ExioVisuals/timeseries.html", data)



def geo(request):
    nodes = [
    {"id": "alpha123"},
    {"id": "beta"},
    {"id": "gamma"}
  ];
    edges = [
    {"strength": 2, "source": 0, "target": 2},
    {"strength": 1, "source": 1, "target": 2},
    {"strength": 1, "source": 2, "target": 0},
    {"strength": 6, "source": 2, "target": 1},
  ];

    return render(request,'ExioVisuals/geo.html', {"nodes": nodes, "edges": edges })

def supplychain(request):
    nodes = [
    {"id": "alpha123"},
    {"id": "beta"},
    {"id": "gamma"}
  ];
    edges = [
    {"strength": 2, "source": 0, "target": 2},
    {"strength": 1, "source": 1, "target": 2},
    {"strength": 1, "source": 2, "target": 0},
    {"strength": 6, "source": 2, "target": 1},
  ];

    return render(request,'ExioVisuals/supplychain.html', {"nodes": nodes, "edges": edges })

#-------------------------------------Retrieving data
def retrieveData():
    #below:get specific values (for filtering)
        #countryNames = GhgEmissions.objects.get(code='WM')
        #below: retrieve all absolute emissions
        absData = GhgEmissions.objects.all().values_list('absolute', flat=True)
        #below: retrieve all countrynames
        countryNames = GhgEmissions.objects.all().values_list('label', flat=True)

        #query all objects
        t = GhgEmissions.objects.all().values_list()
        #remove region data
        pre = list(t)
        #print(pre)
        #print("bla")
        pre.pop(-1)
        pre.pop(-1)
        pre.pop(-1)
        pre.pop(-1)
        pre.pop(-1)
        countryNames =[]
        absData = []
        for x in pre:
            countryNames.append(x[1])
            absData.append(x[3])


        #now map the data

        xdata = countryNames
        ydata = absData
        return xdata,ydata




#--------------------------------------Visual Analytics library
def pieChart(vLabel,vData, vTitle, vDescr):
    chartdata = {'x': vLabel, 'y': vData}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'
    pieData = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
            },
        'title' : vTitle,
        'description': vDescr,



    }
    return pieData

def timeSeries(vLabel,vData):
    print("is this working?")
    vData = [ int(x) for x in vData ]
    data = []

    for x, y in zip(vData, vLabel):
        data.append({"year": y, "name":"selected products and sectors", "value": x},)


    return data
    '''
     var sample_data = [
    {"year": 1991, "name":"alpha", "value": 17},
    {"year": 1992, "name":"alpha", "value": 20},
    {"year": 1993, "name":"alpha", "value": 25},
    {"year": 1994, "name":"alpha", "value": 33},
    {"year": 1995, "name":"alpha", "value": 52},
    {"year": 1991, "name":"beta", "value": 36},
    {"year": 1992, "name":"beta", "value": 32},
    {"year": 1993, "name":"beta", "value": 40},
    {"year": 1994, "name":"beta", "value": 58},
    {"year": 1995, "name":"beta", "value": 13},
    {"year": 1991, "name":"gamma", "value": 24},
    {"year": 1992, "name":"gamma", "value": 27},
    {"year": 1994, "name":"gamma", "value": 35},
    {"year": 1995, "name":"gamma", "value": 40}
  ]
    return data
    '''



def test(request):
	form = ProductSelectionForm(request.POST or None)
	print("you are here ")
	if request.method == "POST":
		if form.is_valid():
			print("you are here 3")

			subject = form.cleaned_data['categories']
			test = subject.values_list('url', flat=True)
			print(test)



	return render(request, "ExioVisuals/test.html", {'form': form})

def redirectView(request):
    MemberFormSet = formset_factory(wraps(reloadForm)(partial(reloadForm)))
    formTree = ProductSelectionForm(request.POST or None)
    if request.method == 'POST':
         #as I use formsets this is mandatory
        formset = MemberFormSet(request.POST)
        #make sure every form is validMemberFormSet = formset_factory(wraps(PostFormEFactor)(partial(PostFormEFactor)))
        if formset.is_valid():
            #start retrieving formset data, which is all filter data except FancyTree
            for f in formset:
                cd = f.cleaned_data

                print("selection:")
                selection = cd.get('selection')
                print(selection)
                #

                #start getting some form skeletons now!
                ArticleFormSet = formset_factory(PostFormEFactor)
                formset = ArticleFormSet()
                formset = formset_factory(wraps(PostFormEFactor)(partial(PostFormEFactor)), extra=1)
                #updata dictionary for filter options: form skeletons

                selectionForm = formset_factory(wraps(reloadForm)(partial(reloadForm)), extra=1)
                dict = ({'selectionForm': selectionForm})
                #now send some other forms to the filter interface
                dict.update({'formset':formset})
                dict.update({'formTree': formTree})
                #send signal for popup
                popup = 1
                dict.update({'popup': popup})
                return render(request,"ExioVisuals/distribution.html", dict)


def ajax(request):
    if request.method == 'POST':
        #POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        if request.is_ajax():
            #Always use get on request.POST. Correct way of querying a QueryDict.
            email = request.POST.get('email')
            password = request.POST.get('password')
            data = {"email":email , "password" : password}
            #Returning same data back to browser.It is not possible with Normal submit
            return JsonResponse(data)
    return render(request, "ExioVisuals/ajax.html")


def queryhdf5(plotType,selectMode, envP, year, regP, secP,regRS, regC,secC, plotDatatitles):
    #determine plottype as it affects the query and determine the mode that we are in
    if plotType == "PieChart" and selectMode == "Absolute footprint of consumption split by country where impact occurs":
        #as it is piechart we only select one year
        print("Query is: ")
        #print("regP"+str(regP[0])+"secP"+str(secP[0])+"regRS"+str(regRS[0])+"regC"+str(regC[0])+"secC"+str(secC[0]))
        #we have the title list and the actual data points , both needs to be sorted for the query to hdf5 according to the data points
        regPadjusted = [ int(x) for x in regP ]
        points = zip(regPadjusted,plotDatatitles)
        pack = (sorted(points))
        regPadjusted = [point[0] for point in pack]
        plotDatatitles = [point[1] for point in pack]

        #regPadjusted = sorted(regPadjusted, key=int)
        print(regPadjusted)
        #regParray = np.array( regPadjusted )
        #print(regPadjusted)
        #with h5py.File('/home/sidney/datahdf5/experiments/{0}_combined.hdf5'.format(year) ,'r')as hf:

        with h5py.File('/home/chai/data/experiments/{0}_combined.hdf5'.format(year) ,'r')as hf:
            #importing region is region of consumption so we pass that in to retrieve that data
            test = (hf.get('region{0}'.format(int(regC[0]))))
            tmp = test[regPadjusted,int(secP[0]),int(regRS[0]),int(secC[0])]
            #tmp = np.around(tmp, decimals=0)
            #tmp = test[0:49,43,44,2]
            tmp = tmp.tolist()
            return tmp, plotDatatitles
    #determine plottype as it affects the query and determine the mode that we are in
    if plotType == "PieChart" and selectMode == "Absolute footprint of consumption split by sector where impact occurs":
        #as it is piechart we only select one year
        print("Query is: ")
        #print("regP"+str(regP[0])+"secP"+str(secP[0])+"regRS"+str(regRS[0])+"regC"+str(regC[0])+"secC"+str(secC[0]))
        #we have the title list and the actual data points , both needs to be sorted for the query to hdf5 according to the data points
        secPadjusted = [ int(x) for x in secP ]
        points = zip(secPadjusted,plotDatatitles)
        pack = (sorted(points))
        secPadjusted = [point[0] for point in pack]
        plotDatatitles = [point[1] for point in pack]

        #regPadjusted = sorted(regPadjusted, key=int)
        print(secPadjusted)
        #regParray = np.array( regPadjusted )
        #print(regPadjusted)
        #with h5py.File('/home/sidney/datahdf5/experiments/{0}_combined.hdf5'.format(year) ,'r')as hf:

        with h5py.File('/home/chai/data/experiments/{0}_combined.hdf5'.format(year) ,'r')as hf:
            #importing region is region of consumption so we pass that in to retrieve that data
            test = (hf.get('region{0}'.format(int(regC[0]))))
            tmp = test[int(regP[0]),secPadjusted,int(regRS[0]),int(secC[0])]
            #tmp = np.around(tmp, decimals=0)
            #tmp = test[0:49,43,44,2]
            tmp = tmp.tolist()
            return tmp, plotDatatitles
    #determine plottype as it affects the query and determine the mode that we are in
    if plotType == "PieChart" and selectMode == "Absolute footprint of consumption split by consumed product category":
        #as it is piechart we only select one year
        print("Query is: ")
        #print("regP"+str(regP[0])+"secP"+str(secP[0])+"regRS"+str(regRS[0])+"regC"+str(regC[0])+"secC"+str(secC[0]))
        #we have the title list and the actual data points , both needs to be sorted for the query to hdf5 according to the data points
        secCadjusted = [ int(x) for x in secC ]
        points = zip(secCadjusted,plotDatatitles)
        pack = (sorted(points))
        secCadjusted = [point[0] for point in pack]
        plotDatatitles = [point[1] for point in pack]

        #regPadjusted = sorted(regPadjusted, key=int)
        print(secCadjusted)
        #regParray = np.array( regPadjusted )
        #print(regPadjusted)
        #with h5py.File('/home/sidney/datahdf5/experiments/{0}_combined.hdf5'.format(year) ,'r')as hf:

        with h5py.File('/home/chai/data/experiments/{0}_combined.hdf5'.format(year) ,'r')as hf:
            #importing region is region of consumption so we pass that in to retrieve that data
            test = (hf.get('region{0}'.format(int(regC[0]))))
            tmp = test[int(regP[0]),int(secP[0]),int(regRS[0]),secCadjusted]
            #tmp = np.around(tmp, decimals=0)
            #tmp = test[0:49,43,44,2]
            tmp = tmp.tolist()
            return tmp, plotDatatitles
    #determine plottype as it affects the query and determine the mode that we are in
    if plotType == "PieChart" and selectMode == "Absolute footprint of consumption split by consuming region":
        with h5py.File('/home/chai/data/experiments/{0}_combined.hdf5'.format(year) ,'r')as hf:
            data = []
            #retrieve the data for each region of consumption and append to data variable
            for x in regC:
                print(x)
                test = (hf.get('region{0}'.format(int(x))))
                tmp = test[int(regP[0]),int(secP[0]),int(regRS[0]),int(secC[0])]
                tmp = tmp.tolist()
                data.append(tmp)

            return data, plotDatatitles
    #determine plottype as it affects the query and determine the mode that we are in
    if plotType == "TimeSeries" and selectMode == "Absolute footprint of consumption split by year":
        print("we arrived!")
        data = []
        for x in year:


            with h5py.File('/home/chai/data/experiments/{0}_combined.hdf5'.format(x) ,'r')as hf:

            #retrieve the data for each yearon and append to data variable

                test = (hf.get('region{0}'.format(int(regC[0]))))
                tmp = test[int(regP[0]),int(secP[0]),int(regRS[0]),int(secC[0])]
                tmp = tmp.tolist()
                data.append(tmp)


        return data, plotDatatitles
        #with h5py.File('/home/chai/data/experiments/{0}_combined.hdf5'.format(year) ,'r')as hf:

'''
                # **regC** = region(s) that imports > region(s) of interest that has indirect emissions
                # lets assume it is Netherlands and Belgium
                # **secC** = product(s) that is imported > product(s) of interest that has indirect emissions
                #lets assume it is Aluminium and Alumnium products
                # **secP** = sector(s) of emission  > sector of consumption
                #lets assume it is electricity by coal
                plotData = []
                #print("region of emission/exporting country/secP")
                #print(regP)
                # for all those importing regions we want to get data according to query
                #for x in impRegions:
                #get the respective importing region at a given time in the for loop
                    #test = (hf.get('region{0}'.format(x)))
                    #for each importing region we want to use the query given by user >
                    # THE ONLY PART THAT IS non SELECTABLE IS THE EXPORTING COUNTRY > secP
                    # **each query follows the structure of 1 region of emissions (regP NOT SELECTABLE), 2 sector of emission (secP),3 region selling (regRS), 4 product of sale (secC)
                    #tmp = test[0:nr,0:ns,0:nr,0:ns]
                    #regionOfEmission =
                #print(data)
            #print(data.shape)
            #print(data)
    #open the HDF5 datasets according to query
'''

def generateDesc(selectMode,envPtitles,year,plotDataTitles, secPtitles, regRStitles, regCtitles, secCtitles):
    head = '<div class="container" ><table class="table table-hover" ><thead><tr><th class="col-sm-0.5">Type </th><th class="col-sm-0.5">Query</th></tr></thead>'
    body = '<tbody><tr><td>Select mode</td><td>{0}</td></tr><tr><td>Environmental pressure</td><td> {1}</td> </tr><tr><td>Year</td><td>{2} </td> </tr><tr><td>Region of production </td><td>{3} </td> </tr><tr><td> Sector of production</td><td>{4} </td> </tr><tr><td>Region selling</td><td>{5} </td> </tr><tr><td>Region of consumption </td><td>{6} </td> </tr><tr><td>Sector of consumption </td><td>{7} </td> </tr></tbody></table></div>'.format(selectMode,envPtitles,year,plotDataTitles, secPtitles, regRStitles, regCtitles, secCtitles)
    table = head + body
    return table