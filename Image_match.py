import pandas
from image_match.goldberg import ImageSignature

# filedialog를 위한 패키지 import
from tkinter import *
import tkinter.filedialog 

# 파일 선택 후 파일 경로 읽어오기
# root.filename[0], root.filename[1]와 파일 경로가 배열로 입력
root = Tk()
root.filename =  filedialog.askopenfilenames(initialdir = "C:/",title = "이미지를 비교할 두개의 파일 선택",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
# 파일이 2개가 아닐 때 예외를 처리하는 코드 추가 필요


gis = ImageSignature()

a = gis.generate_signature(root.filename[0])
b = gis.generate_signature(root.filename[1])
c = gis.normalized_distance(a,b)


data = [[c]]
result_data=pandas.DataFrame(data, columns=['     A&B normalized_distance'])

# 0 ~ 0.3 까지를 매우 유사한 것으로 판단
# Image Signature는 유사함에 대한 증거를 추출할 수 없음, 증거가 필요할때는 SIFT와 KNN을 사용한 코드를 사용

print(result_data)