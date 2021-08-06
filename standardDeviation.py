import math
import csv


# list of elements to calculate mean
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

    data = file_data[0]

# finding mean
def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean



    
# squaring and getting the values
squared_list= []
for number in data:
    a = int(number) - mean(data)
    a= a**2
    squared_list.append(a)


    #getting sum
sum =0
for i in squared_list:
    sum =sum + i

    
#dividing the sum by the total values
result = sum/ (len(data)-1)


# getting the deviation by taking square root of the result
std_deviation = math.sqrt(result)
print(std_deviation)