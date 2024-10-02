# 한 줄짜리 주석
"""
코드 작성 일자 : 2024년 10월 1일
코드 작성자 : 한수민
코드 이름 : utils.py
코드 목적 : 유용한 함수를 따로 저장해 두고 불러워 사용하기 위함"""

def factorial(x) :
    if x <=1 :
        return 1
    return x * factorial(x-1)


def gugudan(x):
    for i in range(9):
        print((i + 1) * x)




