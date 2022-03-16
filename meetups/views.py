from django.shortcuts import render
from django.http import HttpResponse

import meetups

# Create your views here.

def index(request):
    meetups = [
        {
            'title': 'Family Reunion',
            'location': 'Itaporã',
            'slug': 'family-reunion-itapora'
        },
        {
            'title': 'Coffee Break 1.0',
            'location': 'Pindamonhangama',
            'slug': 'coffee-break-pindamonhangaba'
        },
        {
            'title': 'Intervention For Our Dear Friend',
            'location': 'Patos de Minas',
            'slug': 'intervention-for-our-dear-friend-patos-de-minas'
        },
        {
            'title': 'Coffee Break 2.0',
            'location': 'Chuí',
            'slug': 'coffee-break-chui'
        }
    ]

    return render(request, 'meetups/index.html', {
        'showMeetups': True,
        'meetups': meetups
    })