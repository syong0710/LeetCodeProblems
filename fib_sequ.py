# Fib sequence, the input is the number

def fib(num:int):
    # The initialization
    if num==0:
        return 0
    if num==1:
        return 1

    # The change of status
    return fib(num-1) + fib(num-2)


n = 5
print("Fib seq: " + str(fib(n)))


