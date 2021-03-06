def GetNCBI(crop):

    import mysql.connector
    connection = mysql.connector.connect(host='localhost',
                                         database='sdd',
                                         user='root',
                                         password='')



    sql_select_Query = "select * from crop where Name = " + "'" + crop  + "'"
    #  print(sql_select_Query)
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()


    for row in records:
        f_name = row[9]
    f_name = f_name + '.txt'
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
    n = len(alignment)
    for char in alignment:
        if char == '*':
            score += 1
    score = (score/n)*100
    return score

#crop1 = str(input('Enter crop1 of interest: '))
#crop2 = str(input('Enter crop2 of interest: '))
#seq1 = GetNCBI(crop1)
seq1 = """
>>AH001724.2 Pisum sativum 28S rRNA, complete sequence
GGTTGCACCGCCGACCGACCCTGATCTTTTGTGAAGGGTTCGAGTGAGAGCATACCTGTCGGGACCCNAA
AGATGGTGAACTATGCCTGAGCGGGGCGAAGCCAGAGGAAACTCTGGTGGAGGCCCGMAGCGATACTGAC
GTGCAAATCGTTCGTCTGACTTGGGTATAGGGGCGAAAGACTAATCGAACCGTCTAGTAGCNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNTGAACCGGGACGTGGTGGCTGACGGCAACGTTAGGGAGTCCGGAGACGT
TGGCGGGGGCCCCGGAAAGAGTTATCTTTTCTGTTTAACAGCCTGCCCACCCTGGAAANGCCTCAGCCGG
AGGTAGGGTCCAGCGGCTGGAAGAGCACCGCACGWCGCGTGGTGTCCGGTGCCCCTGGCGGCCCTTGAAA
ATCCGGAGGACNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNCTCTGAGGGCTGGGCACGGGGGTCCCAGT
TCCGAACCCGTCGGCTGTTGGTGGACTGCTCGAGCGTCTCNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
CGCGTGCCGGTCGGGNGACGGNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNTTCGGGGCCTCTTCCCCGG
GCATCGAACAGTCAACTCAGAACTGGTACGGACAAGGGGAATCCGACTGTTTAATTAAAACAAAGCATTG
CGATGGT
"""
#seq2 = GetNCBI(crop2)
seq2 = """
>U20809.1 Vigna radiata clone MII-4 auxin-induced protein mRNA, partial cds
GAATTAAAGTGCTTCGATGGGTTCAAGTCAGGAAGAAGTGACCCTTCTGGAATTATTGGAAGCCCATTTG
TTTGCAGGGTGAAGATAGCCCTGAAGTTGAAGGGAGTTGAATACAAATACGTTGAAGAAAATTTCCGCAA
CAAGAGTGAACAGCTTCTGAAATACAACCCAGTTCACAAGAAGGTTCCAGTGTTTGTTCATGGTGACAAA
CCCCTTCCAGAGTCCCTTGTGATTGTTGAGTACATCGATGAGACATGGAACAACAACCCCATCTTGGCTT
CTGATCCTTACCAGAGAGCCTTGGCTCGTTTCTGGTCCAAATTCATCGATGACAAGATTGTGGGTGCTTC
GTGGAAATCTGTTTTCACAGTTGATGAGAAAGAGCGTGAGAAGAATATTGCAGAAACATATGAGAGTCTG
CAGTTTCTTGAGAATGAGATAAAGGAGAAGAAGTTCTTTGGAGGAGAAGAGCTTGGGTTGGTAGATATTG
CTGCTGTCTATGTAGCATTTTGGATCCCTTTGATTCAAGAAATAGCAGGATTGGAGTTATTGACAAGTGA
GAAATTTCCTAATCTCTACAGGTGGAGCCAAGAATTTTTGAACCATCCAATTGTCAAAGAAAGTCTTCCC
CCTAGAGACCCAGTTTTTGCCTTTTTCAAAGGACGCTATGAAGGCCTTTTTTCTTCGAAATAGATTTCAT
GTTGTGAGAGATTTAGAATTTATAAGGAAAATTGTGTGGAGTACTTAGTTAGGATTTGGTTTCAAAATTA
TGGTTGAAGTTGAATCCTAGGATTTGCGCATGTCAAACAAATAACCTGGGATTGTTCGTGTTGATATTTT
ACTATTTCAATCAATAAATTATGCAGCTTCTTACCGAGTTAACATTCGATCGAAATAAGGACCAACAAGA
TTAAGTAAGGCTGCATTATTTGTCTTTTTGTTAAATTAGATATTAGTATGCACCAAAAAGTGAGTATTTC
CTTACAGAAGCTTTTTAAATATTAAGTAGTTAATTCCATAGGTCTACCATTATAGCTCAAGTTATATACA
TATTATGGGTGCCATTCTCTACTCAACAATTATGACTATAAAATCTTGTGGTTATAATGCCACGAACAAG
TGAACTATCTCACTTCA
"""
alignment = align(seq1, seq2)
score = align_score(alignment)
print(alignment)
print(score)