import os
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Scripe.settings')

import django
django.setup()

from ScripeAlpha.models import Snomed


data = pd.read_csv("D:\\script prescript\\snomed_ct_findings.csv",header=0)




def poppy(dc):
    for i in data.ix[97762:]['STRING']:
        
        Snomed.objects.create(synonym = i.decode('ascii','ignore').encode("utf-8"))
        
        
if __name__ == '__main__':

    print('pop script')
    poppy(data)
    print ('pop end')



