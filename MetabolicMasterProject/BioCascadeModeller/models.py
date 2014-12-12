from django.db import models

#Parameters model containing nutrients and other molecules from Wastes
class Parameters(models.Model):
    #has a name
    name = models.CharField(max_length=128, unique=True)
    #has a unit
    unit = models.CharField(max_length=128)
    #has a type
    type = models.CharField(max_length=128)

    #has a description
    desc = models.TextField(default='test')

    #mandatory
    def __unicode__(self):
        return self.name

#waste model
class Waste(models.Model):
    #has a name
    name = models.CharField(max_length=128, unique=True)
    #has a description
    desc = models.TextField(default='test')
    #has a picture
    imageWaste = models.ImageField(upload_to="static")
    #many to many relationship with Waste
    parametersList = models.ManyToManyField(Parameters, through='WasteParameters')

    #mandatory
    def __unicode__(self):
        return self.name



#treatment technologies model
class TreatmentTech(models.Model):
    #has a name
    name = models.CharField(max_length=128, unique=True)
    #has a description
    desc = models.TextField(default='test')
    #short description
    summary = models.TextField(default='test')
    #url testing to create dynamic functional links
    url = models.URLField()
    #has technical specification
    tech_spec = models.TextField(default='test')
    #has products
    products = models.TextField(default='test')
    #has byproducts
    byproducts = models.TextField(default='test')

    #has images (not yet implemented still some research needed on how to do this well )
    image = models.ImageField(upload_to="static")
    image2 = models.ImageField(upload_to="static")


    #many to many relationship with Waste
    waste = models.ManyToManyField(Waste)

    #mandatory
    def __unicode__(self):
        return self.name



#Waste Parameters model containing quantity info which is connected to the Parameters model
class WasteParameters(models.Model):
    #has a quantity
    quantity = models.FloatField(default=0)

     #linking
    parameters = models.ForeignKey(Parameters)
    waste = models.ForeignKey(Waste)

    #mandatory
    def __unicode__(self):
       return self.id


