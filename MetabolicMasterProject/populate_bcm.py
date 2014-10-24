import os

def populate():
    urine_cat = add_waste('Pure Urine', 'Fertilizers are mostly based on phosphorus (P) and ammonia (NH3) compounds. Phosphorus and ammonia in general are essential nutrients for plants and animals. Fertilizers are used to support plant growth efficiently and in the end ensure sufficient food production. However the production of ammonia is very energy intensive. The current production phases in order to make fertilizers are based on phosphorus import and ammonia production through energy intensive methods. Even though urine for instance contains a lot of nitrogen (which can be converted to ammonia) and phosphorus. This makes urine a possible source of nutrient extraction. To be precise struvite can be recovered from urine. The mineral struvite is a combination of molecules magnesium, phosphate and ammonia.  This will mean that in the ideal situation phosphorus does not need to be imported anymore. But also recovering ammonia will lead to less energy demanding procedures needed to produce ammonia. This technology can reduce the need of fossil fuel for waste water treatment systems and can lead to production of sustainable fertilizers with the use of urine. ')

    gw_cat = add_waste('Grey Water', 'Grey Water is water coming from cleansing operations: showering, bathing, sink drains, washing machines, and dishwashers')


    # Print out what we have added to the user.
    for c in Waste.objects.all():
            print('Done!')



def add_waste(name, desc):
    c = Waste.objects.get_or_create(name=name, desc=desc)[0]

    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting MetabolicMasterProject population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MetabolicMasterProject.settings')
    from BioCascadeModeller.models import Waste
    populate()