from django.urls import path
from . import views
app_name='Cars'

urlpatterns = [
    path('', views.home , name='home'),
    path('about/', views.about, name='about'),
    path('password/generate/', views.password, name='password'),
]