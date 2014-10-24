from django.db import models

#waste model
class Waste(models.Model):
    #has a name
    name = models.CharField(max_length=128, unique=True)
    #has a description
    desc = models.TextField(default='test')


    def __unicode__(self):
        return self.name
