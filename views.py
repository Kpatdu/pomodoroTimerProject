from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Timer
from .forms import TimerForm

def front_page(request):
    return render(request, "index.html")
    # return render(request, "index_css.html")

def home_page(request):
    success = False
    added_timer = None
    if request.method == "POST":
        form = TimerForm(request.POST)
        if form.is_valid():
            new_timer = form.save()
            success = True
            added_timer = new_timer
            return render(request, "home_page.html", 
            {"form": form,
            "added_timer": added_timer,
            "success": success},
            )
    else:
        form = TimerForm()
    return render(
        request, "home_page.html",
        {"form": form,
        "added_timer": added_timer,
        "success": success},
    )
    # return render(request, "home_page_css.html")


def add_timer(request):
    success = False
    added_contact = None
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save()
            success = True
            added_contact = new_contact
            return render(
                request,
                "timerHome.html", # "add_contact_css.html",
                {"form": form,
                 "added_timer": added_timer,
                 "success": success},
            )
    else:
        form = ContactForm()
    return render(
        request,
        "timerHome.html", # "add_contact_css.html",
        {"form": form,
         "added_timer": added_timer,
         "success": success},
    )
