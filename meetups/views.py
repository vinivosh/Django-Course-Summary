from django.shortcuts import render
from django.http import HttpResponse

import meetups

# Create your views here.

def index(request):
    meetups = [
        {'title': 'Family Reunion'},
        {'title': 'Coffee Break 1.0'},
        {'title': 'Intervention For Our Dear Friend'},
        {'title': 'Coffee Break 2.0'}
    ]

    return render(request, 'meetups/index.html', {
        'showMeetups': True,
        'meetups': meetups
    })