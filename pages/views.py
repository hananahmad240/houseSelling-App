from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices
# Create your views here.


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:6]
    context = {"listings": listings, "bedrooms": bedroom_choices,
               "prices": price_choices, "states": state_choices}
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')  # ascending order
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {"realtors": realtors,
               "mvp_realtor": mvp_realtors}
    return render(request, 'pages/about.html', context)
