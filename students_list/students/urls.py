from django. urls import path
from . import views
urlpatterns=[
    path('present/',views.registerattendance,name="prese_nt")
]