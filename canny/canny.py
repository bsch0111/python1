import cv2
from matplotlib import pyplot as plt


# filedialog를 위한 패키지 import
from tkinter import *
import tkinter.filedialog 


def nothing():
    pass


#Canny 소스 참고
#https://m.blog.naver.com/samsjang/220507996391

# 파일 선택 후 파일 경로 읽어오기
# root.filename[0], root.filename[1]와 파일 경로가 배열로 입력
root = Tk()
root.filename =  filedialog.askopenfilenames(initialdir = "C:/",title = "이미지를 비교할 두개의 파일 선택",filetypes = (("jpg files","*.jpg"),("bmp files","*.bmp"),("all files","*.*")))
# 파일이 2개가 아닐 때 예외를 처리하는 코드 추가 필요

# 이미지 파일 읽어 오기(img1)
img_gray = cv2.imread(root.filename[0],cv2.IMREAD_GRAYSCALE)

cv2.namedWindow("Canny Edge")
cv2.createTrackbar('low threshold', 'Canny Edge', 0, 1000, nothing)
cv2.createTrackbar('high threshold', 'Canny Edge', 0, 1000, nothing)

cv2.setTrackbarPos('low threshold', 'Canny Edge', 50)
cv2.setTrackbarPos('high threshold', 'Canny Edge', 150)

cv2.imshow("Original", img_gray)

while True:

    low = cv2.getTrackbarPos('low threshold', 'Canny Edge')
    high = cv2.getTrackbarPos('high threshold', 'Canny Edge')

    img_canny = cv2.Canny(img_gray, low, high)
    cv2.imshow("Canny Edge", img_canny)

    if cv2.waitKey(1)&0xFF == 27:
        break


cv2.destroyAllWindows()