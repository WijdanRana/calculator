from django.urls import path, include
from . import views

urlpatterns = [
    path('calculate/',views.cal)
    
]
