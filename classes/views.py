from django.shortcuts import render, redirect, reverse, get_object_or_404
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


def add_class(request):
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
    template = 'classes/add_class.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_class(request, classes_id):
    """ Edit a class in the store """
    classes = get_object_or_404(Classes, pk=classes_id)
    if request.method == 'POST':
        form = ClassesForm(request.POST, request.FILES, instance=classes)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classes successfully updated!')
            return redirect(reverse('classes'))
        else:
            messages.error(request, 'Failed to update classes. Please ensure the form is valid.')
    else:
        form = ClassesForm(instance=classes)
        messages.info(request, f'You are editing {classes.name}')

    template = 'classes/edit_class.html'
    context = {
        'form': form,
        'classes': classes,
    }

    return render(request, template, context)
