from django.contrib import admin
from django.urls import path
from myapp import views
from .views import *


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('reg/', RegView.as_view()),
]
