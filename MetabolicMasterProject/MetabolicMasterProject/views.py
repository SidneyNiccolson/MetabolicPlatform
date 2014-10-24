from django.template import RequestContext
from django.shortcuts import render_to_response

#this is the first page of the Metabolic Web-app
def homePage(request):

    #call the HomePage HTML
    context = RequestContext(request)

    #nothing to pass to the template
    context_dict = {}

    #return render_to_response('/MetabolicMasterProject/HomePage.html', context_dict, context)
    return render_to_response('MetabolicMasterProject/HomePage.html', context_dict, context)