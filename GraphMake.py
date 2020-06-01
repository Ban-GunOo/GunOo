import numpy as np
import pandas as pd                        #파일를 불러오기 위한 모듈
import matplotlib.pyplot as plt            #그래프 출력에 필요한 모듈
from matplotlib import font_manager, rc    #그래프에 한글이 출력되기 위해 필요한 함수
import csv

pd.set_option('display.max_rows', 1200)     # 출력 결과 생략 방지
pd.set_option('display.max_columns', 1200)
pd.set_option('display.width', 1000)

class GraphMake:
    def __init__(self):
        f = 'restaurant_list.csv'  # csv 파일 불러오기
        df = pd.read_csv(f)

        # CSV 파일에서 검색에 필요한 열만 추출
        self.Name = df.loc[:, "업소명"]
        self.Price = df.loc[:, "가격대"]
        self.Menu = df.loc[:, "메뉴"]

        data = {'업소명': self.Name, '가격대': self.Price, '메뉴': self.Menu}  # 그래프 객체에 데이터 추가

        self.DFrame = pd.DataFrame(data,)  # DFrame에 데이터 정렬해서 저장하고 리턴하기
        with open('Dframe.csv', 'r+', encoding='utf-8') as f:
            pd.read_csv("Dframe.txt")      # txt파일 생성
            pd.read_csv('Dframe.txt', sep=',', header=None, index_col=None, skiprows=None)
            for line in f:                     # 데이터를 콤마 기준으로 행과 열을 분할함
                fields = line.strip().split(',')
                print(fields, file=f)
                f.close()

    # 데이터에서 검색한 값이 있나 확인하는 함수
    def Find(self, money, menu):  # 가격대 ,메뉴 입력받은 값을 비교해서 비슷한 값 출력
        f = 'Dframe.txt'
        df = pd.DataFrame[f]
        treat1 = df[ money + 2000 >money > money - 2000] # 전체 열에서 데이터 근처에 있는 값을 가진 행 입력
        treat2 = df.loc[menu]                            # 검색 받은 메뉴와 이름이 같은 데이터를 입력
        if treat1 == treat2:                           # treat1,2에 둘 다 있는 값을 찾으면 데이터 저장
            for i in df:
                print(treat1, file=f)


    # 막대 그래프를 출력하는 함수
    def Graph(self,price,name):
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)  # 그래프에 한글로 출력되기 위해 필요한 문장

        with open('Dframe.txt', 'r', encoding='utf-8') as file:
            df =pd.DataFrame[file]
            grouped = df['가격대'].groupedby(df['식당이름']) #식당이름 별로 가격 그룹핑
            PRICE = [df[2]]                                  #가격 식당이름 선언
            NAME = [df[1]]
            price = grouped.pr()
            name = grouped.na()

            df2 = pd.DataFrame({'price' : price })
            df3 = pd.DataFrame({'name' :  name  })
            dic = {"price" : PRICE , "name" : NAME }

            df_list = pd.DataFrame[dic]         #데이터 프레임 변환

            plt.figure(figsize=(12, 8))  # 그래프의 크기 지정

            pos = np.arange(5)
            rects = plt.bar(pos, PRICE, align='center', width=0.5)

            # x축 설정
            xpos = np.arange(len(PRICE))
            plt.xticks(xpos + 1, NAME)
            plt.xlabel("식당이름", fontsize=14)

            # y축 설정
            plt.yticks([10000, 20000, 30000, 40000, 50000])  # 그래프 y축 간격 만원씩
            plt.ylabel("가격대", fontsize=14)
            plt.ylim([2000, 60000])  # 그래프 최솟값 최댓값

            plt.title("그래프")

            plt.savefig('Graph.png', format='png', dpi=350)  # 그래프 저장하고 출력
            plt.show()