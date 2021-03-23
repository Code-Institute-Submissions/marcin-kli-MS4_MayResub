from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def add_class(request):
    """ Add a classes to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Only administrator can see this site.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ClassesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classes successfully added!')
            return redirect(reverse('classes'))
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


@login_required
def edit_class(request, classes_id):
    """ Edit a class in the site """
    if not request.user.is_superuser:
        messages.error(request, 'Only administrator can see this site.')
        return redirect(reverse('home'))

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


@login_required
def delete_class(request, classes_id):
    """ Delete a class from the site """
    if not request.user.is_superuser:
        messages.error(request, 'Only administrator can see this site.')
        return redirect(reverse('home'))

    classes = get_object_or_404(Classes, pk=classes_id)
    classes.delete()
    messages.success(request, 'Class deleted!')
    return redirect(reverse('classes'))
