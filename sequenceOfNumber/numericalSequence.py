from typing import *
from abc import *

# 숫자의 나열: 등차수열, 등비수열, 계차수열
# 실생활 적용: https://blog.naver.com/claykim999/223466634338

def accumulateSum(function: Callable):
    def wrapper(a: float, sequence_pattern: float, n: int):
        totalsum = 0
        for i in range(1, n+1):
            totalsum += function(a, sequence_pattern, i)
        return totalsum
    return wrapper

@accumulateSum
def arithmeticSequence(a: float, d: float, n: int):
    """각 항 사이에 일정한 수, 공차가 더해지는 등차수열
    a_n = a + (n-1)*d (단, a_n=등차수열의 일반항, a=초항, d=공차)"""
    return a + (n-1)*d

@accumulateSum
def geometricSequence(a: float, r: float, n: int):
    """각 항 사이에 일정한 수, 공비가 곱해지는 등비수열
    a_n = a x r^(n-1) (단, a_n=등비수열의 일반한, a=초항, r=공비)
    1, 0, -1을 경계로 r의 범위에 따라 다양한 양상을 띔"""
    return a * (r**(n-1))

def differenceSequence(a: float, b: List, n: int):
    """수열의 인접한 두 항에 대하여 뒷 항에서 앞 항을 뺀 값, 계차들을 항으로 하는 수열
    계차수열의 일반항을 알면 원래 수열의 일반항을 알 수 있음, 차분(미분의 이산)"""
    if isinstance(b, int):
        raise TypeError("b는 계차항을 원소로 하는 리스트 또는 배열로 정수가 아닌 유효한 값을 입력해주세요.")

    result = a
    # 초기값으로 초항 설정

    for i in range(n-1):
        result += b[i]
    # ai번째 항은 초항에 계차수열 b1에서 b_(i-1)까지 더한 값
    return result
    

# 급수 : 등차수열의 합, 등비수열의 합

def inputSeries(a: float, n: int, sequence_type: str, sequence_pattern: float):
    """수열의 각 항의 합을 일컫는 급수
    Sn = \Sigma_{k=1}^{n}(=∑)a_k
    Q1. 그런데 만약 sequence_pattern이 주어지지 않고, 
        a가 각 항을 원소로 하는 리스트로 주어진다면 어떻게 급수를 구할지
    A1. 등비수열은 공비 없이 급수 계산은 어려움
    Q2. 미리 정의한 arithmeticSequence(), geometricSequence()를 이용하려면"""
    if sequence_type == "arithmetic": 
        d = sequence_pattern
        return n*(2*a + (n-1)*d) / 2

    elif sequence_type == "geometric":
        r = sequence_pattern
        if r == 1:
            return a*n
        return a*(1-r**n) / (1-r)

    else:
        raise ValueError(
            "유효한 수열 타입 'arithmetic(등차)' 또는 'geometric(등비)'을 입력하세요.")
    

def methodSeries(a: float, n: int, sequence_type: str, sequence_pattern: float):
    """arithmeticSequence()와 geometricSequence()를 활용한 급수 계산 메서드
    더 나아가 함수를 좀 더 구조적으로 호출하기 위해 누적합 계산 로직을 데코레이터로 감싸서 추가적인 기능을 부여
    
    실제로는 데코레이터가 각 항을 누적하여 반환함
    이로 인해 decoratorSeries함수의 결과값과 methodSeries의 결과값이 동일하지 않다는 점
    # Trial & Error
    if sequence_type == "arithmetic":    
        for i in range(1, n+1):
            totalsum += arithmeticSequence(a, sequence_pattern, i)
        return totalsum

    elif sequence_type == "geometric":
        for i in range(1, n+1):
            totalsum += geometricSequence(a, sequence_pattern, i)
        return totalsum   
    """
    if sequence_type == "arithmetic":
        return sum(arithmeticSequence(a, sequence_pattern, i) for i in range(1, n+1))
    elif sequence_type == "geometric":
        return sum(geometricSequence(a, sequence_pattern, i) for i in range(1, n+1))
    else:
        raise ValueError("유효한 수열 타입 'arithmetic(등차)' 또는 'geometric(등비)'을 입력하세요.")

def decoratorSeries(a: float, n: int, sequence_type: str, sequence_pattern: float):
    """데코레이터를 사용하여 수열의 총합을 계산"""
    if sequence_type == "arithmetic":
        return arithmeticSequence(a, sequence_pattern, n)
    elif sequence_type == "geometric":
        return geometricSequence(a, sequence_pattern, n)
    else:
        raise ValueError("유효한 수열 타입 'arithmetic(등차)' 또는 'geometric(등비)'을 입력하세요.")