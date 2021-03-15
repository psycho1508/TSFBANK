from . import views
from django.urls import path

urlpatterns = [
  
    path('',views.homeview, name='home'),
    path('transferlist',views.transferlistview, name='transferlist'),
    path('user/<str:name>/confirmation',views.confirmationView, name='confirmation'),
    path('userView/<str:name>',views.userView, name='userView'),
]



    