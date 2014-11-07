# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Waste'
        db.create_table(u'BioCascadeModeller_waste', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('desc', self.gf('django.db.models.fields.TextField')(default='test')),
        ))
        db.send_create_signal(u'BioCascadeModeller', ['Waste'])


    def backwards(self, orm):
        # Deleting model 'Waste'
        db.delete_table(u'BioCascadeModeller_waste')


    models = {
        u'BioCascadeModeller.waste': {
            'Meta': {'object_name': 'Waste'},
            'desc': ('django.db.models.fields.TextField', [], {'default': "'test'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['BioCascadeModeller']