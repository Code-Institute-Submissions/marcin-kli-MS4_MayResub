from django.shortcuts import render
from .models import Classes

# Create your views here.


def classes(request):
    """ A view to return the classes """

    classes = Classes.objects.all()

    context = {
        'classes': classes,
    }

    return render(request, 'classes/fitness_classes.html', context)
