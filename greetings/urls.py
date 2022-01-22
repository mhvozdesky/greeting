from django.urls import path
from greetings import views


urlpatterns = [
    path('', views.Greetings.as_view(), name='greetings'),
]


