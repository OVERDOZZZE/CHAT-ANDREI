from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm

def frontpage(request):
    return render(request, 'core/frontpage.html')
