for i in range(10):
    print(i)

for i in range(1, 6):
    print(i * 2)

for i in range(10, 0, -1):
    print(i)

sum = 0
for i in range(1, 101):
    sum += i
print(sum)

word = "Python"
for i in range(len(word)):
    print(word[i])
    
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
