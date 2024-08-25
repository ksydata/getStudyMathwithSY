import sys
sys.path.append("C:/StudyMath/sequenceOfNumber/")
from numericalSequence import *


diffsequence_result = differenceSequence(a = 0, 
                                         b = [3, 5, 7, 9, 11, 13, 15],
                                         n = 6)
print(diffsequence_result)
# {a_n} = {0, 3, 8, 15, 24, 35, 48, 63, ...}
# C:/StudyMath/sequenceOfNumber/execution.py > 35


inputseries_result = inputSeries(a = 1, 
                                 n = 3,
                                 sequence_type = "geometric", 
                                 sequence_pattern = 2)
print(inputseries_result)
# C:/StudyMath/sequenceOfNumber/execution.py > 7.0
# {a_n} = {1, 3, 5, 7, 9, 11, 13, 15...}


# 실제로는 데코레이터가 각 항을 누적하여 반환함
# 이로 인해 decoratorSeries함수의 결과값과 methodSeries의 결과값이 동일하지 않다는 점

methodseries_result = methodSeries(a = 1, 
                                   n = 3,
                                   sequence_type = "geometric", 
                                   sequence_pattern = 2)
print(methodseries_result)


decoratorseries_result = decoratorSeries(a = 1, 
                                         n = 3,
                                         sequence_type = "geometric", 
                                         sequence_pattern = 2)
print(decoratorseries_result)