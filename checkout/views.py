from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """A view to return the checkout page with the bag contents of the session - if there are any"""
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "You have no items on your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
