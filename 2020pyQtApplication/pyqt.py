import sys
import requests
# PYQT5를 이용하기 위한 모듈갱신
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 불러오고자 하는 .ui 파일
# .py 파일과 같은 위치에 있어야 함
form_class = uic.loadUiType("search.ui")[0]

class MyWindow(QDialog, form_class):
    #초기 설정해주는 init
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 시그널(이벤트루프에서 발생할 이벤트) 선언
        # self.객체명.객체함수.connect(self.슬롯명)
        self.search_btn.clicked.connect(self.search_btn_click)

    # 시그널을 처리할 슬롯
    # Couch DB sample Query : data = '{"selector":{"작품명":{"$regex":"두여"}}}'.encode('utf-8')

    def search_btn_click(self):
        # 입력된 textedit에서 text GET
        name = self.name.text()
        start_year = self.startyear.text()
        end_year = self.end_year.text()
        keyword1 = self.keyword1.text()
        keyword2 = self.keyword2.text()
        headers = {"Accept-Encoding": "gzip", 'Content-Type': 'application/json'}
        # query = '{"selector":{"작품명":{"$regex":' +'"'+ name +'"'+ '}}}'
        query = '{"selector":{"작품명":{"$regex":' +'"'+ name +'"'+ '},"제작시작년도":{"$gte":' + start_year + '},"제작종료년도":{"$lte":' + end_year + '},"키워드":{"$in":['+'"'+ keyword1 + '", "' + keyword2 + '"' + ']}}}'
        
        data = query.encode('utf-8')
        
        response = requests.post('http://192.168.120.239:5984/condatabase/_find', headers=headers, data=data)
        self.textBrowser.setText(response.text)
        




if __name__=="__main__":
    app=QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()

    #이벤트 루프 진입 전 작업할 부분




    #이벤트 루프 진입
    app.exec_()

