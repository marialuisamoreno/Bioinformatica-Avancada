print("Finding a Motif in DNA")
s = input("s = ")
a = input("a = ")

index = []

for i in range(len(s)):
  result = s[i:].find(a)
  if result == -1: break
  else:
    result = result + i + 1
    if result not in index: index.append(result)

print(*index)