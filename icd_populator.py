import os
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Scripe.settings')

import django
django.setup()

from ScripeAlpha.models import ICD
from nltk.tokenize import word_tokenize



data = pd.read_csv("D:\\script prescript\\ICD-10-codes.csv",header=0,low_memory=False)

#for i in data[['Full Description','Category Title']].head().iterrows():
    #print i[1]['Full Description']

def initialize(sent):

        '''this method is to return initials of a synonym via tokenizing the synonym then taking the initials'''
        
        _theList = word_tokenize(sent)
        _initialsString = ''.join([ i[0] for i in _theList ] )
        if len(_initialsString)==1: _initialsString = sent
        return _initialsString

def poppy(data):
    
    for i in data[['Full Description','Category Title']].iterrows():
        ICD.objects.create(
            synonym = i[1]['Full Description'].decode('ascii','ignore').encode("utf-8"),
            category = i[1]['Category Title'].decode('ascii','ignore').encode("utf-8"),
            initials = initialize(i[1]['Full Description'].decode('ascii','ignore').encode("utf-8"))
            )
        
 
if __name__ == '__main__':

    print('pop script')
    poppy(data)
    print ('pop end')
