import os

def populate():
    urine_cat = add_waste('Urine', 'Fertilizers are mostly based on phosphorus (P) and ammonia (NH3) compounds. Phosphorus and ammonia in general are essential nutrients for plants and animals. Fertilizers are used to support plant growth efficiently and in the end ensure sufficient food production. However the production of ammonia is very energy intensive. The current production phases in order to make fertilizers are based on phosphorus import and ammonia production through energy intensive methods. Even though urine for instance contains a lot of nitrogen (which can be converted to ammonia) and phosphorus. This makes urine a possible source of nutrient extraction. To be precise struvite can be recovered from urine. The mineral struvite is a combination of molecules magnesium, phosphate and ammonia.  This will mean that in the ideal situation phosphorus does not need to be imported anymore. But also recovering ammonia will lead to less energy demanding procedures needed to produce ammonia. This technology can reduce the need of fossil fuel for waste water treatment systems and can lead to production of sustainable fertilizers with the use of urine. ')

    gw_cat = add_waste('Grey Water', 'Grey Water is water coming from cleansing operations: showering, bathing, sink drains, washing machines, and dishwashers.')

    bw_cat = add_waste('Black Water','Water mixed with feces (and urine) from toilets.')

    kw_cat = add_waste('Kitchen Waste','Food waste from cooking passed through a grinder in the kitchen.')

    sw_cat = add_waste('Storm Water','Rainwater entering a sewer.')

    #add the struvite reactor to the treattech and add the urine object to the struvite reactor
    struvite_reactor = add_treatTech('Struvite Reactor', 'A struvite reactor is a ....', waste_kind=[urine_cat])

    #add 5 parameters
    nitrogen = add_parameters('Nitrogen', 'grams/per person/per day', 'Nutrient', 'Nitrogen plays a key role in chlorophyll production and protein synthesis. Chlorophyll is the green plant pigment responsible for photosynthesis. When nitrogen is deficient, plants develop yellow or pale leaves and their growth is stunted.')
    phosphorus = add_parameters('Phosphorus', 'grams/per person/per day', 'Nutrient', 'Phosphorus is a vital component of adenosine triphosphate (ATP) which supplies the energy for many processes in the plant. Phosphorus rarely produces spectacular growth responses, but is fundamental to the successful development of all crops.')
    potassium = add_parameters('Potassium', 'grams/per person/per day', 'Nutrient', 'Potassium is needed by virtually all crops and often in higher rates than nitrogen. Potassium regulates the plants water content and expansion. It is key to achieving good yield and quality in cotton and critical for increasing the size, juice content and sweetness of fruit.')
    calcium = add_parameters('Calcium', 'grams/per person/per day', 'Nutrient', 'Calcium is perhaps the most important. Calcium strengthens cell walls, helping to reduce bruising and disease in fruit, salad and vegetable crops. This means that a good supply of calcium produces food crops that are less prone to damage and have a longer shelf life. Crops short in calcium will have growth disorders such as corky skin. Fruit and vegetables containing higher levels of calcium also have a higher nutritional value for example, vitamin C and antioxidants in tomatoes. This means that eating fresh fruit with strong skins and a great, crisp bite will help provide us with the calcium we need for strong bones.')
    magnesium = add_parameters('Magnesium', 'grams/per person/per day', 'Nutrient', 'Magnesium is also important for crop quality, but is also a key component of leaf chlorophyll and the enzymes that support plant growth. Low magnesium leads to reduced photosynthesis, which severely limits crop yields. Grain fill in rice and dry matter content of potatoes can be significantly reduced if magnesium is undersupplied.')

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
def add_waste(name, desc):
    c, created = Waste.objects.get_or_create(name=name, desc=desc)

    return c
#add treatment technologies
def add_treatTech(name, desc, waste_kind):
    d, created = TreatmentTech.objects.get_or_create(name=name, desc=desc)
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