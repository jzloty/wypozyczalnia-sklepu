from django.contrib import admin
from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt

app_name = 'wypozyczalnia'
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('szukajGry', csrf_exempt(views.szukajGry), name="szukajGry")
]
