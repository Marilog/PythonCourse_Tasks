#first task Zen of Python
Zen_Python = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

#print(Zen_Python)

#print("The count of BETTER is ", Zen_Python.count("better"))
#print("The count of NEVER is ", Zen_Python.count("never") )
#print("The count of IS is ", Zen_Python.count("is"))
#print(Zen_Python.upper())
#print(Zen_Python.replace("i", "&"))

#second task

nat_number = 4386

#1.solution
#mult=1
#while(nat_number!=0):
 #   mult=mult*(nat_number%10)
  #  nat_number=nat_number//10
#print(mult)


#2.solution
number_to_list = [int(x) for x in str(nat_number)]
print(str(number_to_list))

def multiplyList(myList):
    result = 1
    for x in myList:
        result=result * x
    return result
print(multiplyList(number_to_list))

#3.solution
import numpy
mult_with_np = numpy.prod(number_to_list)
print(mult_with_np)

#import math
#mult_with_math = math.prod(number_to_list)
#print(mult_with_math) #for python 3.8


print(number_to_list[::-1])


sorted_list = sorted(number_to_list)
print(sorted_list)



#3.task

var_1 = 134
var_2 = 543243

var_1, var_2 = var_2, var_1

print("Swapped first variable is ", var_1)
print("Swapped second variable is ", var_2)
