# filedialog를 위한 패키지 import
from tkinter import *
import tkinter.filedialog 

from PIL import Image
import imagehash

# 파일 선택 후 파일 경로 읽어오기
# root.filename[0], root.filename[1]와 파일 경로가 배열로 입력
root = Tk()
root.filename =  tkinter.filedialog.askopenfilenames(initialdir = "C:/",title = "이미지를 비교할 두개의 파일 선택",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
# 파일이 2개가 아닐 때 예외를 처리하는 코드 추가 필요

# 숫자가 0이면 일치하며
# 숫자가 작을수록 비슷하다고 판단
file1_hash = imagehash.dhash(Image.open(root.filename[0]))
file2_hash = imagehash.dhash(Image.open(root.filename[1]))
print(file1_hash - file2_hash)