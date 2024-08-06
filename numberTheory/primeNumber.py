def theNthPrimeNumber(n):
    sieve = [True]*1000000
    # 충분히 큰 크기(1000000 정도)를 가진 리스트를 생성
    sieve[0] = sieve[1] = False
    m = int(1000000**0.5)

    for i in range(2, m+1):
    # 2의 배수는 2*2부터 2*10까지 지우기
    # 3의 배수는 3*2는 이미 지웠으므로 3*3부터 3*10지우기
    # 5의 배수는 5*2 ~ 5*4는 이미 지웠으므로 5*5부터 5*10까지 지우기
        if sieve[i] == True:
            for j in range(i*i, 1000000, i):
                sieve[j] = False
        prime_list = []
        for i in range(0, n):
            if sieve[i] == True:
                prime_list.append(i)
        prime_list = [i for i in range(1000000) if sieve[i]]
        # 소수 리스트를 생성하는 리스트 컴프리핸션
        return prime_list[n-1]
        # 에라토스테네스의 체를 사용해 n번째의 소수를 찾아 반환

def mersennePrimes(n):
    """메르센 소수는 2의 n제곱-1의 형태로 n이 소수일 경우에만 소수가 될 수 있는 수"""
    from numberTheory import modularArithmetic
    if not modularArithmetic(n):
        return False
    mersenne_number = 2**n - 1
    return modularArithmetic(mersenne_number)

def sumOfPrimeNumbers(n):
    pass

def isEfficientPrimeNumber(n):
    pass
