con = 0
student = []

while True:
    print("===== 메뉴 =====\n")
    print("1.데이터 추가\n2.데이터 검색\n3.데이터 삭제\n4.데이터 정렬\n5.종료\n")

    num = int(input("번호를 입력해주세요 :"))

    if num == 1:
        name =input("이름 입력 : ")
        hak = input("학과 입력: ")
        bun = int(input("학번 입력: "))
        kor = int(input("국어 입력: "))
        eng = int(input("영어 입력: "))
        mat = int(input("수학 입력: "))

        all = kor + eng + mat
        avg = round(all/3,2)

        if avg >= 90:
            jum = 'A+'
        elif avg >= 80:
            jum = 'A0'
        elif avg >= 70:
            jum = 'B+'
        elif avg >= 60:
            jum = 'B0'
        elif avg >= 50:
            jum = 'C+'
        elif avg >= 40:
            jum = 'C0'
        elif avg >= 30:
            jum = 'D+'
        elif avg >= 20:
            jum = 'D0'
        else:
            jum = 'F'

        student.append([name, hak, bun, kor, eng, mat, all, avg, jum])
        con += 1

    elif num == 2:
        search = input('검색할 학생의 이름을 입력해주세요 : ')

        for i in range(0, con):
            if search == student[i][0]:
                print("=======================================================")
                print('이름\t' '\t학과 \t' '학번 \t' '\t국어 ' '  영어  ' ' 수학 ' ' 총점  ' '   평균 ' '  학점 \n')
                for j in range(0, 9):
                    print(student[i][j] , end='   ')
                print("\n=======================================================")

        else:
            print('해당 이름이 없습니다.')

    elif num == 3:
        score = int(input("학번을 입력해주세요 : "))
        delete = input("학생의 이름을 입력해주세요 : ")

        for i in range(0, con):
            if score == student[i][2]:
                if delete == student[i][0]:
                    del(student[i])
                    print("삭제 됐습니다")
                    con -= 1
        else:
            print("해당 이름이 없습니다")

    elif num == 4:
        sort = sorted(student,key = lambda student:student[0])
        print("이름 순 정렬 \n")
        print("=======================================================")
        for i in range(0, con):
                for j in range(0, 9):
                    print(student[i][j] , end='   ')
                    if(j == 8):
                        print('\n')
        print("\n=======================================================")
    elif num == 5:
        print("프로그램을 종료합니다")
        break
    else :
        print("잘못 입력하셨습니다.")
