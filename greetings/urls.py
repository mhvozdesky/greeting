from django.urls import path
from greetings import views

urlpatterns = [
    path('', views.greetings, name='greetings'),
]