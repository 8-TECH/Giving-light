from django.shortcuts import render
from .models import Program, Event


def giving_light(request):
    program = Program.objects.all()
    event = Event.objects.all()

    context = {'program': program, 'event': event}
    return render(request, 'giving_light/index.html', context)


