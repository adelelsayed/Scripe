from django.conf.urls import url

from . import views

app_name = 'ScripeAlpha'

urlpatterns = [

    url(r'^snomed/(?P<piece>[^\n]+)$' , 
        views.ReplyString.as_view(), name = 'SnomedReplyString'  ),
    url(r'^ICD/(?P<piece>[^\n]+)$' , 
        views.ReplyStringICD.as_view(), name = 'ICDReplyString'  ),
    url(r'^test/(?P<piece>[a-zA-Z0-9_ ]+)$' , 
        views.test  )
]

#(?P<piece>[a-zA-Z0-9_ ]+)$' #regular expression for a single string 