from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('signup', views.sign_up),
    path('login', views.log_in),
    path('whoami', views.who_am_i),
    path('logout', views.log_out)
]