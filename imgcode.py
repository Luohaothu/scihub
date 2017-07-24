#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
"""
作者: jinaYang
博客: yangshengliang.com
时间: 2016-11-6
功能描述: 下载验证码图片,并显示

"""

import requests
import os


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


def showImage():
    image = getImage("http://www.chinabidding.com.cn/zbw/login/image.jsp")
    from PIL import Image
    import matplotlib.pyplot as plt
    img = Image.open(image)
    plt.figure("img")
    plt.imshow(img)
    plt.show()


if __name__ == "__main__":
    showImage()
