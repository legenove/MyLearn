# -*- coding: utf-8 -*-

import hashlib

orderid = "1040148732613602152591"
merchantid = "22294531"
key = "test"

signData = ""
text = "merchant=" + merchantid + "&orderId=" + orderid + "&key=" + key
m = hashlib.md5()
m.update(text)
signData = m.hexdigest()
print signData