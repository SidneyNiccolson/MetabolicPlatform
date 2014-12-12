from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, render
from django.template import RequestContext
from django.http import HttpResponseForbidden
from models import Waste, TreatmentTech, Parameters, WasteParameters
from django.shortcuts import get_object_or_404
from forms import PostFormTreatmentTech


def test2(request):
    return render_to_response('BioCascadeModeller/effluentmockup.html')

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

    #replace every technologies spaces with underscores for creating functional links
    for treat in treatment_list:
        treat.url = decode(treat.name)



    #send it off
    context_dict = {'treatments': treatment_list}

      #retrieve all waste information by ID
    waste_specific_list = Waste.objects.get(id=waste_id)
    context_dict['wastes'] = waste_specific_list


    return render_to_response('BioCascadeModeller/BCMtech.html', context_dict, context)

#this function is for specific detail show on each treatment technology and will have a button to go to modelling
def treatmentTech2(request, waste_id, treat_id):
    #retrieve mandatory context
    context = RequestContext(request)
    #retrieve only the instance of treatmenttech by treat_id
    treatment = TreatmentTech.objects.get(id=treat_id)

    context_dict = {'treatment': treatment}

    waste_specific_list = Waste.objects.get(id=waste_id)
    context_dict['wastes'] = waste_specific_list

    return render_to_response('BioCascadeModeller/BCMtech2.html', context_dict, context)
#modelling part
def test(request,treatment_id, waste_id):
    #retrieve mandatory context
    context = RequestContext(request)
    context_dict = {}
    #if treatment_id equals 1 show the post of PostFormTreatmentTech and get the data (this is the struvite reactor stuff that is connected to urine)
    #treatment is struvite and waste is urine
    if treatment_id == "1" and waste_id == "2":
         # if this is a POST request we need to process the form data
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
            form = PostFormTreatmentTech(request.POST)
        # check whether it's valid:
            if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
                persons = (form.cleaned_data['persons'])
                print(persons)
                #retrieve all valuable data
               #retrieve all waste information by ID
                waste_specific_list = Waste.objects.get(id=waste_id)





                #get all the parameters
                param = Parameters.objects.all()




                    #get all the quantities per waste_id
                waste = get_object_or_404(Waste, pk=waste_id)

                values = []
            #do some calculations
                for wasteparameters in waste.wasteparameters_set.all():
                    value= wasteparameters.quantity * persons
                    values.append(value)

                #put the waste specific info in the context_dict and send it off to the HTML
                context_dict = {'wastes': waste_specific_list}
                context_dict['parameters'] = param
                context_dict['treatment_id'] = treatment_id
                context_dict['waste'] = waste
                context_dict['persons'] = persons

                context_dict['values'] = values
                #stuff in request dictionary will pass the variable per user
                request.session['persons'] = persons
                request.session['nutrient_loss'] = values
            #print(waste_specific_list)
            # redirect to a new URL:
                return render_to_response('BioCascadeModeller/BCMResult.html', context_dict, context)
            else:
        #errors about the supplied form
                print form.errors
                form = PostFormTreatmentTech()

        #the form itself and all other data to send
                context_dict = {'form': form}

        #context_dict['wastes'] = waste_specific_list
        #context_dict['treatments'] = treatment_list
        #treat = encode(treat_url)
        #context_dict['names'] = treat

                return render(request, 'BioCascadeModeller/BCMmodel.html', context_dict)


    # if a GET (or any other method) we'll create a blank form
        else:
            form = PostFormTreatmentTech()

        #the form itself and all other data to send
            context_dict = {'form': form}
        #context_dict['wastes'] = waste_specific_list
        #context_dict['treatments'] = treatment_list
        #treat = encode(treat_url)
        #context_dict['names'] = treat

        return render(request, 'BioCascadeModeller/BCMmodel.html', context_dict)
    else:
        return HttpResponse("This function is not yet implemented for this technology.")

def decode(categoryParam):
        return categoryParam.replace(' ', '_')
def encode(categoryParam):
        return categoryParam.replace('_', ' ')

def about2(request):
    context = RequestContext(request)

    #nothing to pass to the template
    context_dict = {}
    return render_to_response('BioCascadeModeller/BCMabout.html', context_dict, context)

#!!! THIS FUNCTION IS COMPLETELY DEPENDEND ON WASTE ID(URINE) AND TREATMENT ID (STRUVITE REACTOR)
def calc_results_Struvite(request, waste_id, treatment_id):
    #retrieve mandatory context
    context = RequestContext(request)


    #request some data from the request (per-user) dictionary
    persons = request.session.get('persons')
    nutrient_loss = request.session.get('nutrient_loss')

    #assumptions
    #1: one person will produce 1.4 Liter of urine a day
    #2: 0.8 grams of magnesium per liter of urine is needed for the struvite reactor
    #3: 90% of Phosphorus can be recovered with the struvite reactor
    average_urine_prod = persons*1.4
    needed_magnesium = average_urine_prod * 0.8
    phosphorus_loss = nutrient_loss[1]
    phosphorus_recovery = phosphorus_loss*0.9


    #annual recovery and magnesium needed
    annual_needed_magnesium = needed_magnesium*365
    annual_phosphorus_recovery = phosphorus_recovery * 365

    #put all data in dictionary to be send to the html template
    context_dict = {'persons': persons}
    context_dict['average_urine_prod'] = average_urine_prod
    context_dict['needed_magnesium'] = needed_magnesium
    context_dict['phosphorus_recovery'] = phosphorus_recovery
    context_dict['annual_needed_magnesium'] = annual_needed_magnesium
    context_dict['annual_phosphorus_recovery'] = annual_phosphorus_recovery

    #this HTML is strictly dependend on Struvite with Yellow Water!!
    return render_to_response('BioCascadeModeller/CalcResults/StruviteResults.html', context_dict, context)



'''
#treatment specific page
def treatSpecific(request, waste_id, treat_url):
     #retrieve mandatory context
    context = RequestContext(request)

    treat = encode(treat_url)

    #retrieve all treatment technologies by waste_id
    treatment_list = TreatmentTech.objects.filter(waste=waste_id)

    #replace every technologies spaces with underscores for creating functional links
    for treat in treatment_list:
        treat.url = decode(treat.name)



    #send it off
    context_dict = {'treatments': treatment_list}

      #retrieve all waste information by ID
    waste_specific_list = Waste.objects.get(id=waste_id)
    context_dict['wastes'] = waste_specific_list
    context_dict['names'] = treat

    return render_to_response('BioCascadeModeller/BCMtechspecific.html', context_dict, context)
'''