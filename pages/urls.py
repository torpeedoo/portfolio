from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path("contact_me", views.contact_me, name='contact_me')
]