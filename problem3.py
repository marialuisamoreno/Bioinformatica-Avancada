print("A Rapid Introduction to Molecular Biology")
dna = input("dna = ")

a = 0
c = 0
g = 0
t = 0

for i in range(0, len(dna)):
    if dna[i] == 'A': a+=1
    if dna[i] == 'C': c+=1
    if dna[i] == 'G': g+=1
    if dna[i] == 'T': t+=1

print(a, c, g, t)