from django.urls import path
from .import views 

urlpatterns = [
    path('k/',views.get_name)
]
