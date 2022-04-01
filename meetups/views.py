from email.mime import image
from django.shortcuts import render, redirect
from django.http import HttpResponse

import meetups
from .models import Meetup, Participant
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

        # If method POST, then we're processing a registration
        if request.method == 'POST':
            participantForm = ParticipantForm(request.POST)

            # If the form entered by the user is valid, create and save/just save the participant to the DB
            if participantForm.is_valid():
                # Getting the email field from the form
                participantEmail = participantForm.cleaned_data['email']
                # Create and save the new participant to the Participant table and to a variable. If it already exists, just get the existing entry.
                participant, wasCreated = Participant.objects.get_or_create(email=participantEmail) # Remember: the get_or_create method returns a tuple, with the participant it got or created and a boolean flag "wasCreated"
                # Adding the new or existing participant to the "participants" field in the current meetup
                selectedMeetup.participants.add(participant)
                # Redirecting to the confirmation page
                return redirect('meetupRegisterSuccess', meetupSlug, participantForm.cleaned_data['email'])

        # Else, the method's probably GET and we're just returning the page with the empty form for a possible registration
        else:
            participantForm = ParticipantForm()

        # For any method, we must return the page anyway. If a registration was susccesseful though, we don't get here, as we're redirected to the 'meetupRegisterSuccess' page
        return render(request, 'meetups/meetupDetails.html', {
            'meetupFound': True,
            'meetup': selectedMeetup,
            'form': participantForm
        })

    # If the meetup with the corresponding slug wasn't found, return a "not found" version of the page
    except Exception as exc:
        print(exc)
        return render(request, 'meetups/meetupDetails.html', {
            'meetupFound': False
        })


# Registration success page
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