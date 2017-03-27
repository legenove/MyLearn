# -*- coding: utf-8 -*-
__author__ = 'legenove'

from setting import settings


login_log = '{ICP_CODE}\t{DATA_TYPE}\t{SRC_IP}\t{SRC_PORT}\t{CORP_SITE}\t' \
             '{CORP_LOGIN_ACCOUNT}\t{USER_ID}\t{USER_NAME}\t{NICK_NAME}\t{PASSWORD}\t' \
             '{MAC_ADDRESS}\t{INNER_IP}\t{ACTION_TIME}\t{ACTION}\t{LONGITUDE}\t' \
             '{LATITUDE}\t{TERMINAL_TYPE}\t{OS_TYPE}\t{STATION_ID}\t{COMMUNITY_CODE}\t' \
             '{IMEI_CODE}\t{IMSI_CODE}\t{EXTEND_ITEM_1}\t{EXTEND_ITEM_2}\t{EXTEND_ITEM_3}'



login_dict ={
    'ICP_CODE': settings.get('ICP_CODE'),
    'DATA_TYPE': settings.get('DATA_TYPE'),
    'SRC_IP': "",                            # TODO: 源ip
    'SRC_PORT': "",                          # TODO: 源端口
    'CORP_SITE': "",                         # TODO: 合作网站
    'CORP_LOGIN_ACCOUNT': "",                # TODO: 合作网站账号
    'USER_ID': "",                           # account.id
    'USER_NAME': "",                         # 空
    'NICK_NAME': "",                         # account.nickname
    'PASSWORD': "",                          # 空
    'MAC_ADDRESS': "",                       # TODO: 源Mac
    'INNER_IP': "",                          # TODO: 内网IP
    'ACTION_TIME': "",                       # TODO: 登录时间
    'ACTION': "",                            # TODO: 上线/登录 下线/离线/退出等
    'LONGITUDE': "",                         # TODO: 经度
    'LATITUDE': "",                          # TODO: 纬度
    'TERMINAL_TYPE': "",                     # TODO: 终端类型  01:PC   02:手机  03:PAD
    'OS_TYPE': "",                           # TODO: 操作系统 09:WINDOWS  10:UNIX  11:LINUX  12:MAC  13:IOS  14:ANDROID
    'STATION_ID': "",                        # TODO: 手机基站号
    'COMMUNITY_CODE': "",                    # TODO: 手机小区号
    'IMEI_CODE': "",                         # TODO: 移动终端设备
    'IMSI_CODE': "",                         # TODO: 移动用户的 IMSI
    'EXTEND_ITEM_1': "",                     # 预留1
    'EXTEND_ITEM_2': "",                     # 预留2
    'EXTEND_ITEM_3': ""                      # 预留3
}
