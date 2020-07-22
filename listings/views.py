from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Listing
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .choices import bedroom_choices, price_choices, state_choices

# Create your views here.


def listings(request):
    # listings = Listing.objects.all()
    # listings = Listing.objects.order_by('-list_date')
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)
    paginator = Paginator(listings, 2)
    page = request.GET.get("page")  # get page from url
    paged_listings = paginator.get_page(page)

    context = {"listings": paged_listings}
    # return HttpResponse("<h1>listings</h1>")
    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {"listing": listing}
    return render(request, "listings/listing.html", context)


def search(request):
    query_listing = Listing.objects.order_by("-list_date")

    # keywords like pool garage
    if "keywords" in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            query_listing = query_listing.filter(discription__icontains=keywords)

    # city
    #  iexact is casesensitive exact is no sensite
    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            query_listing = query_listing.filter(city__iexact=city)

    # state
    #  iexact is casesensitive exact is no sensite
    if "state" in request.GET:
        state = request.GET["state"]
        if state:
            query_listing = query_listing.filter(state__iexact=state)

    if "bedrooms" in request.GET:
        bedrooms = request.GET["bedrooms"]
        if bedrooms:
            query_listing = query_listing.filter(bedrooms__lte=bedrooms)

    if "price" in request.GET:
        price = request.GET["price"]
        if price:
            query_listing = query_listing.filter(price__lte=price)

    context = {
        "prices": price_choices,
        "bedrooms": bedroom_choices,
        "states": state_choices,
        "listings": query_listing,
        "values": request.GET,
    }
    return render(request, "listings/search.html", context)
