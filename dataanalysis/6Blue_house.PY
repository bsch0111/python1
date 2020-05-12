import pandas as pd
import urllib.request
import re
import matplotlib.pyplot as plt
import numpy as np

#프로그래스바
from tqdm import tqdm
#형태소
from konlpy.tag import Okt
#토큰나이즈
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
#모델을 위함
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding


train = pd.read_csv("C:/inputcsv/Blue House/train.csv", index_col = 'index')
test = pd.read_csv("C:/inputcsv/Blue House/test.csv", index_col = 'index')
submission = pd.read_csv("C:/inputcsv/Blue House/sample_submission.csv", index_col = 'index')

train.info
#결측값 체크
train.isnull().sum()

#데이터 전처리 
#결측값 삭제
train = train.dropna(how='any')
train['data'] = train['data'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","") #특수문자 제거
test['data'] = test['data'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","") #특수문자 제거
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다','을'] #불용어

okt = Okt()

X_train = []
#tqdm : 프로그래스바 생성 및 함수나 반복문의 TTC(time to completation)을 예측
#https://antilibrary.org/2269

#list = []
#for x in tqdm(range(10000)):
#    list.append(x**x)
#***

# 형태소 구분
# 형태소란 뜻을 가진 가장 작은 말의 단위
# https://wikidocs.net/21698
for sentence, i in zip(train['data'],tqdm(range(len(train['data'])))) :
    temp_X = []
    temp_X = okt.morphs(sentence, stem = True)
    temp_X = [word for word in temp_X if not word in stopwords]
    X_train.append(temp_X)

#####
X_test =  []
for sentence in test['data']:
    temp_X = []
    temp_X = okt.morphs(sentence, stem=True)
    temp_X = [word for word in temp_X if not word in stopwords]
    X_test.append(temp_X)


#토큰나이즈(Tokenize)
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)
X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequence(X_test)
max_len = 500
X_train = pad_sequences(X_train, maxlen = max_len)
X_test = pad_sequence(X_test, maxlen = max_len)
y_train = to_categorical(train['category'])

#모델 생성 및 훈련
model = Sequential()
model.add(Embedding(vocab_size, 120))
model.add(LSTM(120))
model.add(Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
history = model.fit(X_train, y_train, batch_size=128, epochs=15)

#훈련된 모델로 예측, submission 파일 생성
y_pred = model.predict_classes(X_test)
sample_submission['category'] = y_pred
sample_submission.to_csv('C:/inputcsv/Blue House/submission.csv',encoding='utf-8', index=False)
