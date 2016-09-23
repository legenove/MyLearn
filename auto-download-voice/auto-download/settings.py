# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from os import path, environ as _env
from urlparse import urlparse
from celery.schedules import crontab


# 线上环境用Calypso 配置，所以做一个environ 的代理
class CalypsoEnv(object):
    def get(self, key, default=None):
        value = _env.get(key)

        # 相当于重定向
        alias = _env.get(value)
        if alias is not None:
            return alias

        if not value and default:
            return default
        return value

environ = CalypsoEnv()


class EnvConfigType(type):

    def __getattribute__(cls, key):
        value = object.__getattribute__(cls, key)
        env = environ.get(key)

        if env is not None:
            value = type(value)(env)
        return value


class Config(object):

    __metaclass__ = EnvConfigType

    DEBUG = True
    TESTING = False

    ONLINE_LAST_MINUTES = 5

    SECRET_KEY = '53a01e6bd34caef997eed24f5ee9d3e0'
    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        environ.get('PG_USER', 'zhifubao'),
        environ.get('PG_PASSWORD', 'zzzz'),
        environ.get('POSTGRES_PORT_5432_TCP_ADDR', 'localhost'),
        environ.get('POSTGRES_PORT_5432_TCP_PORT', '5432'),
        environ.get('PG_DATABASE', 'zhifubao'))
    SQLALCHEMY_SLAVE_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        environ.get('PG_USER', 'zhifubao'),
        environ.get('PG_PASSWORD', 'zzzz'),
        environ.get('SLAVE_POSTGRES_PORT_5432_TCP_ADDR', 'localhost'),
        environ.get('SLAVE_POSTGRES_PORT_5432_TCP_PORT', '5432'),
        environ.get('PG_DATABASE', 'zhifubao'))
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_MAX_OVERFLOW = 10
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_BINDS = {
        'master': SQLALCHEMY_DATABASE_URI,
        'slave': SQLALCHEMY_SLAVE_DATABASE_URI
    }

    COEFFICIENT = float(environ.get('COEFFICIENT', 0.72))

    RATE_LIMIT_ON = environ.get('RATE_LIMIT_ON', False)
    RATE_LIMIT = int(environ.get('RATE_LIMIT', 500))
    RATE_LIMIT_PERIOD = int(environ.get('RATE_LIMIT_PERIOD', 60 * 10))

    REDIS_MASTER_HOST = environ.get('REDIS_PORT_6379_TCP_ADDR', 'localhost')
    REDIS_MASTER_PORT = environ.get('REDIS_PORT_6379_TCP_PORT', '6379')
    REDIS_DATABASE = environ.get('REDIS_DATABASE', '4')
    REDIS_MASTER_URL = 'redis://%s:%s/%s' % (REDIS_MASTER_HOST,
                                             REDIS_MASTER_PORT,
                                             REDIS_DATABASE)
    REDIS_MASTER_SERVER = {
        'host': REDIS_MASTER_HOST,
        'port': REDIS_MASTER_PORT,
        'db': REDIS_DATABASE,
    }

    REDIS_SLAVE_HOST = environ.get('REDIS_SLAVE_PORT_6379_TCP_ADDR',
                                   'localhost')
    REDIS_SLAVE_PORT = environ.get('REDIS_SLAVE_PORT_6379_TCP_PORT', '6379')
    REDIS_SLAVE_URL = 'redis://%s:%s/%s' % (REDIS_SLAVE_HOST, REDIS_SLAVE_PORT,
                                            REDIS_DATABASE)
    REDIS_SLAVES_SERVER = [
        {
            'host': REDIS_SLAVE_HOST,
            'port': REDIS_SLAVE_PORT
        },
    ]

    MEMCACHED_URLS = environ.get('MEMCACHED_URLS', 'localhost:11211')

    # celery settings
    CELERY_BROKER_URL = 'amqp://{username}:{password}@{host}:{port}/zhifubao'.format(
        username=environ.get('CELERY_RABBITMQ_PORT_5672_USERNAME', 'zhifubao'),
        password=environ.get('CELERY_RABBITMQ_PORT_5672_PASSWORD', 'zhifubao'),
        host=environ.get('CELERY_RABBITMQ_PORT_5672_TCP_ADDR', 'localhost'),
        port=environ.get('CELERY_RABBITMQ_PORT_5672_TCP_PORT', '5672'))
    CELERY_RESULT_BACKEND = 'rpc://{username}:{password}@{host}:{port}/zhifubao'.format(
        username=environ.get('CELERY_RABBITMQ_PORT_5672_USERNAME', 'zhifubao'),
        password=environ.get('CELERY_RABBITMQ_PORT_5672_PASSWORD', 'zhifubao'),
        host=environ.get('CELERY_RABBITMQ_PORT_5672_TCP_ADDR', 'localhost'),
        port=environ.get('CELERY_RABBITMQ_PORT_5672_TCP_PORT', '5672'))
    CELERY_ALWAYS_EAGER = False
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERY_TASK_RESULT_EXPIRES = 30

    VISIT_AMOUNT = int(environ.get('VISIT_AMOUNT', 2))

    STATIC_FOLDER = 'static'

    MAX_FOLLOWING_COUNT = int(environ.get('MAX_FOLLOWING_COUNT', 2000))
    FDB_IOS_SERVER_HOST = environ.get(
        'FDB_IOS_SERVER_HOST', 'http://fdb_coin_ios:8889')
    FDB_ANDROID_SERVER_HOST = environ.get(
        'FDB_ANDROID_SERVER_HOST', 'http://fdb_coin_android:8889')
    REVOKE_DELAY_SECONDS = int(environ.get('REVOKE_DELAY_SECONDS', 60))
    RECOURSE_ROLE_IDS = environ.get('RECOURSE_ROLE_IDS', '6')

    APP_TRANSPORT = environ.get('APP_TRANSPORT', 'http')
    APP_DOMAIN = environ.get('APP_DOMAIN', 'http://zhitest.zaih.com')
    DOMAIN = '%s://%s' % (APP_TRANSPORT, urlparse(APP_DOMAIN).netloc)
    PAY_DOMAIN = environ.get('PAY_DOMAIN', '%s/py' % DOMAIN)

    ES_HOST = environ.get('ES_HOST', b'54.222.236.124')
    ES_PORT = environ.get('ES_PORT', b'9200')

    ES_SERVER_HOST = environ.get('ES_SERVER_HOST', "http://10.0.80.13:8910")

    REVIEW_SERVER_HOST = environ.get('REVIEW_SERVER_HOST', b'54.223.60.47')
    REVIEW_SERVER_PORT = environ.get('REVIEW_SERVER_PORT', b'8008')
    REVIEW_SERVER_URL = "http://%s:%s/api/v1/blacklist" % (REVIEW_SERVER_HOST,
                                                           REVIEW_SERVER_PORT)
    REVIEW_SERVER_SYNC_URL = "http://%s:%s/api/v1/sync" % (REVIEW_SERVER_HOST,
                                                           REVIEW_SERVER_PORT)
    REVIEW_SERVER_USERNAME = environ.get('REVIEW_SERVER_USERNAME', b'')
    REVIEW_SERVER_PASSWORD = environ.get('REVIEW_SERVER_PASSWORD', b'')

    # SENTRY DNS
    SENTRY_DSN = ('http://1719faec88124a8dbaf19f795c7347a7:'
                  '46988a33167d47b380e85972215c8ad4@sentry.iguokr.com:5000/12')

    # 微信 公众账号信息
    WEIXINMP_APPID = environ.get('WEIXINMP_APPID', 'wxba29bd8df2c92c95')
    WEIXINMP_APP_SECRET = environ.get('WEIXINMP_APP_SECRET',
                                      '28f70d8e1cd9823b178afeedffb5c9b9')
    WEIXINMP_TOKEN = environ.get('WEIXINMP_TOKEN',
                                 'OHBlcWfhMUHczZDMxNWJjMDRkZTJiOGE')
    WEIXINMP_ENCODINGAESKEY = environ.get(
        'WEIXINMP_ENCODINGAESKEY',
        '9On5TSh45id6e9RNakfPkbaElU6nZlA2ZNFe6K9fuof')

    # 微信appid 移动应用
    WEIXINAPP_APPID = environ.get('WEIXINAPP_APPID', 'wx8d596a03f69aaa8f')
    WEIXINAPP_APPSECRET = environ.get(
        'WEIXINAPP_APPSECRET', 'd68bc46520369c70f407fea408ae27ae')

    # 商户号类型 guokr zaihang
    WXPAY_MCH_TYPE = environ.get('WXPAY_MCH_TYPE', 'guokr')

    # 微信支付信息
    # 微信商户号由微信统一分配的 10 位正整数 (120XXXXXXX)号
    OLD_WXPAY_MCH_ID = environ.get('OLD_WXPAY_MCH_ID', '1285567001')
    OLD_WXPAY_PARTNER_KEY = environ.get('OLD_WXPAY_PARTNER_KEY',
                                        'ZZJVhwd7NVK8ttfYkeTDVjdoucAWnBjr')
    if WXPAY_MCH_TYPE == 'guokr':
        WXPAY_MCH_ID = OLD_WXPAY_MCH_ID
        WXPAY_PARTNER_KEY = OLD_WXPAY_PARTNER_KEY
    else:
        WXPAY_MCH_ID = environ.get('WXPAY_MCH_ID', '1285567001')
        WXPAY_PARTNER_KEY = environ.get('WXPAY_PARTNER_KEY',
                                        'ZZJVhwd7NVK8ttfYkeTDVjdoucAWnBjr')
    WXAPPPAY_MCH_ID = environ.get('WXPAY_MCH_ID', '1350029301')
    # 微信支付商户 Key
    WXAPPPAY_PARTNER_KEY = environ.get('WXPAY_PARTNER_KEY',
                                       '12345678901234567890123456789012')

    OLD_WXPAY_MCH_CERT = path.normpath(path.join(
        path.dirname(__file__), 'wxpem/apiclient_cert.pem'))
    OLD_WXPAY_MCH_KEY = path.normpath(path.join(
        path.dirname(__file__), 'wxpem/apiclient_key.pem'))
    if environ.get('DEBUG'):
        WXPAY_MCH_CERT = path.normpath(path.join(
            path.dirname(__file__), 'wxpem/dev_apiclient_cert.pem'))
        WXPAY_MCH_KEY = path.normpath(path.join(
            path.dirname(__file__), 'wxpem/dev_apiclient_key.pem'))
    else:
        if WXPAY_MCH_TYPE == 'guokr':
            WXPAY_MCH_CERT = OLD_WXPAY_MCH_CERT
            WXPAY_MCH_KEY = OLD_WXPAY_MCH_KEY
        else:
            WXPAY_MCH_CERT = path.normpath(path.join(
                path.dirname(__file__), 'wxpem/new_apiclient_cert.pem'))
            WXPAY_MCH_KEY = path.normpath(path.join(
                path.dirname(__file__), 'wxpem/new_apiclient_key.pem'))

    # 签名方式 不需修改
    WXPAY_SIGN_TYPE = 'MD5'
    # 字符编码格式 目前支持 GBK 或 utf-8
    WXPAY_INPUT_CHARSET = 'UTF-8'
    # 交易过程中服务器通知的页面 要用
    # http://格式的完整路径，不允许加?id=123这类自定义参数
    WXPAY_NOTIFY_URL = '%s/weixin_pay/notify' % PAY_DOMAIN
    # 微信获取用户信息接口
    WX_USER_INFO_URL = 'https://api.weixin.qq.com/cgi-bin/user/info'

    QINIU_ACCESS_TOKEN = 'x7cu88uRBgDKIWHzGHvK-OgKznQpY4ZfhbObIrt2'
    QINIU_SECRET_TOKEN = 'btfJJE_RuWdlX9C9Ww3Y3a2ayVBwDF5lKKsRLs7c'
    QINIU_UPLOAD_URL = 'http://up.qiniu.com/'
    QINIU_DOMAIN = environ.get('QINIU_DOMAIN', 'media.zaih.com')
    QINIU_DOMAINS = [QINIU_DOMAIN, 'hangjia.qiniudn.com']
    QINIU_HOST = "http://%s" % QINIU_DOMAIN
    QINIU_NOTIFY_URL = '%s/py/qiniu/pfop/notify' % DOMAIN
    QINIU_PUBLIC_BUCKET = 'hangjia'
    # 私有空间域名
    QINIU_PRIVITE_DOMAIN = environ.get('QINIU_PRIVITE_DOMAIN', 'audio.zaih.com')
    QINIU_PRIVITE_HOST = "http://%s" % QINIU_PRIVITE_DOMAIN
    QINIU_PRIVITE_BUCKET = 'fenda-media'
    QINIU_PIPELINE = environ.get('QINIU_PIPELINE', 'zaih_media')
    QINIU_FILTER_NOTIFY_URL = '%s/py/qiniu/pfop/filter_notify' % DOMAIN
    QINIU_RECOGNITION_NOTIFY_URL = '%s/py/qiniu/pfop/recognition_notify' % DOMAIN
    #百度语音识别
    BAIDU_ASR_TOKEN = environ.get('BAIDU_ASR_TOKEN',
                                  '24.ccb5fc7c741a8abc1558b2fa6e52ccee.2592000.1470290039.282335-2214261')
    BAIDU_ASR_GRANT_TYPE = environ.get('BAIDU_ASR_GRANT_TYPE', 'client_credentials')
    BAIDU_ASR_CLIENT_ID = environ.get('BAIDU_ASR_CLIENT_ID', '5ztZwWTrRWZSk5bhSKVvPfPs')
    BAIDU_ASR_CLIENT_SECRET = environ.get('BAIDU_ASR_CLIENT_SECRET', 'ErR3dIoQkfZoCoc9HGQu3HU6QDMlNtjX')
    #科大讯飞语音API
    XUNFEI_WEBAPI_TOKEN = environ.get('XUNFEI_WEBAPI_TOKEN', 'dfc4de75')
    XUNFEI_WEBAPI_HOST = environ.get('XUNFEI_WEBAPI_HOST', 'openapi.openspeech.cn')
    XUNFEI_WEBAPI_RECOGNITION_PATH = environ.get('XUNFEI_WEBAPI_RECOGNITION_PATH', '/webapi/iat.do')
    XUNFEI_WEBAPI_APP_ID = environ.get('XUNFEI_WEBAPI_APP_ID', '57611ed9')
    XUNFEI_WEBAPI_RECOGNITION_NOTIFY_URL = '%s/py/xunfei/webapi/recognition_notify' % DOMAIN

    # 国新办域名 地址
    GXB_SERVER_HOST = environ.get('GXB_SERVER_HOST', 'http://localhost:3721')
    GXB_SERVER_URL = '%s/gxb.service/SuspiciousAv/uploadAvInfo' % GXB_SERVER_HOST

    # jpush config
    JPUSH_APP_KEY = environ.get('JPUSH_APP_KEY', '')
    JPUSH_MASTER_SECRET = environ.get('JPUSH_MASTER_SECRET', '')

    # 通知模板
    # 提问后通知
    TEMPLATE_ID_ASK = environ.get(
        'TEMPLATE_ID_ASK', 'iMHbmQMrItfm994g0f2Qv6EPk-N5VaX3si8KAUsYY9A')
    # 回答后通知提问者
    TEMPLATE_ID_ANSWER_TO_ASKER = environ.get(
        'TEMPLATE_ID_ANSWER_TO_ASKER', '2AxVi9lj8Rms6b3kOFj0tvqQCkgTCmf-2IgSJ6JO4uA')
    # 结算提醒
    TEMPLATE_ID_SETTLE = environ.get(
        'TEMPLATE_ID_SETTLE', '9wEjbJDV45O_ECjX2SShanslz59tyYGKiq6AtTDA8_s')
    # 超时未回答退款通知
    TEMPLATE_ID_TIMEOUT = environ.get(
        'TEMPLATE_ID_REFUND', 'VOM9wJnh3delJEP95kDg_9iQZklwcL7GohD_6FrmAaA')
    # 未回答问题提醒
    TEMPLATE_ID_UNANSWERED = environ.get(
        'TEMPLATE_ID_UNANSWERED', 'x_fQaDZZe6sdxXZUGVc7dd1XQAC1PkzwfmmXZbGG8Kc')
    TEMPLATE_ID_ANSWER_RESPONDENT = environ.get(
        'TEMPLATE_ID_ANSWER_RESPONDENT', '')
    # 系统出错提醒模板
    TEMPLATE_ID_ERROR = environ.get(
        'TEMPLATE_ID_ERROR', '_Lk48qylJa8iWnMOaEsv6UluQ_HMH3PJ2s5l9IJOxcg')
    TEMPLATE_ID_DONATION = environ.get(
        'TEMPLATE_ID_DONATION', 'yS2v49PAjaUi_4M2jiSP2721WexN7d0elceOAWi3a5U')
    TEMPLATE_ID_REANSWER_TO_ASKER = environ.get(
        'TEMPLATE_ID_REANSWER_TO_ASKER', 'jrRVUL0JuLzTXj8Dgwqikum20tTWomlCm1U-3HtvDHk')
    TEMPLATE_ID_REVIEW_DRAFT = environ.get(
        'TEMPLATE_ID_REVIEW_DRAFT', 'zPq9zLvPtSn5lXk4LkhwCFuntmsKFbhwHgcX85wj15c')
    # 答主申请入驻商户反馈模版
    TEMPLATE_ID_TENANT_RESPOND = environ.get(
        'TEMPLATE_ID_TENANT_RESPOND', '01pqtQs_bq1emF48qvVDX28lhPmoWJkGlqA5J45zzL4')
    TEMPLATE_ID_COMMONWEAL_DONE = environ.get(
        'TEMPLATE_ID_COMMONWEAL_DONE', 'wMX-MzCG37YmLCJrgJMKxq8TtDjz3urYZa-hu89rm9Q')
    TEMPLATE_ID_BETA_INVITATION = environ.get(
        'TEMPLATE_ID_BETA_INVITATION', 'gLkH-VzkpjYKHO6XbuiTaI-ee3j7Hl2pXzLCqkLqMqg')
    # 错误通知接受者openid
    ADMIN_OPENID = environ.get('ADMIN_OPENID', 'o7l9Gs_IyQhSH1esMb50zxGnhdwc')

    # board应用地址
    BOARD_SERVER_HOST = environ.get('BOARD_SERVER_HOST', 'http://0.0.0.0:8889')
    BOARD_BACKEND_API = '{host}/backend'.format(host=BOARD_SERVER_HOST)
    # 悬赏server
    WANTED_SERVER_HOST = environ.get('WANTED_PORT_8890_HTTP_PROTO', 'http://localhost:8888')
    WANTED_BACKEND_API = '{host}/backend'.format(host=WANTED_SERVER_HOST)
    # feed server
    FEED_SERVER_HOST = environ.get('FEED_PORT_8891_HTTP_PROTO', 'http://localhost:8015')
    FEED_BACKEND_API = '{host}/backend'.format(host=FEED_SERVER_HOST)
    # auth server
    AUTH_SERVER_HOST = environ.get('OAUTH_PORT_8897_HTTP_PROTO', 'http://localhost:8897')
    AUTH_BACKEND_API = '{host}/backend'.format(host=AUTH_SERVER_HOST)
    AUTH_API = '{host}/backend/oauth/tokeninfo'.format(host=AUTH_SERVER_HOST)
    # tutor server 只用来检查行家信息
    TUTOR_SERVER_HOST = environ.get('TUTOR_PORT_8888_HTTP_PROTO', 'https://apis.zaih.com')
    TUTOR_BACKEND_API = '{host}/backend'.format(host=TUTOR_SERVER_HOST)

    BACKEND_APIS = {
        'auth': AUTH_BACKEND_API,
        'feed': FEED_BACKEND_API,
        'board': BOARD_BACKEND_API,
        'tutor': TUTOR_BACKEND_API,
        'wanted': WANTED_BACKEND_API,
    }

    # 创蓝短信
    CLSMS_API_URL = environ.get(
        'CLSMA_API_URL', 'http://222.73.117.156:80/msg/HttpBatchSendSM')
    CLSMS_ACCOUNT = environ.get('CLSMS_ACCOUNT', '')
    CLSMS_PASSWORD = environ.get('CLSMS_PASSWORD', '')
    CLSMS_ACCOUNT_MARKETING = environ.get('CLSMS_ACCOUNT_MARKETING', '')
    CLSMS_PASSWORD_MARKETING = environ.get('CLSMS_PASSWORD_MARKETING', '')

    # 苹果审核测试账号
    APPLE_TEST_ACCOUNT = environ.get('APPLE_TEST_ACCOUNT', '')

    FIRST_ACCOUNT_ID = 587467193
    APP_CLIENT_ID = 'zhifubao'
    APP_CLIENT_SECRET = 'YhGF19NB8fgg700AVEWolGuH008N'

    # 是否审核全部问题
    IS_REVIEW_ALL = True
    # 普通用户问题自动过审时间 分
    NORMAL_QUESTION_REVIEW_DURATION = int(environ.get('NORMAL_QUESTION_REVIEW_DURATION', 8 * 60))
    # 普通用户答案自动过审时间 分
    NORMAL_ANSWER_REVIEW_DURATION = int(environ.get('NORMAL_ANSWER_REVIEW_DURATION', 8 * 60))
    # 白名单用户问题自动过审时间 分
    WHITELIST_QUESTION_REVIEW_DURATION = int(environ.get('WHITELIST_QUESTION_REVIEW_DURATION', 8 * 60))
    # 白名单用户答案自动过审时间 分
    WHITELIST_ANSWER_REVIEW_DURATION = int(environ.get('WHITELIST_ANSWER_REVIEW_DURATION', 8 * 60))

    # 问题可添加的图片数
    MAX_QUESTION_IMAGE = 3
    # 可以接受图片问题的标签ID
    _RECEIVED_IMAGES_TAG_IDS = environ.get('RECEIVED_IMAGES_TAG_IDS', '10,21')
    RECEIVED_IMAGES_TAG_IDS = map(int, _RECEIVED_IMAGES_TAG_IDS.split(','))

    # 用户修改资料周期(秒) 30天
    ACCOUNT_DRAFT_DURATION = int(environ.get(
        'ACCOUNT_DRAFT_DURATION', 3600 * 24 * 30))

    # 审核不通过图片默认的图片地址
    DEFAULT_PENDING_IMAGE = 'http://media.zaih.com/Fpl8biDIQVYBnVI3jbN_HWa5y2D0'

    CELERYBEAT_SCHEDULE = {
        'scheduled_close_questions': {
            'task': 'zzhifubao.tasks.scheduled_close_questions',
            'schedule': crontab(minute='*/30'),
        },
        #  'scheduled_remind_answer_question': {
            #  'task': 'zzhifubao.tasks.scheduled_remind_answer_question',
            #  'schedule': crontab(minute='30', hour='21'),
        #  },
        'scheduled_settle': {
            'task': 'zzhifubao.tasks.scheduled_settle',
            'schedule': crontab(minute='45', hour='21,22,23'),
        },
        'scheduled_query_settle': {
            'task': 'zzhifubao.tasks.scheduled_query_settle',
            'schedule': crontab(minute='30', hour='22,23,0'),
        },
        'scheduled_refund_query': {
            'task': 'zzhifubao.tasks.scheduled_refund_query',
            'schedule': crontab(minute='45', hour='*/1'),
        },
        'scheduled_update_baiduasr_token': {
            'task': 'zzhifubao.tasks.scheduled_update_baiduasr_token',
            'schedule': crontab(minute='10', hour='1', day_of_month='1,16'),
        },
        #  'scheduled_update_questions_score': {
            #  'task': 'zzhifubao.tasks.scheduled_update_questions_score',
            #  'schedule': crontab(minute='*/30'),
        #  },
        # 'scheduled_update_tmprank': {
        #     'task': 'zzhifubao.tasks.scheduled_update_tmprank',
        #     'schedule': crontab(minute='*/15'),
        # },
        # 'scheduled_refresh_income_rank': {
        #     'task': 'zzhifubao.tasks.scheduled_refresh_income_rank',
        #     'schedule': crontab(minute='23', hour='5'),
        # },
        #  'scheduled_update_promote_plan_status': {
            #  'task': 'zzhifubao.tasks.scheduled_update_promote_plan_status',
            #  'schedule': crontab(minute='*/60'),
        #  },
        'scheduled_update_account_index': {
            'task': 'zzhifubao.tasks.scheduled_update_account_index',
            'schedule': crontab(minute='*/60'),
        },
        # 'scheduled_remind_answer_donation': {
        #     'task': 'zzhifubao.tasks.scheduled_remind_answer_donation',
        #     'schedule': crontab(minute='0', hour='21'),
        # },
        #  'scheduled_refresh_draft_answers': {
            #  'task': 'zzhifubao.tasks.scheduled_refresh_draft_answers',
            #  'schedule': crontab(minute='*/30'),
        #  },
        #  'scheduled_update_library_valuable_questions': {
            #  'task': 'zzhifubao.tasks.scheduled_update_library_valuable_questions',
            #  'schedule': crontab(minute='*/60'),
        #  },
        #  'scheduled_question_top_up': {
            #  'task': 'zzhifubao.tasks.scheduled_question_top_up',
            #  'schedule': crontab(minute='*/30'),
        #  },
        #  'scheduled_calculate_order_score': {
            #  'task': 'zzhifubao.tasks.scheduled_calculate_order_score',
            #  'schedule': crontab(minute='0', hour='3'),
        #  },
        #  'scheduled_order_score_random_factor': {
            #  'task': 'zzhifubao.tasks.scheduled_order_score_random_factor',
            #  'schedule': crontab(minute='0', hour='4'),
        #  },
    }
