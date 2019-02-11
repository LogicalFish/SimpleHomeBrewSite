from django.contrib import admin

# Register your models here.
from .models import Homebrew
from .models import Job

class HomebrewAdmin(admin.ModelAdmin):

    fields = ['jobs','title','summary','user']

    list_filter = ['jobs','user']

    list_display = ['title','jobs','user']


admin.site.register(Homebrew,HomebrewAdmin)
admin.site.register(Job)