from django.shortcuts import render, redirect, reverse
from django.contrib import messages

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
    if request.method == 'POST':
        form = ClassesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classes successfully added!')
            return redirect(reverse('add_classes'))
        else:
            messages.error(request, 'Failed to add classes. Please ensure the form is valid.')
    else:
        form = ClassesForm()
    form = ClassesForm()
    template = 'classes/add_classes.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
