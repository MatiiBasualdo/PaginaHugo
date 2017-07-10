from django.shortcuts import render, render_to_response, redirect
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.shortcuts import render, get_object_or_404

# Create your views here.

def inicio(request):
    return render(request, 'index.html')
