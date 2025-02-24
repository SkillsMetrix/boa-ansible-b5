

# solution-1
def sumOfArray(arr):
    total=0
    for num in arr:
        total +=num
    return total

numbers=[12,13,14,1,5]
result= sumOfArray(numbers)
print(f"the addition is {result}")


#solution-2
def sumOfArray(*arr):
    total=0
    for num in arr:
        total +=num
    return total

 
result= sumOfArray(12,13,14,1,5)
print(f"the addition is {result}")