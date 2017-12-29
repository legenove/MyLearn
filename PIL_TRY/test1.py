# -*-coding:utf-8-*-
import sys
import requests
from requests.exceptions import (ConnectTimeout, ReadTimeout,
                                 ConnectionError)
from urllib import urlencode

TIMEOUT = 2

PY2 = sys.version_info[0] == 2
if PY2:
    text_type = unicode
    iteritems = lambda d, *args, **kwargs: d.iteritems(*args, **kwargs)

    def to_native(x, charset=sys.getdefaultencoding(), errors='strict'):
        if x is None or isinstance(x, str):
            return x
        return x.encode(charset, errors)
else:
    text_type = str
    iteritems = lambda d, *args, **kwargs: iter(d.items(*args, **kwargs))

    def to_native(x, charset=sys.getdefaultencoding(), errors='strict'):
        if x is None or isinstance(x, str):
            return x
        return x.decode(charset, errors)

import requests as req
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import cStringIO
import base64

def get_img_by_uri(uri):
    # url获取图片
    response = req.get(uri)
    img = Image.open(BytesIO(response.content))
    return img.convert('RGBA')

def create_circle(s=640):
    # 创建一个圆
    img = Image.new('RGBA', size=(s, s), color=(255, 255, 255, 0))
    canvas = ImageDraw.Draw(img)
    canvas.ellipse((0, 0, s, s), fill=(255, 255, 255, 255))
    del canvas
    return img

# def create_shaddow(agvs, w=640, h=315):
#     img = Image.new("P", size=(w, h), color=agvs)
#     img.convert("RGBA")
#     img_l = Image.new("L", size=(w, h), color=255)

def paste_center_img(target, img, x, y):
    hx, hy = img.size
    start = (x - hx/2, y-hy/2)
    target.paste(img, start, img)


def paste_top_center_img(target, img, x, y):
    hx, hy = img.size
    start = (x - hx/2, y)
    target.paste(img, start, img)

img_src = "http://audio.zaih.com/tmp_91fa6f793fff8a861fee4085de9dac6c.jpg?imageMogr2/thumbnail/!151p/crop/!960x960a303a609"

# 生成白板
w, h = 640, 1110
image = Image.new('RGBA', size=(w, h), color=(255, 255, 255, 255))

img = get_img_by_uri(img_src)
img.thumbnail((640, 640))
# avg_8bit = sum([i[1] for i in img.convert("P").getcolors()])/sum([i[0] for i in img.convert("P").getcolors()])
# create_shaddow(avg_8bit)
qrcode_uri = "http://audio.zaih.com/StoryQrcode_3036790321744423.jpg"
qrcode = get_img_by_uri(qrcode_uri)
qrcode.thumbnail((138, 138))
h_size = 150
hw_size = 160

play_icon = Image.open("play_icon.png").convert('RGBA')
circle = create_circle()
# shaddow = Image.open("shaddow.png").convert('RGBA')
circle.thumbnail((hw_size, hw_size))
# shaddow.thumbnail((640, 315))

paste_center_img(img, circle, 320, 640-5)
paste_top_center_img(image, img, 320, 0)


def get_header(uri):
    return get_img_by_uri(uri)

def cut_header(head_im, s=h_size):
    img = Image.new('RGBA', size=(s, s), color=(255, 255, 255, 0))
    img_k = Image.new('RGBA', size=(s, s), color=(0, 0, 0, 0))
    canvas = ImageDraw.Draw(img)
    # Now I draw the circle:
    canvas.ellipse((0, 0, s, s),
                   fill=(255, 255, 255, 255))
    del canvas
    return Image.composite(head_im, img_k, img)


def add_shadow(im, s=h_size):
    img = Image.new('RGBA', size=(s, s), color=(255, 255, 255, 0))
    # img_1 = Image.new('RGBA', size=(s, s), color=(255, 255, 255, 0))
    canvas = ImageDraw.Draw(img)
    # Now I draw the circle:
    canvas.ellipse((0, 0, s, s), fill=(0, 0, 0, 80))
    # ImageCms.applyTransform(im, img, inPlace=0)
    del canvas
    # im.putalpha(img)
    im.paste(img, (0, 0), img)
    # Image.alpha_composite(im, img)
    # im.paste(img, (0, 0), mask=img)
    return im

head_uri = "https://wx.qlogo.cn/mmopen/vi_32/ajNVdqHZLLDBTxs7mGQia8ojRyjKU6Krm8RDkpvsnV56SXKOkD3dTKj1P0ByLz2AsO3OMpKVvItMrZzibibSHsrpA/0"


