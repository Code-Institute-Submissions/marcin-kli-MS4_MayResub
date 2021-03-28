from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Packages
from .forms import PackagesForm


def packages(request):
    """ A view to return the packages """

    packages = Packages.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)


def package_detail(request, package_id):
    """ A view to show individual package details """

    package = get_object_or_404(Packages, pk=package_id)
    context = {
        'package': package,
    }

    return render(request, 'packages/package_detail.html', context)


@login_required
def add_package(request):
    """ Add a package to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Only administrator can see this site.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PackagesForm(request.POST, request.FILES)
        if form.is_valid():
            package = form.save()  # this is used to add package to the form.
            messages.success(request, 'Package successfully added!')
            return redirect(reverse('packages'))
        else:
            messages.error(
                request, 'Failed to add package. \
                    Please ensure the form is valid.')
    else:
        form = PackagesForm()

    form = PackagesForm()
    template = 'packages/add_package.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_package(request, package_id):
    """ Edit a package in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Only administrator can see this site.')
        return redirect(reverse('home'))

    package = get_object_or_404(Packages, pk=package_id)
    if request.method == 'POST':
        form = PackagesForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            messages.success(request, 'Package successfully updated!')
            return redirect(reverse('packages'))
        else:
            messages.error(
                request, 'Failed to update package. \
                    Please ensure the form is valid.')
    else:
        form = PackagesForm(instance=package)
        messages.info(request, f'You are editing {package.name}')

    template = 'packages/edit_package.html'
    context = {
        'form': form,
        'package': package,
    }

    return render(request, template, context)


@login_required
def delete_package(request, package_id):
    """ Delete a class from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Only administrator can see this site.')
        return redirect(reverse('home'))

    package = get_object_or_404(Packages, pk=package_id)
    package.delete()
    messages.success(request, 'Package deleted!')
    return redirect(reverse('packages'))
