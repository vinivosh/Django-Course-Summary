from email.mime import image
from django.shortcuts import render, redirect
from django.http import HttpResponse

import meetups
from .models import Meetup
from .forms import ParticipantForm



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

        if request.method == 'GET':
            participantForm = ParticipantForm()
        else:
            # There's an annoying limitation on this form: you can't use the same e-mail to enter different meetups for now. This will be corrected later.
            participantForm = ParticipantForm(request.POST)
            print(request.POST)

            # If the form entered by the user is valid, save the participant to the DB!
            if participantForm.is_valid():
                # Saving the participant to the Participant table and to a variable
                participant = participantForm.save()
                # Adding the participant to the "participants" field in the current meetup
                selectedMeetup.participants.add(participant)
                # Redirecting to the confirmation page
                return redirect('meetupRegisterSuccess', meetupSlug, request.POST['email'])

        return render(request, 'meetups/meetupDetails.html', {
            'meetupFound': True,
            'meetup': selectedMeetup,
            'form': participantForm
        })
    except Exception as exc:
        print(exc)
        return render(request, 'meetups/meetupDetails.html', {
            'meetupFound': False
        })


# Get the meetup details page
def meetupRegisterSuccess(request, meetupSlug, email):
    try:
        selectedMeetup = Meetup.objects.get(slug=meetupSlug)

        return render(request, 'meetups/registration-success.html', {
            'meetupFound': True,
            'meetup': selectedMeetup,
            'email': email
        })
    except Exception:
        return render(request, 'meetups/registration-success.html', {
            'meetupFound': False
        })