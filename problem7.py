print("Working with Files")
f1 = open('entrada/problem7.txt', 'r')
f2 = open('saida/problem7.txt', 'w')

i = 0
for line in f1:
  if i % 2 == 1: f2.write(line)
  i += 1