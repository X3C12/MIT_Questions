'''
NOTE:
This is a simple program to calculate error for physics 11th grade 
use it as u wish
'''

# Loop until user enters a valid positive integer for the number of readings
while True:
    try:
        num_repeats = int(input("How many readings do you have: "))
        if num_repeats <= 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Initialize an empty list to store the readings
readings = []

# Loop to input each reading
for i in range(num_repeats):
    while True:
        try:
            # Input each reading and convert to float
            reading = float(input(f"Reading {i+1}: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    # Append each reading to the list
    readings.append(reading)

# Print the list of readings
print("Readings:", readings)

# Calculate the sum of all readings
sum_of_readings = sum(readings)
print("Sum of readings:", sum_of_readings)

# Calculate the mean (Rm) of the readings
Rm = sum_of_readings / num_repeats
print("Rm:", Rm)

# Calculate the deviations from the mean
deviations = [reading - Rm for reading in readings]
print("Deviations from mean:", deviations)

# Calculate the absolute deviations from the mean
abs_deviations = [abs(reading - Rm) for reading in readings]
print("Deviations from mean (absolute values):", abs_deviations)

# Calculate the mean of the deviations (dRm)
dRm = sum(deviations) / num_repeats
print("dRm:", dRm)

# Calculate the mean of the absolute deviations (dRm_abs)
dRm_abs = sum(abs_deviations) / num_repeats
print("dRm (absolute values):", dRm_abs)

# Calculate the relative error (RE)
RE = dRm_abs / Rm
print("RE:", RE)

# Calculate the percentage relative error
Percent_Rm = RE * 100
print("Percent_Rm:", Percent_Rm)