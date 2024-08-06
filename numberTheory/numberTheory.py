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


def modularArithmetic(x):
    """소수와 합성수(약수의 개수가 세 개 이상인 수) 판별하는 모듈러 연산 x % y 수행 후 나머지 반환"""
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


def sieveOfEratosthenes(n):
    """10,000보다 작은 모든 소수를 구하는 에라토스테네스의 체 알고리즘"""
    sieve = [True]*n
    # 찾고자 하는 범위의 자연수 나열
    # (True는 소수, False는 합성수)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
    # 2~n의 제곱근까지 루프
        if sieve[i]:
        # i가 소수인 경우(True 생략) i의 배수를 False로 변경
            for j in range(i * i, n, i):
                # i의 배수는 False로 변경
                # 2부터 시작해 2의 배수 소거
                # 다음 소수의 배수(3, 5, ...) 소거
                sieve[j] = False
        # i자체는 소수이므로 True를 유지
                
    result = []
    for i in range(0, n):
        if sieve[i] == True :
        # 소수인 i값만 반환
            result.append(i)
    return result    


def primeFactorization(n):
    """소인수분해: 소수(바탕이 되는 수)들의 곱으로만 나타낸 수"""
    primes_list = sieveOfEratosthenes(n+1)
    # 규칙은 가장 작은 소수로 나누고 더 이상 2로 못 나누면 다음 큰 3으로 나누고... 
    # n자체가 소수일 수 있다는 점에서 n+1

    index = 0
    # primes_list의 각 소수에 대한 인덱스 번호
    result = []

    while index < len(primes_list):
        if n % primes_list[index] == 0:
        # 작은 소수부터 n을 나누어보아서 소인수
            result.append(primes_list[index])
            # 현재 소수 n을 결과값 리스트에 원소로 추가
            n = n // primes_list[index]
            # n을 현재 소수로 나누어 갱신(기존 n을 제거)
        else:
            index += 1

    return result

