#MATPLOTLIBDATA Warning 무시
import warnings
warnings.filterwarnings("ignore", "(?s).*MATPLOTLIBDATA.*", category=UserWarning)

#import pandas
from image_match.goldberg import ImageSignature


import sys
# 파일 선택 후 파일 경로 읽어오기
# root.filename[0], root.filename[1]와 파일 경로가 배열로 입력

# 파일이 2개가 아닐 때 예외를 처리하는 코드 추가 필요


gis = ImageSignature()

a = gis.generate_signature(sys.argv[1])
b = gis.generate_signature(sys.argv[2])
c = gis.normalized_distance(a,b)

# 0 ~ 0.3 까지를 매우 유사한 것으로 판단
# Image Signature는 유사함에 대한 증거를 추출할 수 없음, 증거가 필요할때는 SIFT와 KNN을 사용한 코드를 사용
print("{")
if c > 0.45:
    print(' "match" : "0"')
    print(' "match_enough" :"false" ')
    print("}")
else:
    match_percentage = 100-(70/3)*c
    print(' "match" : "%d"' % match_percentage)
    print(' "match_enough" :"true" ')
    print("}")

