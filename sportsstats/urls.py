from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('sharing/', views.sharingPage, name='share'),
    path('about/', views.AboutPage.as_view(), {'onSale': False}, name='about')
]
