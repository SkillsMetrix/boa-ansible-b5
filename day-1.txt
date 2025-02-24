#initializing an empty array
use_numbers=[]

#ask user to add the data

n= int(input('How many numbers you wana add: '))

# take this input into the array
for i in range(n):
    num= int(input (f"Enter Numbers {i+1}" ))
    use_numbers.append(num)
print(use_numbers)

# loop through the array

for num in use_numbers:
    if num%2==0:
        print(f"{num} is even number")
    else:
         print(f"{num} is odd number")
