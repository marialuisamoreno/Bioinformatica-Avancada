print("The Secondary and Tertiary Structures of DNA")
dna = input("dna = ")
reverso = ''
for i in range(0, len(dna)):
  if dna[i] == 'A': reverso += 'T'
  if dna[i] == 'T': reverso += 'A'
  if dna[i] == 'C': reverso += 'G'
  if dna[i] == 'G': reverso += 'C'

print(reverso[::-1])