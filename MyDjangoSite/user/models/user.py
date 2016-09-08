# encoding=utf-8

import base64

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class MyUserManager(UserManager):
    def get_by_natural_key(self, username):
        try:
            _obj = self.get(**{self.model.USERNAME_FIELD: username})
            return _obj
        except self.model.DoesNotExist:
            return None

    def get_by_email_key(self, username):
        try:
            _obj = self.get(**{self.model.EMAIL_FIELD: username})
            return _obj
        except self.model.DoesNotExist:
            return None

    def get_by_mobile_key(self, username):
        try:
            _obj = self.get(**{self.model.MOBIL_FIELD: username})
            return _obj
        except self.model.DoesNotExist:
            return None

class Account(AbstractUser):
    SOURCE = [
        (0, u"自有注册"),
        (1, u'微信'),
        (2, u'微博'),
        (3, u'QQ'),
        (4, u"手机"),
        (5, u"友盟微信"),
    ]
    SOURCE_WEIXIN = 1
    SOURCE_WEIBO = 2
    SOURCE_QQ = 3
    SOURCE_PHONE = 4
    SOURCE_YOUMENG_WEIXIN = 5

    MESSAGE_HAS_READ = [
        (1, u'has'),
        (0, u'nothing')
    ]
    IS_PREMIUM = 1

    PLATFORM = [
        (0, u'Android'),
        (1, u'IOS'),
        (2, u'Web'),
        (3, u'其他')
    ]

    openid = models.CharField(verbose_name=u"openid", max_length=64, blank=True, db_index=True)
    desc = models.CharField(verbose_name=u"自我描述", blank=True, max_length=20)
    phone = models.CharField(verbose_name=u"手机号", max_length=15, null=True, blank=True, db_index=True, unique=True)
    gender = models.IntegerField(verbose_name=u"性别", default=0, choices=((1, u"男"), (2, u"女")), null=True, blank=True)
    image = models.CharField(verbose_name=u"用户图片(大图)", max_length=255, null=True, blank=True, default='')
    image_small = models.CharField(verbose_name=u"用户图片(小图)", max_length=255, null=True, blank=True, default='')

    platform = models.IntegerField(verbose_name=u'平台', choices=PLATFORM, default=2)
    cid = models.CharField(verbose_name=u"client_id(push)", max_length=128, null=True, blank=True, default='')
    osver = models.CharField(verbose_name=u'设备系统版本号', max_length=10, null=True, blank=True, default='')

    longitude = models.FloatField(verbose_name=u"精度", default=0)
    latitude = models.FloatField(verbose_name=u"精度", default=0)
    area = models.CharField(verbose_name=u"地域", default="", max_length=20, null=True, blank=True)

    province = models.CharField(verbose_name=u"省份", max_length=10, null=True, blank=True, default='')
    city = models.CharField(verbose_name=u"城市", max_length=10, null=True, blank=True, default='')
    country = models.CharField(verbose_name=u"国家", max_length=10, null=True, blank=True, default='')

    ip = models.CharField(verbose_name=u"注册ip", blank=True, max_length=20, default='')

    # level = models.ForeignKey(Level, verbose_name=u'用户等级')
    level_desc = models.CharField(max_length=10, blank=True, verbose_name=u'用户等级描述')
    last_experience = models.CharField(max_length=10, blank=True, verbose_name=u'下一级升级经验')

    source = models.IntegerField(verbose_name=u'用户来源', choices=SOURCE, default=0)

    has_message_unread = models.IntegerField(verbose_name=u'是否有未读消息', choices=MESSAGE_HAS_READ, default=0)

    is_block = models.IntegerField(verbose_name='是否屏蔽', default=0)
    is_premium = models.IntegerField(verbose_name='是否付费用户', default=0)

    objects = MyUserManager()

    EMAIL_FIELD = u'email'
    MOBIL_FIELD = u'phone'

    class Meta:
        app_label = "user"
        verbose_name = u"user account"
        verbose_name_plural = verbose_name

    @property
    def uid(self):
        try:
            return 'U{0}'.format(base64.b64encode(str(long(self.id) << 2)))
        except ValueError:
            return self.id

    @classmethod
    def decode_uid(cls, uid):
        if isinstance(uid, unicode):
            uid = uid.encode('utf-8')

        if isinstance(uid, (int, long)) or str(uid).isdigit():
            return long(uid)
        else:
            try:
                return long(base64.b64decode(uid[1:])) >> 2
            except (TypeError, ValueError):
                return 0L
