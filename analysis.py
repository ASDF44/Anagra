def GetNCBI(f_name):
    file = open(f_name, 'r')
    seq = ''
    for line in file:
        seq = seq + line
    return seq


def align(seq1, seq2):
    alignment = ''
    s1 = len(seq1)
    s2 = len(seq2)
    if s1 < s2:
        n = s1
    else:
        n = s2
    for i in range(n):
        if seq1[i] == seq2[i]:
            alignment += '*'
        else:
            alignment += '_'
    return alignment

def align_score(alignment):
    score = 0
    print(alignment)
    n = len(alignment)
    print('length: ',n)
    for char in alignment:
        if char == '*':
            score += 1
    score = (score/n)*100
    return score

"""
seq1 = GetNCBI('C:/Users/Saurabh/SDD/ncbi/barley.txt')
seq2 = GetNCBI('C:/Users/Saurabh/SDD/ncbi/rice.txt')
a = align(seq1, seq2)
s = align_score(a)
print(s)
"""