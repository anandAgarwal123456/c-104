# Python program to print
# median of elements
import csv

with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    allData = list(reader)
# removing the list of titles using pop
allData.pop(0)

heightArr=[]
for i in range(len(allData)):
	n_num = allData[i][1]
	heightArr.append(n_num)

n = len(heightArr)
heightArr.sort()

#using floor division to get the nearest number whole number
# floor division is shown by //
if n % 2 == 0:
    #getting the first number
	median1 = float(heightArr[n//2])
    #getting the second number
	median2 = float(heightArr[n//2 - 1])
    #getting mean of those numbers
	median = (median1 + median2)/2
else:
	median = heightArr[n//2]

print("Median is: " + str(median))
