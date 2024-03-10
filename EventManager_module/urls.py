from django.contrib import admin
from django.urls import path, include
from . import views
from .views import accept_application
from .views import reject_application



app_name = 'EventManager_module'
urlpatterns = [
    path('eventpost/',views.Eventpost,name='Event Post'),
    path('add_event_details', views.add_event_details,name='add_event_details'),
    path('view/',views.view_event_details,name='view_event_details'),
    path('edit/<int:event_id>',views.edit_event_details,name='edit_event_details'),
    path('delete/<int:event_id>/', views.delete_event_details, name='delete_event_details'),
    path('event_application_list/',views.event_application_list, name = 'event_application_list'),
    path('KLU/', views.KLU, name='EventPostklu'),
    path('KLH/', views.KLH, name='EventPostklh'),
    path('vitap/',views.vitap,name = 'EventPostvitap'),
    path('vitchennai/', views.vitchennai, name='EventPostvitchennai'),
    path('srm/', views.srm, name='EventPostsrm'),
    path('gitam/', views.gitam, name='EventPostgitam'),
    path('gmrit/', views.gmrit, name='EventPostgmrit'),
    path('AU/', views.AU, name='EventPostau'),
    path('accept_application/<int:event_application_id>/', views.accept_application, name='accept_application'),
    path('reject_application/<int:event_application_id>/', reject_application, name='reject_application'),

]