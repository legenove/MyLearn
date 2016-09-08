# encoding=utf-8
from django import forms
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.views import login as _login
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext, ugettext_lazy as _

class AuthenTicationLoginForm(AuthenticationForm):
    error_messages = {
        'invalid_password': _(u"密码错误，请输入正确的密码"),
        'invalid_username': _(u"账号不存在，请输入正确的账号"),
        'inactive': _(u"该用户没有激活"),
    }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_username'],
                    code='invalid_username',
                )
            elif hasattr(self.user_cache, 'is_wrong_password') and self.user_cache.is_wrong_password:
                raise forms.ValidationError(
                    self.error_messages['invalid_password'],
                    code='invalid_username',
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data