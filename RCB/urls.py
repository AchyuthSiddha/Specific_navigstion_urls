from django.urls import path
from RCB.views import *
app_name='RCB'
urlpatterns=[
    path('Virat/',Virat,name='Virat')
]