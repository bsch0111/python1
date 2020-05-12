import pandas as pd
import os

dirname = "D:\\백승찬\\2020 엘에스웨어\\2020 [IITP] 콘텐츠 특화 블록체인 기술 개발\\☆ 연구과제 프로세스\\7. 1차년도 테스트데이터\\lsware\\000"

filelist = []
 

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        if os.path.isdir(full_filename):
            search(full_filename)
        else:
            ext = os.path.splitext(full_filename)[-1]
            if ext == '.json': 
                filelist.append(full_filename)



search(dirname)

testdata = pd.read_json(filelist[0])
testdata.drop(1)
testdata.drop(1) # 컬럼만 남음


for file in filelist:
    mergedata = pd.read_json(file)
    testdata = testdata.append(mergedata)



testdata.to_csv('result.csv')
testdata.columns


platform_name = testdata.drop_duplicates("platform_name")

platform_name['platform_name']

testdata['toon_name']

pd.set_option('display.width', 2000)

testdata.loc[testdata['toon_name']=='슬레이어']['platform_name']