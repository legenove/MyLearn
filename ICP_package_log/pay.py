# -*- coding: utf-8 -*-
__author__ = 'legenove'

from setting import settings


pay_log = '{ICP_CODE}\t{DATA_TYPE}\t{USER_ID}\t{CORP_SITE}\t{CORP_LOGIN_ACCOUNT}\t' \
          '{USER_NAME}\t{NICK_NAME}\t{PAY_IP}\t{PAY_PORT}\t{PAY_MAC}\t{PAY_IMEI}\t' \
          '{PAY_BIOSID}\t{ACTION_TIME}\t{ACTION}\t{PAY_ID}\t{GOODS_NO}\t{GOODS_NAME}\t' \
          '{GOODS_TYPE}\t{GOODS_NUM}\t{PAY_CARD}\t{TO_CARD}\t{TO_NAME}\t{PAY_CELL}\t' \
          '{PAY_SUM}\t{PAY_NAME}\t{PAY_MOBILE}\t{PAY_ADD}\t{DELIVERY_ID}'


pay_dict = {
    'ICP_CODE': settings.get('ICP_CODE'),
    'DATA_TYPE': settings.get('DATA_TYPE'),
    'USER_ID': "",                           # account.id
    'CORP_SITE': "",                         # TODO: 合作网站
    'CORP_LOGIN_ACCOUNT': "",                # TODO: 合作网站账号
    'USER_NAME': "",                         # 空
    'NICK_NAME': "",                         # account.nickname
    'PAY_IP': "",                            # TODO: 支付ip
    'PAY_PORT': "",                          # TODO: 支付端口
    'PAY_MAC': "",                           # TODO: 支付是被MAC
    'PAY_IMEI': "",                          # TODO: 支付设备IMEI
    'PAY_BIOSID': "",                        # TODO: 支付其他硬件特征
    'ACTION_TIME': "",                       # TODO: 支付发生时间
    'ACTION': "",                            # TODO: 动作  转账,汇款,充值,交易
    'PAY_ID': "",                            # TODO: 支付编号
    'GOODS_NO': "",                          # TODO: 商品交易号或订单号
    'GOODS_NAME': "",                        # TODO: 商品名称
    'GOODS_TYPE': "",                        # TODO: 商品分类
    'GOODS_NUM': "",                         # TODO: 数量
    'PAY_CARD': "",                          # TODO: 支付卡号或账号
    'TO_CARD': "",                           # TODO: 对方卡号
    'TO_NAME': "",                           # TODO: 接收方名称
    'PAY_CELL': "",                          # TODO: 接收方名称
    'PAY_SUM': "",                           # TODO: 交易金额
    'PAY_NAME': "",                          # TODO: 买方姓名
    'PAY_MOBILE': "",                        # TODO: 买方手机
    'PAY_ADD': "",                           # TODO: 买方地址
    'DELIVERY_ID': ""                        # TODO: 物流单号
}
