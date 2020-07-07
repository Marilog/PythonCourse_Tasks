#second task

nat_number = int(input("Insert four-digit natural number: "))

#1.solution
#mult=1
#while(nat_number!=0):
 #   mult=mult*(nat_number%10)
  #  nat_number=nat_number//10
#print(mult)


#2.solution
number_to_list = [int(x) for x in str(nat_number)]
def multiplyList(myList):
    result = 1
    for x in myList:
        result=result * x
    return result
print("The result of the digits multiplication is ", multiplyList(number_to_list))

#3.solution
import numpy
mult_with_np = numpy.prod(number_to_list)
print("The result of the digits multiplication is ", mult_with_np)


#4.solution - only for python version up 3.8
#import math
#mult_with_math = math.prod(number_to_list)
#print(mult_with_math) 

print("The reverse version of the list is ", number_to_list[::-1])


sorted_list = sorted(number_to_list)
print("The sorted version of the list is ",sorted_list)

