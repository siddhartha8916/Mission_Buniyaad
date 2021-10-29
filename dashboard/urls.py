from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('/statelevel/', views.stateLevel,name='stateLevel'),
    path('/districtlevel/', views.districtLevel,name='districtLevel'),
    path('/blocklevel/', views.blockLevel,name='blockLevel'),
    path('/login/', views.login,name='login'),
]
