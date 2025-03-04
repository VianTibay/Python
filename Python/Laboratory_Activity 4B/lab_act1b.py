'''
output 1 
'''

A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'd', 'f', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

A_and_B = A & B
print("Elements in A and B:", A_and_B, "Count:", len(A_and_B))

B_only = B - (A | C)
print("Elements in B only:", B_only, "Count:", len(B_only))

set_1 = C - (A | B)
set_2 = (A & B) | (A & C)
set_3 = (B & A) | (B & C)
set_4 = (A & B) - C
set_5 = A & B & C
set_6 = B - (A | C)

print("Set i:", set_1)
print("Set ii:", set_2)
print("Set iii:", set_3)
print("Set iv:", set_4)
print("Set v:", set_5)
print("Set vi:", set_6)
