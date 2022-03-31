from django.urls import path
from . import views

urlpatterns = [
    # my-domain.com/meetups
    path('meetups/', views.index, name='allMeetups'),
    # my-domain.com/meetups/<a-dynamic-segment>
    path('meetups/<slug:meetupSlug>', views.meetupDetails, name='meetupDetails'),
    # my-domain.com/meetups/<a-dynamic-segment>/register-success
    path('meetups/<slug:meetupSlug>/register-success&email=<email>', views.meetupRegisterSuccess, name='meetupRegisterSuccess')
]