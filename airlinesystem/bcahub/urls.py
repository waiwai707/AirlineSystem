from django.contrib import admin
from django.urls import path, include


from bcahub.views import airline_views

urlpatterns = [
   
 
    path('pages/createtravel', airline_views.createtravel, name='createtravel'),
    path('portalpages/updateViewtravel/<int:pk>/',airline_views.updateViewtravel, name='updateViewtravel'),
    path('pages/updatetravel/<int:pk>/', airline_views.updatetravel, name='updatetravel'),
    path('pages/base', airline_views.base, name='base'),
    path('pages/store', airline_views.store, name='storename'),
   
    path('pages/createairline', airline_views.createairline, name='createairline'),
    path('portalpages/updateViewairline/<int:pk>/',airline_views.updateViewairline, name='updateViewairline'),
    path('pages/updateairline/<int:pk>/', airline_views.updateairline, name='updateairline'),
    path('pages/baseairline', airline_views.baseairline, name='baseairline'),
    path('pages/storeairline', airline_views.storeairline, name='storeairline'),

    path('pages/createcrew', airline_views.createcrew, name='createcrew'),
    path('portalpages/updateViewcrew/<int:pk>/',airline_views.updateViewcrew, name='updateViewcrew'),
    path('pages/updatecrew/<int:pk>/', airline_views.updatecrew, name='updatecrew'),
    path('pages/basecrew', airline_views.basecrew, name='basecrew'),
    path('pages/storecrew', airline_views.storecrew, name='storecrew'),

    path('pages/createjourney', airline_views.createjourney, name='createjourney'),
    path('portalpages/updateViewjourney/<int:pk>/',airline_views.updateViewjourney, name='updateViewjourney'),
    path('pages/updatejourney/<int:pk>/', airline_views.updatejourney, name='updatejourney'),
    path('pages/basejourney', airline_views.basejourney, name='basejourney'),
    path('pages/storejourney', airline_views.storejourney, name='storejourney'),

    path('pages/createrisk', airline_views.createrisk, name='createrisk'),
    path('portalpages/updateViewrisk/<int:pk>/',airline_views.updateViewrisk, name='updateViewrisk'),
    path('pages/updaterisk/<int:pk>/', airline_views.updaterisk, name='updaterisk'),
    path('pages/baserisk', airline_views.baserisk, name='baserisk'),
    path('pages/storerisk', airline_views.storerisk, name='storerisk'),
]
    
