import sys
sys.path.append("C:/StudyMath/numberTheory/")
from numberTheory import isPrimeNumber, modularArithmetic, sieveOfEratosthenes

# 소수 판별법
prime_result = isPrimeNumber(5)
print(prime_result)

# 모듈러 연산: 합성수 판별
composite_result = modularArithmetic(121)
print(composite_result)

# n보다 작은 모든 소수를 구하는 에라토스테네스의 체 알고리즘
sieve_result = sieveOfEratosthenes(100)
print(sieve_result)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# 소인수분해
