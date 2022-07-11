n = int(input())
if n%2 != 0 & 1 <= n <= 100:
    print("Weird")
elif n%2 == 0 & 2 <= n <= 5:
    print("Not Weird")
elif n%2 == 0 & 6 <= n <= 20:
    print("Weird")
elif n%2 == 0 & 20<n<=100:
    print("Not Weird")
else:
    print("enter a number between 1 and 100 : ")