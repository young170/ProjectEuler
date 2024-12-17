top_boundary = 1000
multiples_of_3_5 = set()

for n in range(1, top_boundary):
  if n % 3 == 0 or n % 5 == 0:
    multiples_of_3_5.add(n)

# print(len(multiples_of_3_5))
print(sum(multiples_of_3_5))
# print(multiples_of_3_5)