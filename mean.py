# Python program to print
# mean of elements

# list of elements to calculate mean
import csv
with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    allValues = list(reader)

allValues.pop(0)
#print(allValues)

# sorting data  to get the height of people.
heightArray=[]
for i in range(len(allValues)):
	height = allValues[i][1]
	heightArray.append(float(height))

#print(heightArray)
#getting the mean
n = len(heightArray)
sumAllValues = 0
for ht in heightArray:
    sumAllValues += ht

mean = sumAllValues / n
print("Mean / Average is: " + str(mean))
