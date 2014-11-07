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

        # Adding model 'TreatmentTech'
        db.create_table(u'BioCascadeModeller_treatmenttech', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('desc', self.gf('django.db.models.fields.TextField')(default='test')),
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


    def backwards(self, orm):
        # Deleting model 'Waste'
        db.delete_table(u'BioCascadeModeller_waste')

        # Deleting model 'TreatmentTech'
        db.delete_table(u'BioCascadeModeller_treatmenttech')

        # Removing M2M table for field waste on 'TreatmentTech'
        db.delete_table(db.shorten_name(u'BioCascadeModeller_treatmenttech_waste'))


    models = {
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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['BioCascadeModeller']