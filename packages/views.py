from django.shortcuts import render, get_object_or_404
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


def add_packages(request):
    """ Add a package to the store """
    form = PackagesForm()
    #template = 'packages/add_packages.html'
    context = {
        'form': form,
    }
    print(form)
    #print(template)
    print(context)

    return render(request, 'packages/add_packages.html', context)
