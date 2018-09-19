# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse


from .models import Diagnosis
from .forms import DiagnosisForm

# Create your views here.
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag, RegexpParser

import json

def TyperIn (request):

    DiagnosisFormTemplate = DiagnosisForm()

    return render(request, 'trial1.html' , {'DiagnosisFormTemplate':DiagnosisFormTemplate} )

def lookerUp(request):

    text = json.loads(request.GET.keys()[0])['text']
    
    
    sentList = [ [sent.encode('utf-8')] for sent in sent_tokenize(text.decode('ascii',"ignore").encode("ascii"))]

    wordList = [ word_tokenize(sent[0]) for sent in sentList   ]

    stopWordSet = set(stopwords.words('english'))
    stopWordSet.add('pt')
    stopWordSet.add('patient')


    for i in wordList:
        for x in i:
            if x in  stopWordSet:
                i.remove(x)
    
    chunk = """ Chunk: {<N.*>+<N.*>+|<J.*>+<N.*>+|<J.*>+|<N.*>+} """
    chunker = RegexpParser(chunk)

    wordList = [pos_tag(wordLister) for wordLister in wordList]

    prowordList = [ chunker.parse(i) for i in wordList ]


    newchunckedTextList= [ i for x in prowordList for i in x.subtrees() if i.label() == 'Chunk']

    featuredWords = [ x.leaves() for x in newchunckedTextList]
    
    for i in range(len(featuredWords)):
        featuredWords[i] = [ x[0] for x in featuredWords[i] if type(x) ==  type(tuple())]
        featuredWords[i] = ' '.join(featuredWords[i])

   

    jsonfeaturedWords = json.dumps(featuredWords)
    

    urlICD = reverse("ScripeAlpha:ICDReplyString",
                     kwargs={'piece': jsonfeaturedWords })

    #urlSnomed = reverse("ScripeAlpha:SnomedReplyString", kwargs={'piece': jsonfeaturedWords })

    return HttpResponseRedirect( urlICD )

def former(request , diagList) :
    
    
    diagList = json.dumps(diagList)
    
    return HttpResponse(diagList)