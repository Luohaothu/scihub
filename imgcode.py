#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
"""
作者: jinaYang
博客: yangshengliang.com
时间: 2016-11-6
功能描述: 下载验证码图片,并显示

"""

import os

import requests


def getImage(imgUrl):
    r = requests.get(imgUrl, stream=True)
    extension = os.path.splitext(imgUrl)[1]  # 获取扩展名
    imgName = ''.join(["./image", extension])
    with open(imgName, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()

    return imgName


def downloadPDF(pdfUrl):
    r = requests.get(pdfUrl, stream=True)
    extension = os.path.splitext(pdfUrl)[1]
    pdfName = ''.join(["./pdf", extension])
    with open(pdfName, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()

    return pdfName

def showImage():
    image = getImage("https://moscow.sci-hub.cc/captcha/securimage_show.php")
    from PIL import Image
    import matplotlib.pyplot as plt
    img = Image.open(image)
    plt.figure("img")
    plt.imshow(img)
    plt.show()


if __name__ == "__main__":
    showImage()
    # downloadPDF("https://moscow.sci-hub.cc/e29656cac20acd1376914f504136ad2f/ji2012.pdf")
