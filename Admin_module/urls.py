from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProjectHomePage, name='ProjectHomePage'),
    path('EventManagerHomePage', views.EventManagerHomePage, name='EventManagerHomePage'),
    path('EventParticipantHomePage', views.EventParticipantHomePage, name='EventParticipantHomePage'),
    path('signup', views.Signup, name='signup'),
    path('signup1',views.signup1,name='signup1'),
    path('login', views.login, name='login'),
    path('login1', views.login1, name='login1'),
    path('logout', views.logout, name='logout'),
    path('account_details', views.account_details, name='account_details'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('AboutUs', views.AboutUs, name='AboutUs'),
    path('OurServices', views.OurServices, name='OurServices'),
    path('ContactUs', views.ContactUs, name='ContactUs'),
    path('Gallery', views.Gallery, name='Gallery'),

]