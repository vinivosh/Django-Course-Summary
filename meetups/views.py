from email.mime import image
from django.shortcuts import render
from django.http import HttpResponse

import meetups
from .models import Meetup



# Get all the meetups to list them
def index(request):
    meetups = Meetup.objects.all()

    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })

# Get the meetup details page
def meetupDetails(request, meetupSlug):
    try:
        selectedMeetup = Meetup.objects.get(slug=meetupSlug)

        return render(request, 'meetups/meetupDetails.html', {
            'meetupFound': True,
            'meetup': selectedMeetup
            })
    except Exception as exc:
        return render(request, 'meetups/meetupDetails.html', {
            'meetupFound': False
        })