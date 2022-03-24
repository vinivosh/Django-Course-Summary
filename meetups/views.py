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
            'location': 'Pindamonhangaba',
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
        'meetups': meetups
    })

def meetupDetails(request, meetupSlug):
    print('#DEBUG\n' + meetupSlug + '\n\n')
    selectedMeetup = {
        'title': 'Family Reunion',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Iaculis urna id volutpat lacus laoreet non curabitur. Ipsum dolor sit amet consectetur adipiscing elit ut aliquam purus. Dolor sit amet consectetur adipiscing elit pellentesque habitant morbi. Nunc mattis enim ut tellus elementum. Sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus. Eget egestas purus viverra accumsan. Scelerisque varius morbi enim nunc faucibus a. Nisi vitae suscipit tellus mauris a diam maecenas sed. Viverra orci sagittis eu volutpat odio facilisis. Suspendisse in est ante in nibh mauris cursus. Sed egestas egestas fringilla phasellus faucibus scelerisque eleifend donec. Aliquet sagittis id consectetur purus ut. Vel facilisis volutpat est velit. Imperdiet proin fermentum leo vel orci porta non pulvinar. Condimentum vitae sapien pellentesque habitant morbi tristique senectus. Aliquet risus feugiat in ante metus dictum at tempor. In cursus turpis massa tincidunt dui ut ornare lectus.'
        }

    return render(request, 'meetups/meetupDetails.html', {
        'meetupTitle': selectedMeetup['title'],
        'meetupDescription': selectedMeetup['description']
        })