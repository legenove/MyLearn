# -*- coding: utf-8 -*-
from array import array

from igt_push import *
from igetui.template import *
from igetui.template.igt_base_template import *
from igetui.template.igt_transmission_template import *
from igetui.template.igt_link_template import *
from igetui.template.igt_notification_template import *
from igetui.template.igt_notypopload_template import *
from igetui.template.igt_apn_template import *
from igetui.igt_message import *
from igetui.igt_target import *
from igetui.template import *
from BatchImpl import *
from payload.APNPayload import *

os.environ['needDetails'] = 'true'

HOST = 'http://sdk.open.api.igexin.com/apiex.htm';

# TODO:需要更新app各项信息

APPKEY = "gj9paw20qe80Vz2E8cj6N6"
APPID = "t1w7xd5kD970blQRKZBlU"
MASTERSECRET = "xA9YzLaBPL8OUHd4tJpLh9"
Alias = '请输入别名'
DEVICETOKEN = ""

APPSECRET = "P9tUh780Sc8Eba4DAOX3iA"

CID = "ddbbd1dbc792e1059026c63f6c6cb15a"


def pushMessageToSingle(cid=CID):
    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    # 1.TransmissionTemplate:透传功能模板
    title = u"直播提醒"
    desc = u"你关注的“你是谁”正在直播，快来观看！"
    content = u"%d" % 1
    template = NotificationTemplateAndroid(title,desc,content)
    # message
    message = IGtSingleMessage()
    message.isOffline = True
    message.offlineExpireTime = 1000 * 3600 * 12
    message.data = template
    # message.pushNetWorkType = 2

    target = Target()
    target.appId = APPID
    target.clientId = cid

    try:
        ret = push.pushMessageToSingle(message, target)
        print ret
    except RequestException, e:
        requstId = e.getRequestId()
        ret = push.pushMessageToSingle(message, target, requstId)
        print ret

# 通知透传模板动作内容
def NotificationTemplateAndroid(title=u"标题", desc=u"说明", content=u""):
    template = NotificationTemplate()
    template.appId = APPID
    template.appKey = APPKEY
    template.transmissionType = 1
    template.transmissionContent = content
    template.title = title
    template.text = desc
    template.logo = "icon.png"
    template.logoURL = ""
    template.isRing = True
    template.isVibrate = True
    template.isClearable = True
    return template

# 通知透传模板动作内容
def NotificationTemplateIOS(title="标题", desc="说明", content=""):
    template = NotificationTemplate()
    template.appId = APPID
    template.appKey = APPKEY
    template.transmissionType = 1
    template.transmissionContent = content
    template.title = title
    template.text = desc
    template.logo = "icon.png"
    template.logoURL = ""
    template.isRing = True
    template.isVibrate = True
    template.isClearable = True
    # 设置APNS信息
    apnpayload = APNPayload()
    apnpayload.badge = 4
    apnpayload.sound = "test1.wav"
    apnpayload.contentAvailable = 1
    apnpayload.category = "ACTIONABLE"
    #简单类型如下设置
    alertMsg = SimpleAlertMsg()
    alertMsg.alertMsg = "alertMsg"
    #字典类型如下设置
    #alertMsg = DictionaryAlertMsg()
    #alertMsg.body = 'body'
    #alertMsg.actionLocKey = 'actionLockey'
    #alertMsg.locKey = 'lockey'
    #alertMsg.locArgs=['loc-args']
    #alertMsg.launchImage = 'launchImage'
    # IOS8.2以上版本支持
    #alertMsg.title = 'Title'
    #alertMsg.titleLocArgs = ['TitleLocArg']
    #alertMsg.titleLocKey = 'TitleLocKey'
    #可以设置字典类型AlertMsg和简单类型AlertMsg其中之一
    apnpayload.alertMsg = alertMsg
    template.setApnInfo(apnpayload)
    return template

pushMessageToSingle()

