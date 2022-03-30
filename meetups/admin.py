from django.contrib import admin

from .models import Meetup, Location



class MeetupAdmin(admin.ModelAdmin):
    list_display =('title', 'slug')
    list_filter = ('location',)
    # This prepopulates the slug field, based on the title, when creating a new Meetup in the DB
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)