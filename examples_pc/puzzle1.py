###Write a Python function that takes a sequence of numbers and determines 
###whether all the numbers are different from each other


a=input("Enter comma seperated Integers:::")
print(a)
numbers=a.split(",")
numbers= [ int(i) for i in numbers]
##print(numbers)
### finding the length of numbers list
len_numbers=len(numbers)
print("Length of Numbers :::",len_numbers)
s=set(numbers)
print(len(s))    
if(len_numbers==s):
    print("Numbers are same")
else:
    print("Numbers are not same")   