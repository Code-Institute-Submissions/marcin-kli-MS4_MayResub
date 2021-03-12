from django.shortcuts import render
from .models import Packages


def packages(request):
    """ A view to return the packages """

    packages = Packages.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)
