# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


class Accounts(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase. This field type is a guess.
    vorname = models.TextField(db_column='Vorname')  # Field name made lowercase. This field type is a guess.
    geburtsdatum = models.DateField(db_column='Geburtsdatum', blank=True, null=True)  # Field name made lowercase.
    verguenstigung = models.IntegerField(db_column='Verguenstigung')  # Field name made lowercase.
    wohnort = models.TextField(db_column='Wohnort', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'accounts'


class Mitarbeiter(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase. This field type is a guess.
    vorname = models.TextField(db_column='Vorname')  # Field name made lowercase. This field type is a guess.
    teilzeit = models.IntegerField(db_column='Teilzeit')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mitarbeiter'


class User(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    vorname = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    verguenstigung = models.CharField(max_length=200, default='Nein')

    def __str__(self):
        return self.name
