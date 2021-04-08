from django.urls import path, include
from . import views
from .views import RegisterAPI, LoginAPI, UserAPI, Raw_Sighting_Input
from knox import views as knox_views

urlpatterns=[
    path('Species/', views.Species_list.as_view()),
    path('Refined_Sightings/', views.Refined_Sightings_list.as_view()),
    path('Species/<int:pk>', views.Species_element.as_view()),
    path('Refined_Sightings/Species/', views.Refined_Sightings_Species_list.as_view()),
    path('Refined_Sightings/Location/', views.Refined_Sightings_Locations_list.as_view()),
    path('Locations/<int:pk>', views.Location_element.as_view()),
    path('Raw_Sighting/', views.Raw_Sighting_Input.as_view()),
    path('Locations/', views.Locations_list.as_view()),
    path('auth', include('knox.urls')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('auth/logoutall', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('auth/user', UserAPI.as_view()),
    path('Ratification_List/', views.Ratification_List.as_view()),
]