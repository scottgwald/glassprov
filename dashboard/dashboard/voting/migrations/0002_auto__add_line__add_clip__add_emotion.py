# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Line'
        db.create_table(u'voting_line', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'voting', ['Line'])

        # Adding model 'Clip'
        db.create_table(u'voting_clip', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'voting', ['Clip'])

        # Adding model 'Emotion'
        db.create_table(u'voting_emotion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'voting', ['Emotion'])


    def backwards(self, orm):
        # Deleting model 'Line'
        db.delete_table(u'voting_line')

        # Deleting model 'Clip'
        db.delete_table(u'voting_clip')

        # Deleting model 'Emotion'
        db.delete_table(u'voting_emotion')


    models = {
        u'voting.clip': {
            'Meta': {'object_name': 'Clip'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'voting.emotion': {
            'Meta': {'object_name': 'Emotion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'voting.line': {
            'Meta': {'object_name': 'Line'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['voting']