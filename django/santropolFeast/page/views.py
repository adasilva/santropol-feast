# coding: utf-8

from django.contrib.auth import logout
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    return render(request, 'pages/home.html')


def custom_login(request):
    '''Custom login function.

    Redirects user to homepage if already logged in.'''
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse_lazy("page:home"))
    else:
        return login(request)
