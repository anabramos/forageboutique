from django.shortcuts import render


def profile(request):
    """ Display the user's account profile. """

    template = 'accounts/profile.html'
    context = {}

    return render(request, template, context)