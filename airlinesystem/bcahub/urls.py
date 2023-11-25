from django.contrib import admin
from django.urls import path, include
from bcahub.appviews import view

from bcahub.views import airline_views

urlpatterns = [
    path('pages/home', view.home, name='home'),
    path('pages/createtravel', airline_views.createtravel, name='createtravel'),
    path('pages/base', airline_views.base, name='base'),
    path('pages/store', airline_views.store, name='storename'),
    path('pages/airlines', view.airline, name='airline'),
    path('pages/riskaction', view.risk, name='risk'),
    path('pages/crew', view.crew, name='crew'),
    path('pages/journey', view.journey, name='journey')

    ]
