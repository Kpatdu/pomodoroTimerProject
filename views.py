from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Timer
from .forms import TimerForm

def front_page(request):
    return render(request, "index.html")
    # return render(request, "index_css.html")