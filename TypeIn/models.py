# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Diagnosis(models.Model):
    '''this model is to hold diagnosis data recorded for patients'''
    ide = models.AutoField(primary_key = True)
    diagnosis_documented = models.CharField(max_length = 255, null = False, blank = False)
    status = models.CharField(max_length = 255, null = False, blank = False,
                                choices = (('Deteriorating','Deteriorating'),
                                    ('In Remission','In Remission'),
                                            ('Active','Active'),
                                            ('Resolved','Resolved'))
                                            ,default=('Active','Active'))