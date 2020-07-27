def LCS(S1, S2):
    if 0 == len(S1) or 0 ==len(S2):
        return 0
    elif S1[0]==S2[0]:
        return 1 + LCS(S1[1:], S2[1:])
    else:
        return max(LCS(S1[1:], S2[1:]))
    if not S1 or not S2:
        return 0
    else:
        head1, tail1 = S1[0], S1[1:]
        head2, tail2 = S2[0], S2[1:]

    if head1 == head 2:
        return 1 + LCS(tail1, tail2)
    else:
        return max(LCS(tail1, S2), LCS(S1, tail2))
