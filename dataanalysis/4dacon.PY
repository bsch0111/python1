import pandas as pd
from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv('C:/inputcsv/dacon_천체/train.csv',index_col='id')
test = pd.read_csv('C:/inputcsv/dacon_천체/test.csv',index_col='id')
sample_submission = pd.read_csv('C:/inputcsv/dacon_천체/sample_submission.csv',index_col='id')

column_number = {}
for i, column in enumerate(sample_submission.columns):
    column_number[column] = i

def to_number(x,dic):
    return dic[x]

train['type_num'] = train['type'].apply(lambda x : to_number(x, column_number))

train[['type','type_num']]

train_x = train.drop(columns=['type', 'type_num'],axis=1)
train_y = train['type_num']
test_x = test

forest = RandomForestClassifier(n_estimators = 100, n_jobs = -1)
forest.fit(train_x, train_y)

forest

# 생성된 모델로 예측 데이터 생성
y_pred = forest.predict_proba(test_x)

submission = pd.DataFrame(data=y_pred, columns=sample_submission.columns, index=sample_submission.index)
submission.to_csv('submission.csv', index=True)
