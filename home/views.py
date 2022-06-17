from django.shortcuts import render

# Create your views here.


def homepage(request):
    """ A view to return the home page """

    return render(request, 'home/index.html')
