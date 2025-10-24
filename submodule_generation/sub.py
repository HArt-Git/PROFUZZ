import re
# Open the file and read its contents
with open("submodules.txt", "r") as file:
    # Read the lines, strip whitespace, and split into words
    target = [word for line in file for word in line.split()]

# Print the list
#print("List contents:", target)
target = [re.sub(r"[{}]", "", item) for item in target]
print("Number of elements in the list:", len(target))



import sys
import random

def generate_random_sample(low, high, percentage):
    # Calculate the total number of numbers in the range [low, high]
    total_numbers = high - low + 1
  

    # Calculate how many numbers to sample based on the percentage
    sample_size = int((percentage / 100) * total_numbers)

    # Generate the random sample
    random_sample = random.sample(range(low, high + 1), sample_size)

    return random_sample


low = 0    # Lowest number in range
high = len(target) -1  # Highest number in range
#print(low)
#print(high)
percentage = 75  # Percentage of target nets to sample


#random.seed(100)


sample = generate_random_sample(low, high, percentage)



print(sample)


with open("sub.tcl", "w") as file:
    file.write("group -name target " + " ".join(f"inst:GPIO/{target[item]}" for item in sample) + "\n")
