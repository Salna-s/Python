n = int(input("How Many Terms ?"))
num1, num2 = 0, 1
count = 0

if n <= 0 :
    print("Please enter a Positive Intiger")
elif n == 1 :
    print("Fibonacci Sequence upto", n, ":")
    print(num1)
else :
    print("Fibonacci Sequence : ")
    while count < n :
        print(num1)
        nth = num1 + num2
        num1 = num2
        num2 = nth
        count += 1
