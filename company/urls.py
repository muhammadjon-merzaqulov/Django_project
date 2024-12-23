from django.urls import path
from .views import homePageView, teamPageView, aboutPageView, contactPageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('team/', teamPageView, name='team'),
    path('about/', aboutPageView, name='about'),
    path('contact-us/', contactPageView, name='contact-us'),
]