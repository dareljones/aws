from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name='site-home'),
    path('senti', include('sentimeter.urls')),
    path('ocr', include('ocr.urls')),


    ]
