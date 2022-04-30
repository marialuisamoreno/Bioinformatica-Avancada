print("Conditions and Loops")
a = input("a = ")
b = input("b = ")
resp = 0

for i in range(int(a), int(b) + 1):
  if i % 2 == 1:
    resp += i

print(resp)