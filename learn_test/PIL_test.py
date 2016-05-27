# -*- coding: utf-8 -*-
__author__ = 'legenove'

import Image

import ImageFilter

im = Image.open("DSC_9016.JPG")
w, h = im.size
print w, h
im2 = im.filter(ImageFilter.GaussianBlur)
im2.show()