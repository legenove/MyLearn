# encoding=utf-8
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.views import login as _login

from ..models import Account
from ..forms import AuthenTicationLoginForm

def login(request):
    return _login(request, 'login.html', authentication_form=AuthenTicationLoginForm)

