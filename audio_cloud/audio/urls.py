from django.urls import path 
from audio import views

name= "audio"

urlpatterns = [
    path('',views.index,name="index"),
    path('<str:type>/',views.audio_list,name='audio_list'),
    path('<str:type>/<int:pk>/',views.audio_list,name='audio_list'),
    path('create/<str:type>/',views.AudioCreateView.as_view(),name='audio_create'),
    path('delete/<str:type>/<int:pk>/',views.AudioDeleteView.as_view(),name='audio_create'),
    path('update/<str:type>/<int:pk>/',views.AudioUpdateView.as_view(),name='audio_create'),
]
