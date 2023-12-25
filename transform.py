import cv2
import numpy as np

from IPython.display import display, Image

def display_cv_image(image, format='.png'):
    decoded_bytes = cv2.imencode(format, image)[1].tobytes()
    display(Image(data=decoded_bytes))

src = "images/plate10.jpg"
img = cv2.imread(src)
# img = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2))
display_cv_image(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th1 = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)
display_cv_image(th1)

# 輪郭抽出
contours, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 面積の大きいもののみ選別
areas = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 1000:
        epsilon = 0.1*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)
        areas.append(approx)

for area in areas:
    print("---area---")
    print(area)
    # if len(area[0]) < 3:
    #     areas.remove(area)

# print(areas)

cv2.drawContours(img,areas,-1,(0,255,0),3)
display_cv_image(img)
cv2.imwrite("result1.jpg", img)


img = cv2.imread(src)
# img = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2))
img = np.where(img > 220, 255, img)

dst = []

pts1 = np.float32(areas[0])
pts2 = np.float32([[0,0],[0,300],[600,300],[600,0]])
# pts2 = np.float32([[600,300],[600,0],[0,0],[0,300]])


M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(600,300))
cv2.imwrite("result.jpg", dst)

display_cv_image(dst)
