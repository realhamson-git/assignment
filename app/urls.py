from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin , name = 'signin'),
    path('signup', views.signup , name = 'signup'),
    path('logout', views.Logout , name = 'logout'),
    path('dashboard', views.dashboard , name = 'dashboard'),
]