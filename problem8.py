print("Dictionaries")
s = input("s = ")

dic = {}
for word in s.split(' '):
  if word in dic: dic[word] += 1
  else: dic[word] = 1

for key, value in dic.items():
  print(key + " " + str(value))