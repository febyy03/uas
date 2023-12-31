from django .urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('amed/', views.amed, name='amed'),
    path('pandawa/', views.pandawa, name='pandawa'),
    path('melasti/', views.melasti, name='melasti'),
    path('kuta/', views.kuta, name='kuta'),
    path('jimbaran/', views.jimbaran, name='jimbaran'),
    #path('', views.first, name='first'),
    #path('website/', views.website, name ='website'),
]