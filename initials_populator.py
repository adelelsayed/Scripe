import os
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Scripe.settings')

import django
django.setup()

from ScripeAlpha.models import Snomed
from nltk.tokenize import word_tokenize


def initialize(sent):

        '''this method is to return initials of a synonym via tokenizing the synonym then taking the initials'''
        __theList = word_tokenize(sent)
        __initialsString = ''.join([ i[0] for i in __theList ] )
        return __initialsString

    
def poppy():
    for i in Snomed.objects.all():
        initialsString = initialize(i.synonym)
        if len(initialsString) > 1:
            i.initials = initialize(i.synonym)
            i.save()
        else:
            i.initials = i.synonym
            i.save()

        print i.ide
        
if __name__ == '__main__':

    print('pop script')
    poppy()
    print ('pop end')
