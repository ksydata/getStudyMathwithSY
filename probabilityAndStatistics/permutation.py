from typing import *

def RecursiveFactorial(n):
    """동명의 함수를 재호출하되 탈출 조건(base case)를 설정한 재귀함수를 활용한 팩토리얼
    O(N)"""
    return n*RecursiveFactorial(n-1) if n > 1 else 1

def MemorizationFactorial(n):
    """한 번 구한 값은 저장하여 같은 요청이 올 때 저장된 값 반환하는 동적계획법을 활용한 팩토리얼"""
    global cache_
    # 전역 변수에 캐시로 쓸 dictionary 선언

    if n in cache_: 
        return cache_[n]
        # n에 해당하는 key에 n!값을 value로 저장
    elif n <= 1:
        return 1
    else:
        cache_[n] = n*MemorizationFactorial(n-1)
        return cache_[n]
        # 재귀함수로 반복문보다 빠르게 곱셈 연산 수행
    
    return n*MemorizationFactorial(n-1) if n > 1 else 1
    # 단, else문 코드의 중복

def cache(function):
    """user function을 받아 wrapper로 감싼 후 결과값을 돌려주는 데코레이터
    name space을 활용"""
    cache_: Dict = {}

    def wrapper(n):
        if n in cache_:
            return cache_[n]
        else:
            cache_[n] = function(n)
            return cache_[n]
    
    return wrapper

@cache
def DecoratorFactorial(n):
    """데코레이터를 통한 동적계획법을 활용한 팩토리얼"""
    return n*DecoratorFactorial(n-1) if n > 1 else 1


def RecursivePermutation(n, r):
    """n개 중 r개를 뽑아 순서대로 나열하는 경우의 수
    nPr = n*(n-1)*(n-2)*...*(n-r+1) = n!//(n-r)!"""
    return RecursiveFactorial(n) // RecursiveFactorial(n-r)
    # math.factorial(n)

def MemorizationPermutation(n, r):
    """동적 계획법을 통한 nPr 순열"""
    return MemorizationFactorial(n) // MemorizationFactorial(n-r)

def DecoratorPermutation(n, r):
    """데코레이터를 통한 nPr 순열"""
    return DecoratorFactorial(n) // DecoratorFactorial(n-r)

