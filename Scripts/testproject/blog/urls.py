from django.contrib import admin  
from django.urls import path  
from blog import views  
from django.conf.urls import url
 
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('',views.index),
    url(r'^create$', views.create, name='create'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
]
