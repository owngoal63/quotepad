import stripe

from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render

from django.contrib.auth.models import User, Group

stripe.api_key = settings.STRIPE_SECRET_KEY

class HomePageView(TemplateView):
    template_name = 'payments/stripe_checkout.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request): 
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=1500,
            currency='gbp',
            description='Quotepad Subscription Charge',
            source=request.POST['stripeToken']
        )
        # Add the user who has paid the sub to the group 'Subscribed'
        subscribed_group = Group.objects.get(name = 'Subscribed')
        request.user.groups.add(subscribed_group)
        request.session['User_subscribed'] = True
        return render(request, 'payments/charge.html')