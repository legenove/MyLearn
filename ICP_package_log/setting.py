# -*- coding: utf-8 -*-
__author__ = 'legenove'

settings = {
    'ICP_CODE': 'ICP_CODE',  # TODO: ICP编码
    'DATA_TYPE': '',         # TODO: 协议类型标识
    'BUISY_DIRS': [           # TODO: 我们需要上报的类型
        'register',
        'connect',
        'group',
        'login',
        'record',  # Q2
        'access',
        'reality',  # Q3
        'pay',
        'express',  # None
        'social'  # None
    ],
    'DATA_PATH': 'data\{ip}\{BUISY_DIR}\{log_time}\{DATA_TYPE}\{data_name}.bcp',
    'DATA_NAME': '{BUISY_DIR}_{DATA_TYPE}_{log_time}_{log_index}',
}