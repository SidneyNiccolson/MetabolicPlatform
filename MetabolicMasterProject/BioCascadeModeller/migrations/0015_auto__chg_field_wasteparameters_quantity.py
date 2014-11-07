# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'WasteParameters.quantity'
        db.alter_column(u'BioCascadeModeller_wasteparameters', 'quantity', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):

        # Changing field 'WasteParameters.quantity'
        db.alter_column(u'BioCascadeModeller_wasteparameters', 'quantity', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        u'BioCascadeModeller.parameters': {
            'Meta': {'object_name': 'Parameters'},
            'desc': ('django.db.models.fields.TextField', [], {'default': "'test'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'False', 'unique': 'True', 'max_length': '128'}),
            'type': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '128'}),
            'unit': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '128'})
        },
        u'BioCascadeModeller.treatmenttech': {
            'Meta': {'object_name': 'TreatmentTech'},
            'desc': ('django.db.models.fields.TextField', [], {'default': "'test'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'waste': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['BioCascadeModeller.Waste']", 'symmetrical': 'False'})
        },
        u'BioCascadeModeller.waste': {
            'Meta': {'object_name': 'Waste'},
            'desc': ('django.db.models.fields.TextField', [], {'default': "'test'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'parametersList': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['BioCascadeModeller.Parameters']", 'through': u"orm['BioCascadeModeller.WasteParameters']", 'symmetrical': 'False'})
        },
        u'BioCascadeModeller.wasteparameters': {
            'Meta': {'object_name': 'WasteParameters'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameters': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['BioCascadeModeller.Parameters']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            'waste_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['BioCascadeModeller.Waste']"})
        }
    }

    complete_apps = ['BioCascadeModeller']