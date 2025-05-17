from django.urls import path
from Guest import views
app_name='Guest'
urlpatterns = [
    path('Ajaxplace/',views.ajaxplace,name='ajaxplace'),
    path('UserRegistration/',views.userregistration,name='UserRegistration'),
    path('Login/',views.login,name='login'),
    path('TravelAgencyRegistration/',views.travelagencyregistration,name='TravelAgencyRegistration'),
    path('',views.index,name='index'),
    path('Search/',views.search,name='Search'),
    path('ViewLocation/<int:id>',views.viewlocation,name='ViewLocation'),
    path('ajaxlocation/',views.ajaxlocation,name='ajaxlocation'),
]