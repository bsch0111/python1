#import numpy as np 왜있는지 모르겠음
import cv2
from matplotlib import pyplot as plt
import numpy as np
from  tkinter import *


def filter_matches(kp1, kp2, matches, ratio = 0.8):
    mkp1, mkp2 = [], []
    for m in matches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            m = m[0]
            mkp1.append( kp1[m.queryIdx] )
            mkp2.append( kp2[m.trainIdx] )
    p1 = np.float32([kp.pt for kp in mkp1])
    p2 = np.float32([kp.pt for kp in mkp2])
    kp_pairs = zip(mkp1, mkp2)
    return p1, p2, list(kp_pairs)

norm = cv2.NORM_L2
root = Tk()
root.filename =  filedialog.askopenfilenames(initialdir = "C:/",title = "이미지를 비교할 두개의 파일 선택",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

img1 = cv2.imread(root.filename[0], 0)
img2 = cv2.imread(root.filename[1], 0)
 
sift = cv2.xfeatures2d.SIFT_create()
 
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
 
bf = cv2.BFMatcher(norm)
# matches = bf.knnMatch(des1,des2, k=2)
matche = bf.match()

good = []
for m,n in matches:
    if m.distance < 0.3*n.distance:
        good.append([m])
 
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)


p1, p2, kp_pairs = filter_matches(kp1, kp2, matches)
H, status = cv2.findHomography(p1, p2, cv2.RANSAC, 5.0)

print('%d%% matched' % (np.sum(status) / len(status) * 100))
 
plt.imshow(img3),plt.show()
