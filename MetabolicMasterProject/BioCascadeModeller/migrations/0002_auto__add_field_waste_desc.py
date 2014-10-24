# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Waste.desc'
        db.add_column(u'BioCascadeModeller_waste', 'desc',
                      self.gf('django.db.models.fields.TextField')(default='description'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Waste.desc'
        db.delete_column(u'BioCascadeModeller_waste', 'desc')


    models = {
        u'BioCascadeModeller.waste': {
            'Meta': {'object_name': 'Waste'},
            'desc': ('django.db.models.fields.TextField', [], {'default': "'description'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['BioCascadeModeller']