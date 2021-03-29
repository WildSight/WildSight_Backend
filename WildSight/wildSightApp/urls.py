from django.urls import path
from . import views

urlpatterns=[
    path('Species/', views.Species_list.as_view()),
    path('Refined_Sightings/', views.Refined_Sightings_list.as_view()),
    path('Species/<int:pk>', views.Species_element.as_view()),
    path('Refined_Sightings/Species/<int:pk>', views.Refined_Sightings_Species_list.as_view()),
    path('Refined_Sightings/Location/<int:pk>', views.Refined_Sightings_Locations_list.as_view()),
    path('Locations/', views.Locations_list.as_view()),
]