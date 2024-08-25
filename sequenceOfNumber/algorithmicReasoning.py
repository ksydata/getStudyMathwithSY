from typing import *


# 점화식 

def linearRecurrenceRelations(a0, p, q, n):
    """항들 간의 관계를 나타내는 점화식
    a_{n+1} = f(a_n)
    a_n = p*a_{n-1} + q"""
    a = a0
    # 초항을 초기값으로 설정

    for _ in range(1, n):
        a = p*a + q
    return a


# 수학적 귀납법(mathematicalInduction)
# 연쇄 반응을 이용한 등식을 증명하는 귀납법으로 분할정복에 적용가능
# 1. n=1일 때, 2. n=2(n=k...)일 때도 성립"""


# 분할정복 
def divideAndConquer(a: List):
    if len(a) == 1:
        return a[0]
    elif len(a) == 2:
        if a[0] > a[1]:
            return a[0]
        else:
            return a[1]
    else: 
    # len(a) > 2:
        length = len(a)
        div_front = divideAndConquer(a = a[0 : length//2])
        div_rear = divideAndConquer(a = a[length//2 : length])
        if div_front > div_rear:
            return div_front
        else:
            return div_rear
 

    
    
    
