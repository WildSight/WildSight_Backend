from django.urls import path, include, re_path
from . import views
from .views import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views

urlpatterns=[
    path('Species/', views.Species_list.as_view()),
    path('Refined_Sightings/', views.Refined_Sightings_list.as_view()),
    path('Species/<int:pk>', views.Species_element.as_view()),
    path('Refined_Sightings/Species/<int:pk>', views.Refined_Sightings_Species_list.as_view()),
    path('Refined_Sightings/Location/<int:pk>', views.Refined_Sightings_Locations_list.as_view()),
    path('Locations/', views.Locations_list.as_view()),
    path('auth', include('knox.urls')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/user', UserAPI.as_view())
]