

from django.urls import path,include
from . import views

urlpatterns = [
    path('datapush', views.data_push),
    path('display',views.display),
    path('movies/<int:movie_id>/', views.detail),
    path('<str:prefix>/', views.prefix),
    path('search/<str:string>/', views.search),
    path('deep_search/<str:string>/', views.deep_search),
    path('',views.style),

]
