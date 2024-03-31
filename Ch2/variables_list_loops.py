l=25
###for printing use print statement
print("The Value of ls l ::"+ str(l))
print("The Value of ls l ::"+ str(l**2))
l+=l
print("Lets find this ::"+str(l))

for i in range(10):
    print("The loop in" +str(i))

l= ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

##Enumerate used in iteration.
for x,i in enumerate(l):
    print(str(x) +" "+str(i))

##While loop
x=5
while (x <=10):
    print("Inside while loop")
    x=x+1

###dictionary
d= {
    1:"Pavan",
    2:"Sudeep",
    3:"Sridhar",
    4:"Seenu"
   } 
print(d)
###How to get the value from the dictionary
print(d.get(1))
### you can also clear the dictionary
#d.clear()
#print(d)
####sets
s={1,2,3,4}
print(s)
print(2 in s)
s.add(5)
