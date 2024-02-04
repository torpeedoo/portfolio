from django.contrib import admin

from pages.models import Socials

class SocialsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Socials, SocialsAdmin)


