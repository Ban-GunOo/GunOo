#2017038082_반용빈
import numpy as np
import pandas as pd                        #파일를 불러오기 위한 모듈
import matplotlib.pyplot as plt            #그래프 출력에 필요한 모듈
from matplotlib import font_manager, rc    #그래프에 한글이 출력되기 위해 필요한 함수

pd.set_option('display.max_rows', 1200)     # 출력 결과 생략 방지
pd.set_option('display.max_columns', 1200)
pd.set_option('display.width', 1000)

class GraphMake:
    def __init__(self):                     #데이터 선언
        self.num = 0
        self.list = [self.Name,self.price,self.Menu]
        self.rs_list = []
        self.Money_list = []

    def Add(self,name,price,menu):          #데이터 리스트에 추가
        self.list.append = (name,price,menu)

        self.rs_list.append(name)            #식당이름 전용 리스트
        self.Money_list.append(price)         #가격대 전용 리스트

        self.num +=1

        return self.rs_list , self.Money_list       #식당리스트 와 가격대 리스트들 리턴하기

    # 막대 그래프를 출력하는 함수
    def Graph(self,rs_list,Money_list,Menu):    #리턴했던 리스트들과 검색한 음식이름 가져오기
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)  # 그래프에 한글을 출력하기 위해 필요한 문장

        # 데이터 프레임 변환

        plt.figure(figsize=(12, 8))  # 그래프의 크기 지정

        pos = np.arange(self.num)
        plt.bar(pos, Money_list, align='center', width=0.5,color = 'red')

        # x축 설정
        xpos = np.arange(len(Money_list))       #x축 길이
        plt.xticks(xpos + 1, rs_list)
        plt.xlabel("식당이름", fontsize=14)       #x축 이름과 폰트 크기

        # y축 설정
        plt.yticks([10000, 20000, 30000, 40000, 50000])  # 그래프 y축 간격 10000원씩
        plt.ylabel("가격대", fontsize=14)        #y축 이름과 폰트크기
        plt.ylim([2000, 60000])  # 그래프 최솟값 최댓값

        plt.title(Menu)             #제목 (음식이름)
        plt.savefig('./django_test/templates/Graph.png', format='png', dpi=350)  # 그래프 저장하고 출력
        plt.show()

#예시
#Graph = GraphMake()
#Graph.Add('중국집',15000,'짜장면')
#Graph.Graph(rs_list,Money_list,Menu)
