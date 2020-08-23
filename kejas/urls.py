from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('addkeja/', views.addkeja, name='addkeja'),
    path('success/', views.success, name='success'),
    path('<int:keja_id>/', views.detail, name='detail'),
]  
