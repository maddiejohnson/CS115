def myLength(L):
    return 0 if not L else 1 + myLength(L[1:])

def deepLength(L):
    if not L:
        return 0
    else:
        head, tail = L[0], L[1:]
        headContribution = deepLength(head) if isinstance(head, list) else 1
        return headContribution + deepLength(L[1:])
