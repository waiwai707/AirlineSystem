from django.contrib import admin
from django.urls import path, include
from bcahub.appviews import view
from .views import *

urlpatterns = [
    path('pages/home', view.home, name='home'),
    path('pages/airlines', view.airline, name='airline'),
    path('pages/riskaction', view.risk, name='risk'),
    path('pages/crew', view.crew, name='crew'),
    path('pages/journey', view.journey, name='journey')
    ]
