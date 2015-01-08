import sys
import random
sys.path.append("../lib/")

#S = {x: {y: (1 if x==y else 0) for y in "ACGT"} for x in "ACGT"}

def SmithWaterman(seq1, seq2, S, gap):
    r = len(seq1) #rows
    c = len(seq2) #cols
    
    maxX = 0
    maxY = 0
    curMax = 0
    
    M = [[0] + [0 for i in seq2] for j in seq1] + [ [0]*(c+1) ]
    
    for j in range(c+1):
        M[0][j] = 0
    for i in range(1,r+1):
        M[i][0] = 0
        for j in range(1,c+1):
            t1 = M[i-1][j-1] + S[seq1[i-1]][seq2[j-1]]
            if not t1 >= 0:
                t1 = 0
            t2 = M[i-1][j] -gap
            if not t2 >= 0:
                t2 = 0
            t3 = M[i][j-1] -gap
            if not t2 >= 0:
                t3 = 0
            M[i][j] = max(t1, t2, t3)
            if M[i][j] > curMax:
                curMax = M[i][j]
                maxX = i
                maxY = j
   
    optimal = curMax
    
    #print(M)
    
    #A1 = seq1
    #A2 = seq2    
    A1 = ""
    A2 = ""
    seq1 = " "+seq1
    seq2 = " "+seq2
    i = 0

    r = maxX
    c = maxY
   #Creating alignments############################################################################################################ 
    while r > 0 or c > 0:         
        curScore = M[r][c]
        if curScore == 0:
            break
        
        if r > 0 and c > 0: #Can test for diagonal up to the left (one row, one column)
            diag = M[r-1][c-1]
            if curScore == diag + S[seq1[r]][seq2[c]]:
                A1 += seq1[r]
                A2 += seq2[c]
                r -= 1
                c -= 1
                continue
        
        if r > 0:   #Can test for moving up (one row)
            up = M[r-1][c]
            if curScore == up - gap:
                A1 += seq1[r]
                r -= 1
                A2 += "-"
                continue
                
        if c > 0:   #Can test for moving to the left (one column)
            left = M[r][c-1]
            if curScore == left - gap:
                A1 += "-"
                A2 += seq2[c]
                c -= 1
                continue
            
    A1 = A1[::-1]
    A2 = A2[::-1]
    
    #print(A1)
    #print(A2)
    
    output = (optimal, A1, A2)
    return output       