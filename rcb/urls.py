from django.urls import path
from rcb.views import *
app_name='potti'
urlpatterns=[
    path('virat/',virat,name='virat'),
]