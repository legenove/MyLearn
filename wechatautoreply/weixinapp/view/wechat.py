# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
import json
from time import time

from flask import Blueprint, url_for, views

from common import WeChatReply

instance_wechat = Blueprint('wechat_public', __name__)


instance_wechat.add_url_rule('/', view_func=WeChatReply.as_view(
    b'wxask'), defaults={'id': 1}, methods=['GET', 'POST'])
instance_wechat.add_url_rule('/<int:id>/', view_func=WeChatReply.as_view(
    b'wxcommon'), methods=['GET', 'POST'])
