# 1.1
print('krishna')
print('krishna')
print('krishna')

# 2.1
a = 1
b = 2
c = 3
d = a+b+c
print(d)

# 2.2
a = "st"
b = "ri"
c = "ng"
d = a+b+c
print(d)

# 4.1
for i in range(1,11):
  print(7,"*",i,"=",i*7)
for i in range(1,11):
  print(9,"*",i,"=",i*9)

# 4.2
n = int(input("Enter No: "))
for i in range(1,11):
  print(n,"*",i,"=",i*n)

# 4.3
n = int(input("Enter No: "))
s = 0
for i in range(1,n+1):
  s=s+i
print("sum is",s)

# 5.1
a = int(input("Enter No 1: "))
b = int(input("Enter No 2: "))
c = int(input("Enter No 3: "))
d = max(a,b,c)
print(d)

# 5.2
n = int(input("Enter No: "))
sum=0
for i in range(1,n+1):
  if i%7==0 and i%9==0:
    sum+=i
print(sum)

# 5.3
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
n = int(input("Enter the value of n: "))
sum = 0
for i in range(1, n + 1):
    if is_prime(i):
        sum += i
print(sum)

# 6.1
def sum_oddnumbers(n):
    sum = 0
    for i in range(1, n + 1, 2):
        sum += i
    return sum
n = int(input("Enter the value of n: "))
res = sum_oddnumbers(n)
print(res)

# 6.2
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def sum_primenumbers(n):
    sum = 0
    for i in range(1, n + 1):
        if is_prime(i):
            sum += i
    return sum
n = int(input("Enter the value of n: "))
result = sum_primenumbers(n)
print(result)
