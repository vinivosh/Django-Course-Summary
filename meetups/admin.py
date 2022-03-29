from django.contrib import admin

from .models import Meetup



class MeetupAdmin(admin.ModelAdmin):
    list_display =('title', 'slug')
    # list_filter = ('title',)
    # This prepopulates the slug field, based on the title, when creating a new Meetup in the DB
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Meetup, MeetupAdmin)