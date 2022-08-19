import operators #using general form
print(operators.addOperator(3,6))
print(operators.divideOperator(9,3))

from operators import addOperator  #importing from specific functions
print(addOperator(5,7))
from operators import divideOperator
print(divideOperator(12,4))

from operators import addOperator as add #importing as alias
print(add(6,8))