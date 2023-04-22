# Bernabe, Aleckxis Kate V.
# BSCpE 1-4

# Run the numbers.txt input file.
with open('numbers.txt', 'r') as f:
# Read every line in the file and turn it into an integer.
    numbers = [int(line.strip()) for line in f.readlines()]
# In order to hold even and odd numbers, make two empty lists.
even_numbers = []
odd_number = []
# Run over each number in the input list repeatedly.
for num in numbers:
# Test if the number is even.
    if number % 2 == 0:
# Add the number to the list of even numbers if it is even.
        even_numbers.append(num)
# Add the number to the list of odd numbers if it is odd.
    else:
        odd_number.append(num)
# Write even integers into the output file "even.txt" after opening it.
# Write odd numbers to the output file 'odd.txt' after opening it.