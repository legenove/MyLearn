# -*- coding: utf-8 -*-
__author__ = 'legenove'

from setting import settings


follow_log = '{ICP_CODE}\t{DATA_TYPE}\t{USER_ID}\t{USER_NAME}\t{NICK_NAME}\t' \
             '{FOLLOW_OTHERS_NUM}\t{FOLLOW_NUM}\t{FOLLOW_NICK_NAME}\t{MODIFY_TIME}\t{ACTION}'



follow_dict = {
    'ICP_CODE': settings.get('ICP_CODE'),
    'DATA_TYPE': settings.get('DATA_TYPE'),
    'USER_ID': "",                           # account.id
    'USER_NAME': "",                         # 空
    'NICK_NAME': "",                         # account.nickname
    'FOLLOW_OTHERS_NUM': "",                 # 关注数量
    'FOLLOW_NUM': "",                        # 被关注数
    'FOLLOW_NICK_NAME': "",                  # 关注的好友昵称
    'MODIFY_TIME': "",                       # account_follow.data_created
    'ACTION': "收听"
}