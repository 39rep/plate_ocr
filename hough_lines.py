import cv2
import scipy
import numpy as np
import math

# 画像の傾き検出
# @return 水平からの傾き角度
def get_degree(img):
    l_img = img.copy()
    gray_image = cv2.cvtColor(l_img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image,50,150,apertureSize = 3)
    minLineLength = 200
    maxLineGap = 30
    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)

    sum_arg = 0
    count = 0
    for line in lines:
        for x1,y1,x2,y2 in line:
            arg = math.degrees(math.atan2((y2-y1), (x2-x1)))
            HORIZONTAL = 0
            DIFF = 20 # 許容誤差 -> -20 - +20 を本来の水平線と考える
            if arg > HORIZONTAL - DIFF and arg < HORIZONTAL + DIFF : 
                sum_arg += arg
                count += 1

    if count == 0:
        return HORIZONTAL
    else:
        return (sum_arg / count) - HORIZONTAL
    

src = "orig/plate10.jpg"
img = cv2.imread(src)

arg = get_degree(img=img)
rotate_img = scipy.ndimage.rotate(img, arg)

cv2.imwrite("res.jpg", rotate_img)