# -*- coding: utf-8 -*-
__author__ = 'legenove'

from setting import settings

register_log = '{ICP_CODE}\t{DATA_TYPE}\t{USER_ID}\t{USER_NAME}\t{PASSWORD}\t{NICK_NAME}\t{BRIF_Intro}\t' \
               '{STATUS}\t{REAL_NAME}\t{SEX}\t{BIRTHDAY}\t{CONTACT_TEL}\t{CERTIFICATE_TYPE}\t{CERTIFICATE_CODE}\t' \
               '{BIND_TEL}\t{BIND_QQ}\t{BIND_MSN}\t{EMAIL}\t{REGISTER_TIME}\t{LAST_LOGIN_TIME}\t' \
               '{LAST_CHANGE_PASSWORD}\t{LAST_MODIFY_TIME}\t{REGISTER_IP}\t{REGISTER_PORT}\t{REGISTER_MAC}\t' \
               '{REGISTER_BIOS_ID}\t{PROVINCE}\t{CITY}\t{ADDRESS}\t{IMAGE_NAME}'

register_dict = {
    'ICP_CODE': settings.get('ICP_CODE'),
    'DATA_TYPE': settings.get('DATA_TYPE'),
    'USER_ID': '',                     # account.id
    'USER_NAME': '',                   # 空
    'PASSWORD': '',                    # 空
    'NICK_NAME': '',                   # account.nickname
    'BRIF_Intro': '',                  # account.introduction
    'STATUS': '',                      # 答主：3 普通：2
    'REAL_NAME': '',                   # account.realname
    'SEX': '',                         # 空
    'BIRTHDAY': '',                    # 空
    'CONTACT_TEL': '',                 # account.mobile 联表
    'CERTIFICATE_TYPE': '',            # 空
    'CERTIFICATE_CODE': '',            # 空
    'BIND_TEL': '',                    # account.mobile 联表
    'BIND_QQ': '',                     # 空
    'BIND_MSN': '',                    # 空
    'EMAIL': '',                       # 空
    'REGISTER_TIME': '',               # account.date_created
    'LAST_LOGIN_TIME': '',             # 空
    'LAST_CHANGE_PASSWORD': '',        # 空
    'LAST_MODIFY_TIME': '',            # account.date_updated
    'REGISTER_IP': '',                 # 空
    'REGISTER_PORT': '',               # 空
    'REGISTER_MAC': '',                # 空
    'REGISTER_BIOS_ID': '',            # 空
    'PROVINCE': '',                    # 空
    'CITY': '',                        # 空
    'ADDRESS': '',                     # 空
    'IMAGE_NAME': ''                   # 下载头像文件
}
