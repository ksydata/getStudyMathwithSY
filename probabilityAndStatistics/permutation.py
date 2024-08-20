def RecursiveFactorial(n):
    """동명의 함수를 재호출하되 탈출 조건(base case)를 설정한 재귀함수를 활용한 팩토리얼
    O(N)"""
    return n*RecursiveFactorial(n-1) if n > 1 else 1

def MemorizationFactorial(n):
    """한 번 구한 값은 저장하여 같은 요청이 올 때 저장된 값 반환하는 동적계획법을 활용한 팩토리얼"""
    pass

def DecoratorFactorial(n):
    """데코레이터를 통한 동적계획법을 활용한 팩토리얼"""
    pass


def RecursivePermutation(n, r):
    """n개 중 r개를 뽑아 순서대로 나열하는 경우의 수
    nPr = n*(n-1)*(n-2)*...*(n-r+1) = n!//(n-r)!"""
    return RecursiveFactorial(n) // RecursiveFactorial(n-r)
    # math.factorial(n)

def MemorizationPermutation(n, r):
    """nPr 순열"""
    return MemorizationFactorial(n) // MemorizationFactorial(n-r)