from django.contrib import admin
from django.urls import path,include
from django.urls.conf import re_path
from django.views.static import serve 
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.home,name='home'),
    path('uploadcontent', views.uploadcontent,name='uploadcontent'),
    path('view_content/<int:id>', views.view_content,name='view_content'),
    # path('upload_recommended', views.upload_recommended,name='recommended'),

]