def handle_head(url):
    img = get_header(url)
    r, r = img.size
    img = cut_header(img, r)
    img = add_shadow(img, r)
    img.thumbnail((h_size, h_size))
    return img


PINGFANG_33 = ImageFont.truetype("PingFang.ttf", 26)
ZIKU_73 = ImageFont.truetype("ziku.ttf", 60)
PINGFANG_36 = ImageFont.truetype("ziku.ttf", 28)

def draw_text(im, text, x, y, font=PINGFANG_33):
    draw = ImageDraw.Draw(im)
    w, h = font.getsize(text)
    start = (x-w/2, y)
    draw.text(start, text, "black", font=font)
    del draw

x, y = image.size


# image.paste(shaddow, (0, 640-314), shaddow)
paste_center_img(image, handle_head(head_uri), x / 2, x-5)
paste_center_img(image, play_icon, x / 2, x-5)
paste_center_img(image, qrcode, x/2, 1004)

nickname = u"晓懒大呆瓜"
draw_text(image, nickname, 320, 726)
zuanti_name = u"王麻子讲故事"
draw_text(image, zuanti_name, 320, 796, ZIKU_73)
zuanti_title = u"王子在享受日光浴，青蛙也在晒太阳"
draw_text(image, zuanti_title, 320, 868, PINGFANG_36)

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config

poster_io = cStringIO.StringIO()
image.convert('RGB').save(poster_io, format='JPEG')
poster_io = cStringIO.StringIO(poster_io.getvalue())
img_str = base64.b64encode(poster_io.getvalue())
print img_str
# image.save("123.png", "PNG")
# image.convert('RGB').save("123.jpg", "JPEG")

QINIU_ACCESS_TOKEN = 'x7cu88uRBgDKIWHzGHvK-OgKznQpY4ZfhbObIrt2'
QINIU_SECRET_TOKEN = 'btfJJE_RuWdlX9C9Ww3Y3a2ayVBwDF5lKKsRLs7c'
QINIU_PRIVITE_BUCKET = 'fenda-media'

bucket_name = QINIU_PRIVITE_BUCKET
key = 'my-python-logo.png'
pipeline = 'zaih_media'

class Request(object):
    @classmethod
    def get(cls, host, path, params, protocal='https', timeout=TIMEOUT,
            headers=None):
        uri = '%s://%s%s' % (protocal, host, path)
        str_parmas = {}
        if params:
            for k, v in params.iteritems():
                str_parmas[k] = text_type(v).encode('utf-8')
            url_params = urlencode(str_parmas)
            if url_params:
                uri = "%s?%s" % (uri, url_params)
        try:
            response = requests.get(uri, params, timeout=timeout,
                                    headers=headers)
        except (ConnectTimeout, ReadTimeout):
            raise ConnectionError('conntect_error '
                                  'Failed to establish a new connection')
        return response

    @classmethod
    def post(cls, host, path, params, protocal='https', timeout=TIMEOUT,
             headers=None):
        uri = '%s://%s%s' % (protocal, host, path)
        str_parmas = {}
        if params:
            for k, v in params.iteritems():
                str_parmas[k] = text_type(v).encode('utf-8')
        try:
            response = requests.post(uri, json=str_parmas, timeout=timeout,
                                     headers=headers)
        except (ConnectTimeout, ReadTimeout):
            raise ConnectionError('conntect_error '
                                  'Failed to establish a new connection')
        return response

    @classmethod
    def post_by_body(cls, host, path, body, protocal='https', timeout=TIMEOUT,
                     headers=None):
        uri = '%s://%s%s' % (protocal, host, path)
        try:
            response = requests.post(uri, data=body, timeout=timeout,
                                     headers=headers)
        except (ConnectTimeout, ReadTimeout):
            raise ConnectionError('conntect_error '
                                  'Failed to establish a new connection')
        return response

def qiniu_putb64(pic, l, save_key):
    path = "/putb64/%s/key/%s" % (l, base64.urlsafe_b64encode(save_key))
    q =  Auth(QINIU_ACCESS_TOKEN, QINIU_SECRET_TOKEN)
    uptoken = q.upload_token(bucket_name,
                             save_key, 3600)
    headers = {
        "Content-Type": "application/octet-stream",
        "Authorization": "UpToken %s" % uptoken
    }
    response = Request.post_by_body('upload.qiniu.com', path, pic,
                                    protocal='http', headers=headers)
    return response.content

print qiniu_putb64(img_str, -1, key)
