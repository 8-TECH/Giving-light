from django.contrib import admin

# Register your models here.
from .models import Program, Event

admin.site.register(Program)
admin.site.register(Event)