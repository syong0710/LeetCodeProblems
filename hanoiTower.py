
# Tower of Hanoi: the recursive method
def hanoi_recursive(n:int, source:str, auxiliary:str, destination:str):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    hanoi_recursive(n-1, source, destination, auxiliary) # move the (n-1) smaller disk to the auxiliary
    print("Move disk", n, "from", source, "to", destination) # move the biggest one to destination
    hanoi_recursive(n-1, auxiliary, source, destination) #move the disks on the auxilary to the destiation


n = 4
# A:source; B:auxiliary; C:destination;
hanoi_recursive(n, 'A', 'B', 'C')

# The illustration of hanoi_recursive(4, 'A', 'B', 'C'):
# time complexity: 2^n-1 (2^4-1 = 15) 
#
#                                              (1, A, C, B) -- pint(move disk1 A->B)
#                                             /
#                                (2, A, B, C)----------------- print(move disk2 A->C)
#                              /              \
#                             /                (1, B, A, C) -- print(move disk1 B->C)
#                 (3, A, C, B)-------------------------------- print(move disk3 A->B)
#               /             \                (1, C, B, A) -- print(move disk1 C->A)
#              /               \             /
#             /                  (2, C, A, B)----------------- print(move disk2 C->B)
#            /                               \
#           /                                  (1, A, C, B) -- print(move disk1 A->B)
# (4, A, B, C) ----------------------------------------------- print(move disk4 A->C)
#           \                                  (1, B, A, C) -- print(move disk1 B->C)
#            \                                /
#             \                   (2, B, C, A)---------------- print(move disk2 B->A)
#              \                /             \
#               \              /               (1, C, B, A) -- print(move disk1 C->A)
#                 (3, B, A, C)-------------------------------- print(move disk3 B->C)
#                              \               (1, A, C, B) -- print(move disk1 A->B)
#                               \             /
#                                 (2, A, B, C) --------------- print(move disk2 A->C)
#                                             \
#                                              (1, B, A, C) -- print(move disk1 B->C)
#
