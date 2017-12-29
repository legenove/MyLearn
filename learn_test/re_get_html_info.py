import re  
import requests
res = requests.get('https://segmentfault.com/q/1010000006789851')
html = res.content
m = re.search(r'<title>(.*)</title>', html, flags=re.I)
title = m and m.group(1) or ""
m = re.search(r'((http|https):.+\.(jpg|gif|png|bmp))', html, flags=re.I)
print title
print m and m.group(1) or ""