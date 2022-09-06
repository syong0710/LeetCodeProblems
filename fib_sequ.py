
def fibSeq(n:int)->int:
    if n>2:
        return (fibSeq(n-1) + fibSeq(n-2))
    else:
        return n-1

print(fibSeq(6))


