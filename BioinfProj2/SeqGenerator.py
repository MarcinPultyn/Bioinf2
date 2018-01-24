from math import *
import random
import numpy as np

def getProbabilitiesMatrix1(a, b, t):
    x = 1/4.0 + 1/4.0 * exp(-4*b*t) + 1/2.0 * exp(-2 * (a+b) * t)
    y = 1/4.0 + 1/4.0 * exp(-4*b*t) - 1/2.0 * exp(-2 * (a+b) * t)
    z = 1/4.0 + 1/4.0 * exp(-4*b*t) 
    p = x
    q = y
    r = z
    matrix = [[p, q, r, r], [q, p, r, r], [r, r, p, q], [r, r, q, p]]
    print ('Prob matrix: ')
    print (matrix)
    return matrix

def getRMatrix(a, b):
    r = (-2*b)-a
    matrix = [[r, b, a, b], [b, r, b, a], [a, b, r, b], [b, a, b, r]]
    print ("R matrix: ")
    print (matrix)
    return matrix

def getProbabilitiesMatrix(a, b, t):
    st = 1/4.0 * (1 - exp(-4*b*t))
    ut = 1/4.0 * (1 + exp(-4*b*t) - 2*exp(-2*(a+b)*t))
    rt = 1 - 2*st - ut
    
    matrix = [[rt, st, ut, st], [st, rt, st, ut], [ut, st, rt, st], [st, ut, st, rt]]
    print ("Prob matrix1: ")
    print (matrix)
    return matrix

def randomDnaSequence(length, actg_distribution=None):
    if (actg_distribution == None):
        actg_distribution = ''.join(random.choice('CGTA') for _x in range(7))
    return ''.join(random.choice(actg_distribution) for _x in range(length))

def getColName(colIndx):
    if colIndx == 0:
        return "A"
    elif colIndx == 1:
        return "C"
    elif colIndx == 2:
        return "G"
    elif colIndx == 3:
        return "T"
    return "-"
        
def getMutation(x, probList):
    val = probList[0]
    for i in range(1, len(probList) + 1):
        if x <= val:
            #print ("i: %d, x: %.4f, val: %.4f" % (i,x,val) )
            return getColName(i-1)
        val += probList[i]
    #print ("i: %d, x: %.4f, val: %.4f" % (i,x,val) )

def mutateSequence(seq, probMatrix):

    random.seed()
    for i in range(0, len(seq)):
        x = random.random()
        if seq[i] == "A":
            seq[i] = getMutation(x, probMatrix[0])
        elif seq[i] == "C":
            seq[i] = getMutation(x, probMatrix[1])
        elif seq[i] == "G":
            seq[i] = getMutation(x, probMatrix[2])
        elif seq[i] == "T":
            seq[i] = getMutation(x, probMatrix[3])
        
        
    return seq
    
a = 0.04
b = 0.02
seqLength = 25

t = int(input("Podaj czas t "))
seq = randomDnaSequence(seqLength)
originalSeq = list(seq)
seqCopy = list(seq)
print ("\n oryg seq: ")
print (seq)

rateMatrix = getRMatrix(a, b)
getProbabilitiesMatrix1(a, b, t)
probMatrix = getProbabilitiesMatrix(a, b, t)
mutatedSeq = mutateSequence(seqCopy, probMatrix)
print ("out seq: ")
print (''.join(mutatedSeq))

file = open("seq1.txt","w") 
file.write(''.join(originalSeq)) 
file.close()

file = open("seq2.txt","w")  
file.write(''.join(mutatedSeq)) 
file.close()

a = np.array(rateMatrix)
mat = np.matrix(a)
print (mat)
with open('rateMatrix.txt','wb') as f:
    for line in mat:
        np.savetxt(f, line, fmt='%.8f')
 
#reading matrix 
#input = np.loadtxt("rateMatrix.txt", dtype='f', delimiter=' ')
#print(input)
        
