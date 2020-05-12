# import numpy as np 예제에는 있지만 왜 있는지 모르겠음
import cv2
import pandas
from matplotlib import pyplot as plt
from  tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilenames(initialdir = "C:/",title = "이미지를 비교할 두개의 파일 선택",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))


# 파일 선택 후 경로 입력으로 바꿔야함
img1 = cv2.imread(root.filename[0], 0)
img2 = cv2.imread(root.filename[1], 0)


orb = cv2.xfeatures2d.SIFT_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

good = []
for m,n in matches:
    if m.distance < 0.3*n.distance:
        good.append([m])

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:20],None,flags=2)
plt.imshow(img3),plt.show()

data = [[len(kp1),len(kp2),len(matches)]]
result_data=pandas.DataFrame(data, columns=['Image1_feature','Image2_feature','match_feature'])

print(result_data)