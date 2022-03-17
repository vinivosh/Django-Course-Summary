from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index),    # my-domain.com/meetups
    path('meetups/<slug:meetupSlug>', views.meetupDetails)    # my-domain.com/meetups/<a-dynamic-segment>
]