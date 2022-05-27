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
        'stripe_public_key': 'pk_test_51L3xrkKq5PI8YlsFBLZo8AjYi2hgUWQz9FvWrdWntRDHBTFGOgNinu42MlMt6qYTcwfNQTsDbkMY4yEwpJJV2z7J00b1fEdw74',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
