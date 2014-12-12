# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Parameters'
        db.create_table(u'BioCascadeModeller_parameters', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('desc', self.gf('django.db.models.fields.TextField')(default='test')),
        ))
        db.send_create_signal(u'BioCascadeModeller', ['Parameters'])

        # Adding model 'Waste'
        db.create_table(u'BioCascadeModeller_waste', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('desc', self.gf('django.db.models.fields.TextField')(default='test')),
            ('imageWaste', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'BioCascadeModeller', ['Waste'])

        # Adding model 'TreatmentTech'
        db.create_table(u'BioCascadeModeller_treatmenttech', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('desc', self.gf('django.db.models.fields.TextField')(default='test')),
            ('summary', self.gf('django.db.models.fields.TextField')(default='test')),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('tech_spec', self.gf('django.db.models.fields.TextField')(default='test')),
            ('products', self.gf('django.db.models.fields.TextField')(default='test')),
            ('byproducts', self.gf('django.db.models.fields.TextField')(default='test')),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'BioCascadeModeller', ['TreatmentTech'])

        # Adding M2M table for field waste on 'TreatmentTech'
        m2m_table_name = db.shorten_name(u'BioCascadeModeller_treatmenttech_waste')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('treatmenttech', models.ForeignKey(orm[u'BioCascadeModeller.treatmenttech'], null=False)),
            ('waste', models.ForeignKey(orm[u'BioCascadeModeller.waste'], null=False))
        ))
        db.create_unique(m2m_table_name, ['treatmenttech_id', 'waste_id'])

        # Adding model 'WasteParameters'
        db.create_table(u'BioCascadeModeller_wasteparameters', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quantity', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('parameters', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['BioCascadeModeller.Parameters'])),
            ('waste', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['BioCascadeModeller.Waste'])),
        ))
        db.send_create_signal(u'BioCascadeModeller', ['WasteParameters'])


    def backwards(self, orm):
        # Deleting model 'Parameters'
        db.delete_table(u'BioCascadeModeller_parameters')

        # Deleting model 'Waste'
        db.delete_table(u'BioCascadeModeller_waste')

        # Deleting model 'TreatmentTech'
        db.delete_table(u'BioCascadeModeller_treatmenttech')

        # Removing M2M table for field waste on 'TreatmentTech'
        db.delete_table(db.shorten_name(u'BioCascadeModeller_treatmenttech_waste'))

        # Deleting model 'WasteParameters'
        db.delete_table(u'BioCascadeModeller_wasteparameters')


    models = {
        u'BioCascadeModeller.parameters': {
            'Meta': {'object_name': 'Parameters'},
            'desc': ('django.db.models.fields.TextField', [], {'default': "'test'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'BioCascadeModeller.treatmenttech': {
            'Meta': {'object_name': 'TreatmentTech'},
            'byproducts': ('django.db.models.fields.TextField', [], {'default': "'test'"}),
            'desc': ('django.db.models.fields.TextField', [], {'default': "'test'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'products': ('django.db.models.fields.TextField', [], {'default': "'test'"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "'test'"}),
            'tech_spec': ('django.db.models.fields.TextField', [], {'default': "'test'"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'waste': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['BioCascadeModeller.Waste']", 'symmetrical': 'False'})
        },
        u'BioCascadeModeller.waste': {
            'Meta': {'object_name': 'Waste'},
            'desc': ('django.db.models.fields.TextField', [], {'default': "'test'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageWaste': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'parametersList': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['BioCascadeModeller.Parameters']", 'through': u"orm['BioCascadeModeller.WasteParameters']", 'symmetrical': 'False'})
        },
        u'BioCascadeModeller.wasteparameters': {
            'Meta': {'object_name': 'WasteParameters'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameters': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['BioCascadeModeller.Parameters']"}),
            'quantity': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'waste': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['BioCascadeModeller.Waste']"})
        }
    }

    complete_apps = ['BioCascadeModeller']