from django.urls import path
from . import views

urlpatterns = [
    path('', views.factorials_view, name='factorials'),
]
