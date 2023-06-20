from django.urls import path

from .views import index, get_openai_summary

urlpatterns = [
    path('', index, name='home'), 
    path('get_openai_summary/', get_openai_summary, name='get_openai_summary'),
]