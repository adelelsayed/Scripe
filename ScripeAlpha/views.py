# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse

from rest_framework.generics import ( ListAPIView, 
RetrieveAPIView)

from nltk.tokenize import word_tokenize
import json

from .models import Snomed, ICD
from .serializers import SnomedSerial,ICDSerial
# Create your views here.



class ReplyString (ListAPIView):

    #queryset = Snomed.objects.all()
    serializer_class = SnomedSerial
    #lookup_field = 'synonym'
    #lookup_url_kwarg = 'piece'

    

    def get_queryset(self):

        '''i am assuming that no abbreviation of a disease name would cexceed 5 letters
        and because initials of one word diseases is the disease synonym itself, it would be safe 
        to lookup initials for 5 letters synonyms '''

        piece = self.kwargs['piece']
        piece = json.loads(piece)
        piece = [ i.encode('utf-8') for i in piece]
        
        if len(piece) ==1:
            if len(piece[0]) >= 5:
                datas = Snomed.objects.filter(synonym__icontains = piece[0])  
                                                
            else:
                datas = Snomed.objects.filter(initials__icontains = piece[0])

        else:
            datas = Snomed.objects.filter(synonym = '')
            
            for i in piece:
                if len(i) >= 5:
                    datas1 = Snomed.objects.filter(synonym__icontains = i)  
                                           
                else:
                    
                    datas1 = Snomed.objects.filter(initials__icontains = i)
                
                datas = datas.union(datas1)
        
        datasSerial =SnomedSerial(datas , many=True).data

        return datasSerial
             
    def get(self, request , **kwargs):
        datas = self.get_queryset()
        
        url = reverse('TypeIn:former' , kwargs={'diagList' : datas }) 
        
        return HttpResponseRedirect(url)
    

class ReplyStringICD (ListAPIView):

    #queryset = Snomed.objects.all()
    serializer_class = ICDSerial
    #lookup_field = 'synonym'
    #lookup_url_kwarg = 'piece'

    

    def get_queryset(self):

        '''i am assuming that no abbreviation of a disease name would cexceed 5 letters
        and because initials of one word diseases is the disease synonym itself, it would be safe 
        to lookup initials for 5 letters synonyms '''

        piece = self.kwargs['piece']
        piece = json.loads(piece)
        piece = [ i.encode('utf-8') for i in piece]
        
        if len(piece) ==1:
            if len(piece[0]) >= 5:
                datas = ICD.objects.filter(synonym__icontains = piece[0])  
                                                
            else:
                datas = ICD.objects.filter(initials__icontains = piece[0])

        else:
            datas = ICD.objects.filter(synonym = '')
            
            for i in piece:
                if len(i) >= 5:
                    datas1 = ICD.objects.filter(synonym__icontains = i)  
                                           
                else:
                    
                    datas1 = ICD.objects.filter(initials__icontains = i)
                
                datas = datas.union(datas1)
        
        datasSerial =ICDSerial(datas , many=True).data

        return datasSerial
    '''
    def get(self, request , **kwargs):
        datas = self.get_queryset()
        
        url = reverse('TypeIn:former' , kwargs={'diagList' : datas }) 
        
        return HttpResponseRedirect(url)
    '''

      
    

def test (request, piece):
    
    return HttpResponse('piece is{}'.format(piece))
