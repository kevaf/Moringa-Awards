from django.conf.urls import url, static
from django.urls import path
from . import views
from django.conf import settings

urlpatterns=[
    url(r'^$', views.index, name='home'),
    path('profile/',views.profile,name = 'profile'),
]
