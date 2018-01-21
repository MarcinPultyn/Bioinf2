from math import *

def GetProbabilitiesMatrix(a, b, t):
    x = 1/4.0 + 1/4.0 * exp(-4*b*t) + 1/2.0 * exp(-2 * (a+b) * t)
    y = 1/4.0 + 1/4.0 * exp(-4*b*t) - 1/2.0 * exp(-2 * (a+b) * t)
    z = 1/4.0 + 1/4.0 * exp(-4*b*t) 
    p = x
    q = y
    r = z
    matrix = [[p, q, r, r], [q, p, r, r], [r, r, p, q], [r, r, q, p]]
    return matrix

a = 0.04
b = 0.02

t = 1

GetProbabilitiesMatrix(a, b, t)

letters = ["A", "C", "G", "T"]

seq1 = "AGCCTGAACCGTT"
seq2 = "GCATAAGGTTCCA"

timePeriodStart = 1
timePeriodEnd = 20
timePeriodLength = timePeriodEnd - timePeriodStart

probabilities = []

for i in range(timePeriodStart, timePeriodEnd):
    matrix = GetProbabilitiesMatrix(a, b, i)
    probabilityTemp = 1
    for j in range(0, len(seq1)):
        x = letters.index(seq1[j])
        y = letters.index(seq2[j])
        probabilityTemp *= matrix[x][y]
    probabilities.append(probabilityTemp)

maxProbability = max(probabilities)
maxProbIndex = probabilities.index(maxProbability)
maxProbTime = maxProbIndex + timePeriodStart

print("Most probable time of evolution: ", maxProbTime)
print("Probability: ", maxProbability)