#printing all even numbers of input numbers
begnumb = int(input("write first number "))
finnumb = int(input("write final number "))
print("Even numbers between", begnumb, "and", finnumb, "are:")
for i in range(begnumb, finnumb + 1):
    if i%2 == 0:
     print(i)

