from django.conf.urls import url
from django.contrib import admin
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('myapp.urls')),
    path('admin/', admin.site.urls),
]
