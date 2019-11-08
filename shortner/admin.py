from django.contrib import admin
from .models import *
# Register your models here.


class urldetailsAdmin(admin.ModelAdmin):
    list_display 	= ('name', 'full_url', 'short_url', 'key', 'created_on')
    list_filter 	= ['created_on']
    search_fields 	= ['full_url']

admin.site.register(urldetails, urldetailsAdmin)
