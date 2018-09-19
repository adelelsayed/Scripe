# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Snomed(models.Model):
    '''this model is to hold snomed synonyms'''
    ide = models.AutoField(primary_key = True)
    synonym = models.CharField(max_length = 255, null = False, blank = False)
    initials = models.CharField(max_length = 255)

class ICD(models.Model):
    '''this model is to hold ICD synonyms'''
    ide = models.AutoField(primary_key = True)
    synonym = models.CharField(max_length = 255, null = False, blank = False)
    category = models.CharField(max_length = 255, null = False, blank = False)
    initials = models.CharField(max_length = 255)

