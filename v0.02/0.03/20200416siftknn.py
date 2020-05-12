#MATPLOTLIBDATA Warning 무시
import warnings
warnings.filterwarnings("ignore", "(?s).*MATPLOTLIBDATA.*", category=UserWarning)

import cv2
import cv2.xfeatures2d as cv
import numpy
from matplotlib import pyplot as plt
import os

#------------------------------------------SIFT와 KNN을 이용한 이미지 매칭----------------------------------------#
# 회전 및 크기 변환, 기울임에도 이미지 매칭 가능
# 95% 이상 일치율을 보일 때 두 이미지가 동일한 이미지 기반이라고 판단
# 80% 이상 일치율을 보일 때 두 이미지가 유사한 이미지라고 판단
# 80% 이하 일치율을 보일 때 의미 없음


# 틀 참고
# https://github.com/ayushgarg31/Feature-Matching/blob/master/SIFT_KNN_BBS.py


#def SIFT_KNN_BBS(img1, img2):

# 실행 시 매개변수로 비교 대상 두개의 이미지 경로 입력
import sys



# 퍼센테이지(%)를 표현하기 위한 자료
# 참고: https://github.com/fchasen/imgcompare/blob/master/match.py
def filter_matches(kp1, kp2, matches, ratio = 0.75):
    mkp1, mkp2 = [], []
    for m in matches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            m = m[0]
            mkp1.append( kp1[m.queryIdx] )
            mkp2.append( kp2[m.trainIdx] )
    p1 = numpy.float32([kp.pt for kp in mkp1])
    p2 = numpy.float32([kp.pt for kp in mkp2])
    kp_pairs = zip(mkp1, mkp2)
    return p1, p2, list(kp_pairs)

    
# 이미지 파일 읽어 오기(img1, img2)
t1 = cv2.imread(sys.argv[1],0)
t2 = cv2.imread(sys.argv[2],0)

#SIFT 특성의 디스크립터(descriptor)를 취함
sift=cv.SIFT_create()

# detectAndCompute: 이미지 별 키포인트(keypoint)를 탐지하고, 디스크립터를 계산
# 리턴 값 : keypoint, 디스크립터(descriptor)
kp1, des1 = sift.detectAndCompute(t1, None)
kp2, des2 = sift.detectAndCompute(t2, None)

# img1에서 찾은 키포인트는 파랑색, img2에서 찾은 키포인트는 빨간색으로 표시
# drawKeypoints 의 flags 목룍 
# cv2.DRAW_MATCHES_FLAGS_DEFAULT
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS -> 참조한 코드였지만 지저분해보여서 기본으로 수정
# cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG
# cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS

f = cv2.drawKeypoints(t1,kp1,None,[0,0,255],flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)
nf =cv2.drawKeypoints(t2,kp2,None,[255,0,0],flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)

# bf(Brute-Force) 객체 생성
# bf를 knnMatch로 수행 후 matches 반환
# des1 기준 des2 비교 항목
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

good1 = []

p1, p2, kp_pairs = filter_matches(kp1, kp2, matches)
print("{")
if len(p1) >= 4:
    H, status = cv2.findHomography(p1, p2, cv2.RANSAC, 4.0)
# findHomography 설명자료 https://ballentain.tistory.com/38
# H는 p1이 p2로 변활할 수 있도록 해주는 변환행렬
    match_percentage = numpy.sum(status) / len(status) * 100
# match_percentage : 실제 매칭된 %
    if match_percentage < 80:
        H, status = None, None
        print(' "match" : "%d"' % len(p1))
        print(' "match_enough" :"false" ')
        print("}")
    else:
        print(' "match" : "%d"'  % match_percentage)
        print(' "match_enough" :"true" ')
        print("}")
else:
    H, status = None, None
    print(' "match" : """%d"""' % len(p1))
    print(' "match_enough" :"""false""" ')
    print("}")
# ----------------------------- 



# knn을 두번 수행해서 그 중 성능이 좋은 디스크립터 출력
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good1.append([m])

# bf를 knnMatch로 수행 후 matches 반환
# des1 기준 des2 비교 항목
matches = bf.knnMatch(des2,des1, k=2)

good2 = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good2.append([m])

good = []

for i in good1:
    img1_id1=i[0].queryIdx
    img2_id1=i[0].trainIdx

    (x1,y1)=kp1[img1_id1].pt
    (x2,y2)=kp2[img2_id1].pt

    for j in good2:
        img1_id2=j[0].queryIdx
        img2_id2=j[0].trainIdx

        (a1,b1)=kp2[img1_id2].pt
        (a2,b2)=kp1[img2_id2].pt

        if (a1 == x2 and b1 == y2) and (a2 == x1 and b2 == y1):
            good.append(i)

result=cv2.drawMatchesKnn(t1,kp1,t2,kp2,good,None,[255,0,0],flags=2)


#현재날짜와 현재시간을 이용한 파일이름 설정
import datetime
basename = datetime.datetime.now().strftime("%y%m%d_%H%M%S")

#결과를 파일출력으로 확인하기
# http://blog.naver.com/PostView.nhn?blogId=cosmosjs&logNo=220981929570&redirect=Dlog&widgetTypeCall=true
if not os.path.isdir('siftknn/'):
	os.mkdir('siftknn/')

cv2.imwrite('siftknn/'+basename+'.jpg',result)


#결과를 matplotlib를 이용하여 이미지로 보여주는 코드
#plt.imshow(result, interpolation = 'bicubic')
#plt.axis('off')
#plt.show()
