# website/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # name='home' allows us to use {% url 'home' %} in templates
    path('', views.home_view, name='home'),
    
    # --- ADD THE FOLLOWING NEW URLS ---
    path('services/', views.services_view, name='services'),
    path('about/', views.about_view, name='about'),
    path('work/', views.work_view, name='work'),
    path('contact/', views.contact_view, name='contact'),
    path('insights/', views.post_list_view, name='post_list'),
    path('insights/<slug:slug>/', views.post_detail_view, name='post_detail'),
]