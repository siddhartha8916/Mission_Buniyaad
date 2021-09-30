from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('uploadcontent_1', views.uploadcontent_1,name='uploadcontent_1'),
    path('STD.I', views.view_content_1,name='view_content_1'),
]
