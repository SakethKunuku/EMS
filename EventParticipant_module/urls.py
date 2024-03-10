from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'EventParticipant_module'
urlpatterns = [
path('viewevents', views.viewEvents, name='View Events'),
path('event_details_list',views.event_details_list,name = "event_details_list"),
path('submit_form/',views.submit_form,name = 'submit_form'),
path('add_eventparticipant_profile/',views.add_eventparticipant_profile,name = 'add_eventparticipant_profile'),
path('apply/<int:event_id>/',views.register_to_event,name ='register_to_event'),


]
