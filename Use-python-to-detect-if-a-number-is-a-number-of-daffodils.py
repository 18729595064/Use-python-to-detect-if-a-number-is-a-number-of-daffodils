def fun1(a):
    b = []
    c = str(a)
    for i in c:
        b.append(int(i))
    c = 0
    d = len(b)
    for j in b:
        c += (j**d)
    if c == a:
        print ("yes")
    else:
        print("no")
while True:
    b = input ("Would you like to try?(please input y/n): \n")
    if b == "n":
        break
    else:
        print("\n")
    a = input("please input a number: \n")
    fun1(int(a))

