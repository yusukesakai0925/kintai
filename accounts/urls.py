from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import SignUpView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]

