#!/usr/bin/python
#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask.ext.wtf import Form
from wtforms import validators, fields


class WeixinConnectForm(Form):
    signature = fields.StringField(validators=[validators.Required()])
    timestamp = fields.StringField(validators=[validators.Required()])
    nonce = fields.StringField(validators=[validators.Required()])
    echostr = fields.StringField(validators=[validators.Required()])
