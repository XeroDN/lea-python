num=[5,6,3,2,1,7,8,9,2,0,2,5,3,4,5,6,7,8,9,10]
print(min(num))
print(max(num))
print(f"         the sum of total number is {sum(num)}".title().lstrip())
print(len(num))
for value in num:
    if value % 2 == 0:
        print(f"{value} is even")
    else:
        print(f"{value} is odd")

num=[value**3 for value in range(2,7)]
print(f"the final result is {num}".capitalize().strip())

num = []
for num in range(0,21):
    
    print(num)