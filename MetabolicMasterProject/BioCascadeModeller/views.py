from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from models import Waste, TreatmentTech, Parameters, WasteParameters
from django.shortcuts import get_object_or_404

#this is the first page of the BCM app
def bcmHome(request):
   #retrieve mandatory context
    context = RequestContext(request)

   #retrieve all wastes
    waste_list = Waste.objects.all()

    # for every waste: decode (note: this is also sent to the HTML through the variable <waste>)
    for waste in waste_list:
        waste.url = waste.name.replace(' ', '_')

    #put it in context_dict and send it off to the HTML
    context_dict = {'wastes': waste_list}


    return render_to_response('BioCascadeModeller/BCMHome.html', context_dict, context)

#page to show for every db entry there properties like nutrients amount etc
#use waste_id as parameter which is tied to waste.id from the BCMHome.html and from waste_list
def details(request, waste_id):
    #retrieve mandatory context
    context = RequestContext(request)

      #retrieve all waste information by ID
    waste_specific_list = Waste.objects.get(id=waste_id)

    #put the waste specific info in the context_dict and send it off to the HTML
    context_dict = {'wastes': waste_specific_list}
    #get all the parameters
    param = Parameters.objects.all()
    context_dict['parameters'] = param

    #get all the quantities per waste_id
    waste = get_object_or_404(Waste, pk=waste_id)

    context_dict['waste'] = waste

    return render_to_response('BioCascadeModeller/BCMspec.html', context_dict, context)

#Page to show for every db entry there corresponding treatment technologies
def treatmentTech(request, waste_id):
    #retrieve mandatory context
    context = RequestContext(request)


    #retrieve all treatment technologies by waste_id
    treatment_list = TreatmentTech.objects.filter(waste=waste_id)
    print(treatment_list)
    #send it off
    context_dict = {'treatments': treatment_list}

      #retrieve all waste information by ID
    waste_specific_list = Waste.objects.get(id=waste_id)
    context_dict['wastes'] = waste_specific_list


    return render_to_response('BioCascadeModeller/BCMtech.html', context_dict, context)