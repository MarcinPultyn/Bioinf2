from math import *
import numpy as np
from decimal import Decimal

letters = ["A", "C", "G", "T"]

def kimuraDistance(st, ut):
    p=ut
    q=2*st
    d = Decimal(1-(2*p)-q)
    d1 = Decimal(1-(2*q))
    dd = d.ln()
    dd1 = d1.ln()
    return ((-(float(dd))/2)-((float(dd1))/4))
   

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

def GetProbabilitiesMatrix(a, b, t):
    x = 1/4.0 + 1/4.0 * exp(-4*b*t) + 1/2.0 * exp(-2 * (a+b) * t)
    y = 1/4.0 + 1/4.0 * exp(-4*b*t) - 1/2.0 * exp(-2 * (a+b) * t)
    z = 1/4.0 + 1/4.0 * exp(-4*b*t) 
    p = x
    q = y
    r = z
    matrix = [[p, q, r, r], [q, p, r, r], [r, r, p, q], [r, r, q, p]]
    return matrix

def FindMostProbableEvolutionTime(seq1, seq2, alfa, beta, timePeriodStart, timePeriodEnd, timePeriodInterval):
    probabilities = []

    for i in my_range(timePeriodStart, timePeriodEnd, timePeriodInterval):
        matrix = GetProbabilitiesMatrix(a, b, i)
        probabilityTemp = 1
        for j in range(0, len(seq1)):
            x = letters.index(seq1[j])
            y = letters.index(seq2[j])
            probabilityTemp *= matrix[x][y]
        probabilities.append(probabilityTemp)

    maxProbability = max(probabilities)
    maxProbIndex = probabilities.index(maxProbability)
    maxProbTime = maxProbIndex * timePeriodInterval + timePeriodStart

    print("Najbardziej prawdopodobny czas ewolucji: ", maxProbTime)
    print("Prawdopodobieństwo: ", maxProbability)

fileName = input("Podaj nazwę pliku z pierwszą sekwencją ")
fo = open(fileName, "r+")
seq1 = fo.read();
fo.close()
fileName = input("Podaj nazwę pliku z drugą sekwencją ")
fo = open(fileName, "r+")
seq2 = fo.read();
fo.close()

#fileName = input("Podaj nazwę pliku z macierzą częstości ")
#fo = open(fileName, "r+")
#rateMatrix = fo.read();
#fo.close()

timePeriodStart = int(input("Podaj początek przedziału czasu "))
timePeriodEnd = int(input("Podaj koniec przedziału czasu "))
timePeriodInterval = float(input("Podaj wielkość odcinków czasu "))

a = 0.04
b = 0.02

#seq1 = "AGCCTGAACCGTT"
#seq2 = "GCATAAGGTTCCA"

#timePeriodStart = 1
#timePeriodEnd = 20
#timePeriodLength = timePeriodEnd - timePeriodStart
#timePeriodInterval = 0.1

FindMostProbableEvolutionTime(seq1, seq2, a, b, timePeriodStart, timePeriodEnd, timePeriodInterval)

input = np.loadtxt("probMatrix.txt", dtype='f', delimiter=' ')
st = input[0][1]
ut = input[0][2]
print ("st %f , ut %f" % (st, ut))
kimD = kimuraDistance(st, ut)
print ("Kimura Distance: ", kimD)
t = kimD/(a+2*b)
print ("time: ", t)
