from math import *
import random

def getProbabilitiesMatrix1(a, b, t):
    x = 1/4.0 + 1/4.0 * exp(-4*b*t) + 1/2.0 * exp(-2 * (a+b) * t)
    y = 1/4.0 + 1/4.0 * exp(-4*b*t) - 1/2.0 * exp(-2 * (a+b) * t)
    z = 1/4.0 + 1/4.0 * exp(-4*b*t) 
    p = x
    q = y
    r = z
    matrix = [[p, q, r, r], [q, p, r, r], [r, r, p, q], [r, r, q, p]]
    print ('Prob matrix: \n')
    print (matrix)
    return matrix

def getRMatrix(a, b):
    r = (-2*b)-a
    matrix = [[r, b, a, b], [b, r, b, a], [a, b, r, b], [b, a, b, r]]
    print ("R matrix: \n")
    print (matrix)
    return matrix

def getProbabilitiesMatrix(a, b, t):
    st = 1/4.0 * (1 - exp(-4*b*t))
    ut = 1/4.0 * (1 + exp(-4*b*t) - 2*exp(-2*(a+b)*t))
    rt = 1 - 2*st - ut
    
    matrix = [[rt, st, ut, st], [st, rt, st, ut], [ut, st, rt, st], [st, ut, st, rt]]
    print ("Prob matrix1: \n")
    print (matrix)
    return matrix

def randomDnaSequence(length, actg_distribution=None):
    if (actg_distribution == None):
        actg_distribution = ''.join(random.choice('cgta') for _x in range(7))
    return ''.join(random.choice(actg_distribution) for _x in range(length))

def getColName(colIndx):
    if colIndx == 0:
        return "a"
    elif colIndx == 1:
        return "c"
    elif colIndx == 2:
        return "g"
    elif colIndx == 3:
        return "t"
        
def getMutation(x, probList):
    val = probList[0]
    for i in range(1, len(probList)):
        if x < val:
            print ("i: %d, x: %.4f, val: %.4f" % (i,x,val) )
            return getColName(i-1)
        val += probList[i]

def mutateSequence(seq, probMatrix):
    for i in range(0, len(seq)):
        x = random.random()
        if seq[i] == "a":
            seq[i] = getMutation(x, probMatrix[0])
        elif seq[i] == "c":
            seq[i] = getMutation(x, probMatrix[1])
        elif seq[i] == "g":
            seq[i] = getMutation(x, probMatrix[2])
        elif seq[i] == "t":
            print (probMatrix[3])
            seq[i] = getMutation(x, probMatrix[3])
        
    return seq
    
a = 0.04
b = 0.02
seqLength = 25

t = int(input("Podaj czas t "))
seq = randomDnaSequence(seqLength)
seq1 = seq2 = list(seq)
print (seq)
print ("\n seq: \n")
print (seq1)
print ("\n")
print (seq1[0])
getRMatrix(a, b)
getProbabilitiesMatrix1(a, b, t)
probMatrix = getProbabilitiesMatrix(a, b, t)
retSeq1 = mutateSequence(seq1, probMatrix)
retSeq2 = mutateSequence(seq2, probMatrix)
print ("out seq: \n")
print (retSeq1)
print ("\n")
print (retSeq2)

file = open("seq1.txt","w") 
file.write(''.join(seq1)) 
file.close()

file = open("seq2.txt","w")  
file.write(''.join(seq2)) 
file.close()

file = open("matrix.txt","w") 
file.write(''.join(probMatrix))
file.close()

        
