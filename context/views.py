from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Context

# Create your views here.
def contact(request):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing = request.POST["listing"]
        user_id = request.POST["user_id"]
        realtor_email = request.POST["realtor_email"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        contact = Context(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
        )

        # check if user has already inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Context.objects.all().filter(
                listing_id=listing_id, user_id=user_id
            )
            if has_contacted:
                messages.error(request, "You already made an inquiry!")
                return redirect("/listings/" + listing_id)

            else:
                contact.save()
                # send_mail(
                #     "propery Listing Inquiry",
                #     "There has been an inquiry of" + ". Sign inti admin panel",
                #     "nayyabhanan2010@gmail.com",
                #     [realtor_email, "ahmadhanan344@gmail.com"],
                #     fail_silently=False,
                # )
                messages.success(
                    request,
                    "You request has been submitted , arealtor will et back you soon",
                )
                return redirect("/listings/" + listing_id)

        else:
            contact.save()
            # send_mail(
            #     "propery Listing Inquiry",
            #     "There has been an inquiry of" + ". Sign inti admin panel",
            #     "nayyabhanan2010@gmail.com",
            #     [realtor_email, "ahmadhanan344@gmail.com"],
            #     fail_silently=False,
            # )
            messages.success(
                request,
                "You request has been submitted , arealtor will et back you soon",
            )
            return redirect("/listings/" + listing_id)

