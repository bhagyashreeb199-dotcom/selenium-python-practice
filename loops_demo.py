greeting = "Its Morning"

if greeting == "Its Morning":
    print("It is a match")
else:
    print("Conditional doesn't match")


#With Value

a = 0
if a > 2:
    print("Right")
else:
    print("Wrong")


#adding value in run time

runtime_dict = {}

runtime_dict[1] = "One"
runtime_dict["second"] = 2
runtime_dict["Three"] = "Three"

print(runtime_dict)
print(runtime_dict[1])


#loops

obj = [1,2,3,4,5]
for i in obj:
    print(i*2)

print("sum of  natural numbers")
s = 0
for j in range(1,6):
    s = s + j
print(s)


print("********************")
for k in range(1,10, 5):
    print(k)


print("************* WHILEEEEEE LOOOOOOP ***********")


c = 4
while c > 1:
    print(c)
    c = c - 1
#print(c)

print("******************")

c = 4
while c > 1:
    if c !=3:
        print(c)
    c = c - 1
print("its done")


print("******************")

d = 10
while d > 1:
    if d == 3:
        break
    print(d)
    d = d - 1








