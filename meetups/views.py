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

def meetupDetails(request):
    selectedMeetup = {
        'title': 'Family Reunion',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Iaculis urna id volutpat lacus laoreet non curabitur. Ipsum dolor sit amet consectetur adipiscing elit ut aliquam purus. Dolor sit amet consectetur adipiscing elit pellentesque habitant morbi. Nunc mattis enim ut tellus elementum. Sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus. Eget egestas purus viverra accumsan. Scelerisque varius morbi enim nunc faucibus a. Nisi vitae suscipit tellus mauris a diam maecenas sed. Viverra orci sagittis eu volutpat odio facilisis. Suspendisse in est ante in nibh mauris cursus.\nSed egestas egestas fringilla phasellus faucibus scelerisque eleifend donec. Aliquet sagittis id consectetur purus ut. Vel facilisis volutpat est velit. Imperdiet proin fermentum leo vel orci porta non pulvinar. Condimentum vitae sapien pellentesque habitant morbi tristique senectus. Aliquet risus feugiat in ante metus dictum at tempor. In cursus turpis massa tincidunt dui ut ornare lectus. Massa ultricies mi quis hendrerit dolor magna eget est lorem. Id semper risus in hendrerit. Lorem ipsum dolor sit amet consectetur adipiscing elit. Nibh mauris cursus mattis molestie a iaculis at erat. Nibh mauris cursus mattis molestie a iaculis at erat pellentesque. Posuere lorem ipsum dolor sit. Sed felis eget velit aliquet sagittis id consectetur purus ut. Placerat duis ultricies lacus sed turpis tincidunt id aliquet risus. Placerat vestibulum lectus mauris ultrices eros in cursus turpis. Lacus sed viverra tellus in hac habitasse. Morbi tincidunt ornare massa eget egestas purus viverra. Lectus nulla at volutpat diam ut venenatis tellus in. Elementum eu facilisis sed odio morbi.'
        }

    return render(request, 'meetups/meetupDetails.html', {
        'meetupTitle': selectedMeetup['title'],
        'meetupDescription': selectedMeetup['Description']
        })