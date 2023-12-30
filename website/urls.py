from django .urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.first, name='first'),
    path('website/', views.website, name ='website'),
]