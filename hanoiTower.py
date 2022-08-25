
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
