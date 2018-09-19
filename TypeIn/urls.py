from django.conf.urls import url

from . import views

app_name = 'TypeIn'

urlpatterns = [

    url(r'type/$' , 
        views.TyperIn , name = 'TyperIn'  ),
    url(r'looker/$' , 
        views.lookerUp , name = 'lookerUp'  ),
    url(r'former/(?P<diagList>[^\n]+)$' , 
        views.former , name = 'former'  ),
]