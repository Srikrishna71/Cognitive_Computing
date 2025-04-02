#Q1 (i)
L=[10,20,30,40,50,60,70,80]
L.append(200)
L.append(300)
print(L)
# (ii)
L.remove(10)
L.remove(30)
print(L)
# (iii)
L.sort()
print(L)
# (iv)
L.sort(reverse=True)
print(L)

#Q2
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
# (i)
high_score=max(scores)
print(high_score)
high_index = scores.index(high_score)
print(high_index)
# (ii)
lowest_score = min(scores)
print(lowest_score)
lowest_count = scores.count(lowest_score)
print(lowest_count)
# (iii)
reversed_scores = list(scores[::-1])
print(reversed_scores)
# (iv)
user_score=int(input('Enter a score: ')) #76 can be input
if user_score in scores:
    first_index = scores.index(user_score)
    print(f"{user_score} found at index {first_index}")
else:
    print(f"{user_score} is not present.")

#Q3 (i)
import random
l=[random.randint(100,900) for i in range(100)]
odd_numbers = [num for num in l if num % 2 == 1]
print(odd_numbers)
#(ii)
even_numbers = [num for num in li if num % 2 == 0]
print(even_numbers)
#(iii)
prime_numbers=[]
for num in l:
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            prime_numbers.append(num)
print(prime_numbers)

#Q4 (i)
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}
unique_scores = A | B
print(unique_scores)
# (ii)
common_scores = A & B
print(common_scores)
# (iii)
exclusive_scores = A ^ B
print(exclusive_scores)
# (iv)
A_sub= A.issubset(B)
B_sup= B.issuperset(A)
print(A_sub)
print(B_sup)  
# (v)
user_score=int(input('Enter the score to remove it:'))
if user_score in A:
    A.remove(user_score)
    print(f"Removed {user_score} from set A.")
else:
    print(f"{user_score} is not present in set A.")
print(A)

#Q5 (i)
data = {"name":"kelly","age":25,"salary":8000,"city": "New York"} 
if "city" in data:
    data["location"] = data.pop("city")
print("Final Dictionary:", data)
