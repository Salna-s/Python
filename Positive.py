arr = []

n = int(input("Enter Number of Element"))

for i in range(0, n):
    ele = int(input())

    arr.append(ele)

for num in arr:
    if num >= 0:
        print(num, end= " ")
