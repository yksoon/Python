# my_to_do_app > urls.py
from django.urls import path

# url 경로 설정
from .import views

urlpatterns = [
    path('', views.index)
]