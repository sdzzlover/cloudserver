import requests
import json
import base64
import os
import cv2
import time

from PIL import Image

# 指定要检测的图片并生成列表[("image", img_1), ("image", img_2), ... ]
file_list =["D:/xxx.txt"]# [":/Users/Administrator/Desktop/face/FaceMaskDetection/img2/demo3.jpg"]
files = "xxx.txt"#[("image", (open(item, "rb"))) for item in file_list]
#image=cv2.imread(file_list[0])
# 指定检测方法为pyramidbox_lite_server_mask并发送post请求#华为云服务器 地址
url = "http://公网ip:8000/predict/image/pyramidbox_lite_server_mask"
sttime=time.time()
r = requests.post(url=url, data=files)
endtime=time.time()
#results1 = eval(r.json())#test   字典输出的时候应用
print(r.text)
print(endtime-sttime)
