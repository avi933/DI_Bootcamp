import numpy as np

lst = [2, 4, 6, 8, 13, 2020]
numpy_arr = np.array(lst)

#printing the minimum value
def min_value():
   print("\nThe minimum value is : ",numpy_arr.min())

#printing the max value
def max_value():
    print("The max value is : ",numpy_arr.max())

# finding the standard deviation of the array
def std():
    print("The standard deviation is: ",np.std(numpy_arr))

#The product of the elements in the array
def product():
    print("The product of the elements is: ",np.prod(numpy_arr))

# Dot product of the array to itself
def dot_pro():
    print("The dot product of the array: ",np.dot(numpy_arr,numpy_arr))

# An array with 4 subtracted from every element in the input array
def sub_four():
    print("The array with 4 subtract from it is: ",(numpy_arr -4),"\n")

min_value()
max_value()
std()
product()
dot_pro()
sub_four()

