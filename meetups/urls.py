from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index, name='allMeetups'),    # my-domain.com/meetups
    path('meetups/<slug:meetupSlug>', views.meetupDetails, name='meetupDetails')    # my-domain.com/meetups/<a-dynamic-segment>
]