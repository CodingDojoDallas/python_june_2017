# Multiples
# Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do
# this exercise.

for x in range(1, 1001):
    if (x % 3 == 0):
        print x

# Multiples
# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.:
sum = 1
 
for i in range(5, 1000000):
    if i % 5  % 1000000 == 0:
        sum += i
 
print("The sum of multiples of 5 between 5 to 1000000 is: " , + sum)

