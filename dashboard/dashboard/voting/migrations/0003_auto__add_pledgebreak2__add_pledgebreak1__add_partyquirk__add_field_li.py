# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PledgeBreak2'
        db.create_table(u'voting_pledgebreak2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True)),
        ))
        db.send_create_signal(u'voting', ['PledgeBreak2'])

        # Adding model 'PledgeBreak1'
        db.create_table(u'voting_pledgebreak1', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True)),
        ))
        db.send_create_signal(u'voting', ['PledgeBreak1'])

        # Adding model 'PartyQuirk'
        db.create_table(u'voting_partyquirk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True)),
        ))
        db.send_create_signal(u'voting', ['PartyQuirk'])

        # Adding field 'Line.timestamp'
        db.add_column(u'voting_line', 'timestamp',
                      self.gf('django.db.models.fields.DateTimeField')(default=None, null=True),
                      keep_default=False)

        # Adding field 'Clip.timestamp'
        db.add_column(u'voting_clip', 'timestamp',
                      self.gf('django.db.models.fields.DateTimeField')(default=None, null=True),
                      keep_default=False)

        # Adding field 'Emotion.timestamp'
        db.add_column(u'voting_emotion', 'timestamp',
                      self.gf('django.db.models.fields.DateTimeField')(default=None, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'PledgeBreak2'
        db.delete_table(u'voting_pledgebreak2')

        # Deleting model 'PledgeBreak1'
        db.delete_table(u'voting_pledgebreak1')

        # Deleting model 'PartyQuirk'
        db.delete_table(u'voting_partyquirk')

        # Deleting field 'Line.timestamp'
        db.delete_column(u'voting_line', 'timestamp')

        # Deleting field 'Clip.timestamp'
        db.delete_column(u'voting_clip', 'timestamp')

        # Deleting field 'Emotion.timestamp'
        db.delete_column(u'voting_emotion', 'timestamp')


    models = {
        u'voting.clip': {
            'Meta': {'object_name': 'Clip'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'voting.emotion': {
            'Meta': {'object_name': 'Emotion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'voting.line': {
            'Meta': {'object_name': 'Line'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'})
        },
        u'voting.partyquirk': {
            'Meta': {'object_name': 'PartyQuirk'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'})
        },
        u'voting.pledgebreak1': {
            'Meta': {'object_name': 'PledgeBreak1'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'})
        },
        u'voting.pledgebreak2': {
            'Meta': {'object_name': 'PledgeBreak2'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'})
        }
    }

    complete_apps = ['voting']