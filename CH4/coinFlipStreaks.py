import random

experimentList = []

# Creating a List of 1 and 0s Randomly Generated
for experimentNumber in range(10000):
        experimentNumber = random.randint(0, 1)
        experimentList.append(experimentNumber)

del experimentList[0:9900]

# Streak Checker
numberOfStreaks = int(str((experimentList.count('111111') + experimentList.count('000000'))))

print(experimentList)
print(numberOfStreaks)