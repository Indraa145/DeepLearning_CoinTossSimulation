import numpy as np
import matplotlib.pyplot as plt

#Indra Imanuel Gunawan - 20195118
#Deep Learning Homework 1 | No. 9

def countPatternInSequence(pattern, sequence):
    count = 0
    for i in range(len(sequence) - len(pattern) + 1):
        if sequence[i:i + len(pattern)] == pattern:
            count += 1
    return count

numOfSimulation = input("Enter number of times you want the simulation be performed:")
numOfToss = input("Enter number of times the coin will be tossed:")
numHTHs = []
numHTTs = []
firstOccurrencePosHTHs = []
firstOccurrencePosHTTs = []

for j in range(int(numOfSimulation)):
    tossResults = ""
    for i in range(int(numOfToss)):
        #1: Head, 0: Tail
        tossResult = np.random.randint(0,2)
        tossResults += str(tossResult)

    print("")
    print("Simulation " + str(j+1) + " results :")
    print("Toss results:")
    print(tossResults)

    #HTH (101)
    numHTH = countPatternInSequence("101",tossResults)
    numHTHs.append(numHTH)
    print("Number of times HTH (101) showed up: " + str(numHTH))
    firstOccurrencePosHTH = tossResults.find("101")
    firstOccurrencePosHTHs.append(firstOccurrencePosHTH)
    print("The first occurrence of HTH is on position: "+str(firstOccurrencePosHTH))

    #HTT (100)
    numHTT = countPatternInSequence("100",tossResults)
    numHTTs.append(numHTT)
    print("Number of times HTT (100) showed up: " + str(numHTT))
    firstOccurrencePosHTT = tossResults.find("100")
    firstOccurrencePosHTTs.append(firstOccurrencePosHTT)
    print("The first occurrence of HTT is on position: " + str(firstOccurrencePosHTT))

totalOccurrenceHTH = np.sum(numHTHs)
totalOccurrenceHTT = np.sum(numHTTs)
x = np.arange(1,int(numOfSimulation)+1)
plt.plot(x, numHTHs, label="HTH; totalOccurences:"+str(totalOccurrenceHTH))
plt.plot(x, numHTTs, label="HTT; totalOccurences:"+str(totalOccurrenceHTT))
plt.xlabel = "Number of simulations"
plt.ylabel = "Number of occurences"
plt.title("Number of occurrences | " + numOfSimulation + " simulations | " + numOfToss + " tosses/simulation")
plt.legend()
plt.show()

avgPosHTH = np.mean(firstOccurrencePosHTHs)
avgPosHTT = np.mean(firstOccurrencePosHTTs)
plt.plot(x, firstOccurrencePosHTHs, label="HTH; avgPos:"+str(avgPosHTH))
plt.plot(x, firstOccurrencePosHTTs, label="HTT; avgPos:"+str(avgPosHTT))
plt.xlabel = "Number of simulations"
plt.ylabel = "First occurence of pattern"
plt.title("Position of the first occurences of pattern | " + numOfSimulation + " simulations | " + numOfToss + " tosses/simulation")
plt.legend()
plt.show()