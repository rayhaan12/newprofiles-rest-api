from django.contrib import admin

from newprofiles_api import models


admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
