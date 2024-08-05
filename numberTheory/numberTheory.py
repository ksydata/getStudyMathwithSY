def isPrimeNumber(n):
    """정수론: 소수 판별법"""
    if n <= 1:
    # n이 1보다 작은 경우, False를 반환
        return False
    for i in range(2, n):
        if n % i == 0:
        # n이 합성수이면, False를 반환(2 ~ n-1로 나누어 떨어질 때)
            return False
    # n이 소수면, True를 반환
    return True

# print(isPrimeNumber(n = 5))

def modularArithmetic(x):
    """소수와 합성수 판별하는 모듈러 연산 x % y 수행 후 나머지 반환"""
    if x <= 1:
            return False
            # 0과 1은 소수와 합성수 둘다 해당하지 아니함
    if x <= 3:
    # prime number
            return True
            # 2~(x-1)까지 나누어 떨어지지 않으면, 소수
    if x % 2 == 0 or x % 3 == 0:
    # composite_number
            return False
            # 자기보다 작은 자연수의 곱이 하나라도 존재하는지
            # 2~(n-1)까지 나누어 떨어지면, 합성수
    
    i = 5
    while i * i <= x:
    # i를 5로 설정 후 6씩 루프마다 증가시켜 i와 i+2로 나누어 떨어지는지 확인
          if x % i == 0 or x % (i+2) == 0:
                return False
          i += 6
    return True

# print(modularArithmetic(x = 121))