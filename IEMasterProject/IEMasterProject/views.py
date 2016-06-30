from django.template import RequestContext
from django.shortcuts import render_to_response


#this is the first page of the Web-app
def homePage(request):

    #call the HomePage HTML
    context = RequestContext(request)

    #nothing to pass to the template
    context_dict = {}

    #return render_to_response('/IEMasterProject/HomePage.html', context_dict, context)
    return render_to_response('IEMasterProject/HomePage.html', context_dict, context)

#about for the online platform
def about(request):
    #call the about HTML
    context = RequestContext(request)

    #nothing to pass to the template
    context_dict = {}
    return render_to_response('IEMasterProject/about.html', context_dict, context)

