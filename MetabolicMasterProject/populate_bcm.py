import os

def populate():

    kw_cat = add_waste('Kitchen Waste','Food waste from cooking passed through a grinder in the kitchen.', '')

    urine_cat = add_waste('Yellow Water', 'Fertilizers are mostly based on phosphorus (P) and ammonia (NH3) compounds. Phosphorus and ammonia in general are essential nutrients for plants and animals. Fertilizers are used to support plant growth efficiently and in the end ensure sufficient food production. However the production of ammonia is very energy intensive. The current production phases in order to make fertilizers are based on phosphorus import and ammonia production through energy intensive methods. Urine contains a lot of nitrogen (which can be converted to ammonia) and phosphorus. This makes urine a possible source for nutrient extraction. By extracting valuable nutrients from urine, energy and fossil fuels needs can be reduced. This can even lead to production of sustainable fertilizers. ', '/static/Urine.png')

    bw_cat = add_waste('Brown Water','Water mixed with feces (and urine) from toilets.', '')


    gw_cat = add_waste('Grey Water', 'Grey Water is water coming from cleansing operations: showering, bathing, sink drains, washing machines, and dishwashers.', '')





    sw_cat = add_waste('Storm Water','Rainwater entering a sewer.', '')

    #add the struvite reactor to the treattech and add the urine object to the struvite reactor
    struvite_reactor = add_treatTech('Struvite Reactor', 'The main minerals required by plants are phosphorus, nitrogen and potassium. Humans excrete about 80% of nitrogen, 60% of phosphorus and 55% of potassium in urine. Even though nitrogen is not a generally scarce nutrient, phosphorus and potassium are less readily available. When urine is stored  precipitate is formed through a spontaneous reaction. This precipitate is called magnesium ammonium phosphate also known as struvite. About 30% to 50% of phosphate precipitates naturally however when adding magnesium to the reaction 90% of the phosphorus can be recovered. This struvite can be filtered out and dried to produce fertilizer. The remaining effluent contains nitrogen and potassium which can also be applied to plants by irrigation systems. By developing and implementing a struvite reactor valuable nutrients can be recovered. A struvite reactor can be produced locally and with low costs, however this technology is still very much in development and new designs can lead to more efficient nutrient recovery. ',
                                     'Uses chemical reactions (precipitation) in order to separate nutrients from other molecules.',
                                     'Logically urine is needed. Urine can be collected from any place like households, markets and offices. The only disadvantage is that there is need for urine separation from feces and other sanitation products. By using source separation toilets this can be achieved. Also a local magnesium source is required and this can come from local salt production facilities. First the reactor is filled with urine and then magnesium is added. The magnesium amount is depended on the phosphorus amount in the urine. The amount of phosphorus can be determined through measuring tools, however these tools can  be expensive. For a low costs struvite reactor the phosphorus amount is assumed based on averages in urine. The molar ratio varies between 1:1 to 1:1.5. Then the mixture is stirred either manually or by a stirring mechanism. This stirring is done in a small amount of time (10 minutes) as the struvite precipitates. After the struvite is has settled, a valve is opened in order to filter out the struvite. This struvite can then be sundried to form struvite powder. As explained earlier the effluent can be used in irrigation systems. Treatment capacities can vary from 10L to 5000L of urine per day. Materials used in order to build a struvite reactor can vary depending on size, scale, funds. For example a struvite reactor can consist of a stainless steel tank, a stirring mechanism, a reactor outlet and filter module. '
                                     ,'Struvite (magnesium ammonium phosphate). When dried it is a fertilizer powder. Pilot studies were conducted by Eawag and UN-Habitat and showed that 400L of urine daily added to a STUN struvite reactor can lead to 170kg struvite per year.',
                                     'Effluent (urine with potassium). Can be added to irrigation systems for plant uptake. ','/static/StruviteBig.png','/static/StruviteSmall.png',waste_kind=[urine_cat])

    #add the struvite reactor to the treattech and add the urine object to the struvite reactor
    test_reactor = add_treatTech('Test Reactor for urine', 'descriptionsss', 'summary',
                                     'tech_spec'
                                     ,'product',
                                     'byproduct','','',waste_kind=[urine_cat])
    test_reactor = add_treatTech('Test Reactor for grey water', 'descriptionsss','summary',
                                     'tech_spec'
                                     ,'product',
                                     'byproduct','','',waste_kind=[gw_cat])

 #add the struvite reactor to the treattech and add the urine object to the struvite reactor

    #add 5 parameters
    nitrogen = add_parameters('Nitrogen', 'grams', 'Nutrient', 'Nitrogen plays a key role in chlorophyll production and protein synthesis. Chlorophyll is the green plant pigment responsible for photosynthesis. When nitrogen is deficient, plants develop yellow or pale leaves and their growth is stunted.')
    phosphorus = add_parameters('Phosphorus', 'grams', 'Nutrient', 'Phosphorus is a vital component of adenosine triphosphate (ATP) which supplies the energy for many processes in the plant. Phosphorus rarely produces spectacular growth responses, but is fundamental to the successful development of all crops.')
    potassium = add_parameters('Potassium', 'grams', 'Nutrient', 'Potassium is needed by virtually all crops and often in higher rates than nitrogen. Potassium regulates the plants water content and expansion. It is key to achieving good yield and quality in cotton and critical for increasing the size, juice content and sweetness of fruit.')
    calcium = add_parameters('Calcium', 'grams', 'Nutrient', 'Calcium is perhaps the most important. Calcium strengthens cell walls, helping to reduce bruising and disease in fruit, salad and vegetable crops. This means that a good supply of calcium produces food crops that are less prone to damage and have a longer shelf life. Crops short in calcium will have growth disorders such as corky skin. Fruit and vegetables containing higher levels of calcium also have a higher nutritional value for example, vitamin C and antioxidants in tomatoes. This means that eating fresh fruit with strong skins and a great, crisp bite will help provide us with the calcium we need for strong bones.')
    magnesium = add_parameters('Magnesium', 'grams', 'Nutrient', 'Magnesium is also important for crop quality, but is also a key component of leaf chlorophyll and the enzymes that support plant growth. Low magnesium leads to reduced photosynthesis, which severely limits crop yields. Grain fill in rice and dry matter content of potatoes can be significantly reduced if magnesium is undersupplied.')

    #add for the five parameters there quantities
    nitrogen_quantity = add_waste_parameters(9, nitrogen, urine_cat)
    phophorus_quantity = add_waste_parameters(0.8, phosphorus, urine_cat)
    potassium_quantity = add_waste_parameters(2.75, potassium, urine_cat)
    calcium_quantity = add_waste_parameters(0.2, calcium, urine_cat)
    magnesium_quantity = add_waste_parameters(0.2, magnesium, urine_cat)

    # Print out what we have added to the user.
    #for c in Waste.objects.all():
    print('Done!')



#add wastes
def add_waste(name, desc, imageWaste):
    c, created = Waste.objects.get_or_create(name=name, desc=desc, imageWaste=imageWaste)

    return c
#add treatment technologies
def add_treatTech(name, desc, summary, tech_spec, products, byproducts, image,image2,waste_kind):
    d, created = TreatmentTech.objects.get_or_create(name=name, desc=desc, summary=summary, tech_spec=tech_spec, products=products, byproducts=byproducts, image=image, image2=image2)
    #create a relationship between treatment technologies and waste
    d.waste.add(*Waste.objects.filter(name__in=waste_kind))


    return d
#add parameters
def add_parameters(name, unit, type, desc):
    e, created = Parameters.objects.get_or_create(name=name, unit=unit, type=type, desc=desc)

    return e

#add waste parameters
def add_waste_parameters(quantity, parameters, waste):
    f, created = WasteParameters.objects.get_or_create(quantity=quantity, parameters=parameters, waste=waste)

    return f


# Start execution here!
if __name__ == '__main__':
    print "Starting MetabolicMasterProject population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MetabolicMasterProject.settings')
    from BioCascadeModeller.models import Waste, TreatmentTech, Parameters, WasteParameters
    populate()