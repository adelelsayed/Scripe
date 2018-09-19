from rest_framework import serializers

from .models import Snomed,ICD

class SnomedSerial(serializers.ModelSerializer):


    class Meta:
        model = Snomed
        fields = ('synonym',)

class ICDSerial(serializers.ModelSerializer):


    class Meta:
        model = ICD
        fields = ('synonym',)