def fibNumber(num:int) -> int:
    if num>=2:
        return fibNumber(num-1) + fibNumber(num-2)
    elif num ==1: return 1
    elif num == 0: return 0


n = 5
print("the" + str(n) + "th number of Fibonacci Seq is " + str(fibNumber(n)))
