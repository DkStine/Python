# Q1 
l = []

l.append('Abcd')
l.extend([1, 2, 3, 4, 2])
l.insert(1, 'efgh')
l.remove(1)
del l[2]
n = l.count(2)
i = l.index('efgh')
l.sort()

# Q2
tup = (1, 2, 3, 4, 5, 6, 2)
n = tup.count(2)
i = tup.index(3)
slice = tup[2 : 5]
print(n, i, slice)

# Q3
dic = {1 : 'D', 2 : 'E'}
for i in dic.items():
    print(i)

print(dic.keys())
print(dic.values())
print(dic.get(2))
print(dic.pop(1))

for i in dic.items():
    print(i)
dic.clear()

# Q4
def isPrime(n):
    for i in range(2, int(n * (1/2)) + 1):
        if n % i == 0:
            return False
        
    return True

num = 2

while num < 20:
    if isPrime(num):
        print(num)
    num += 1

# Q5
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
x = int(input("Enter the number: "))
if x < 0:
    print("Enter a positive integer")
else:
    print(factorial(x))

# Q6
a, b, c = map(int, input("Enter three sides: ").split())
hyp = max([a, b, c])
sumOfOtherSides = 0

for i in [a, b, c]:
    if i != hyp:
        sumOfOtherSides += i**2

if hyp ** 2 == sumOfOtherSides:
    print("Right triangle")
else:
    print("Not a right triangle")
