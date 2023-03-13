from football.views import *

from django.urls import path

app_name='nothing'

urlpatterns=[
    path('messi/',messi,name='messi'),
]