from django.shortcuts import render
from .models import Classes
from .forms import ClassesForm

# Create your views here.


def classes(request):
    """ A view to return the classes """

    classes = Classes.objects.all()

    context = {
        'classes': classes,
    }

    return render(request, 'classes/fitness_classes.html', context)


def add_classes(request):
    """ Add a classes to the store """
    form = ClassesForm()
    template = 'classes/add_classes.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
