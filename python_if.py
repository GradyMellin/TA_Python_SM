


num1=14
key = True

if num1 == 12:
    if key:
        print("yay")
elif num1 > 12:
    if key:
        print(isinstance(num1,int))

else:
    print("not yay")


i = 0

while i < 10:
    print("{} is a great number!".format(i))
    i += 1
    if i== 3:
        continue
    print("nice")
    
else:
    print("I'm tired goodnight")
    
i = 0

for i in range(10):
    print("{} is a great number!".format(i))
    i+=1
    
