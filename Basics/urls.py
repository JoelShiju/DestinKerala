from django.urls import path,include
from Basics import views
urlpatterns = [
    path('add/',views.add,name='add'),
    path('largest/',views.largest,name='largest'),
    path('calculator/',views.calculator,name='calculator')
]