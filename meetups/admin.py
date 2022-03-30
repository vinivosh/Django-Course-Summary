from django.contrib import admin

from .models import Meetup, Location, Participant



class MeetupAdmin(admin.ModelAdmin):
    list_display =('title', 'location', 'date')
    list_filter = ('location', 'date')
    # This prepopulates the slug field, based on the title, when creating a new Meetup in the DB
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)