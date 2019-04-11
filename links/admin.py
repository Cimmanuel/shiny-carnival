from django.contrib import admin
from .models import Link, Vote

class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'owner')
admin.site.register(Link, LinkAdmin)

class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'link')
admin.site.register(Vote, VoteAdmin)