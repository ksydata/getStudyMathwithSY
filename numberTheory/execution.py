import sys
sys.path.append("C:/StudyMath/numberTheory/")
from numberTheory import isPrimeNumber, modularArithmetic

# 소수 판별법
prime_result = isPrimeNumber(5)
print(prime_result)

# 모듈러 연산: 합성수 판별
composite_result = modularArithmetic(121)
print(composite_result)