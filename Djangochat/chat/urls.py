from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [

    path('',views.home,name='home' ),
    path('home/',views.home,name='home' ),
    path('aboutus/',views.aboutus,name='aboutus' ),
    path('<str:room>/',views.room,name='room'),
    path('checkview',views.checkview,name='checkview' ),
    path('send',views.send,name='send' ),
    path('getMessages/<str:room>/',views.getMessages,name='getMessages'),

]

