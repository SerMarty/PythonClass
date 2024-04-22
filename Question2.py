#Martin R. Castillo Midterm Q2
import time

def is_prime(num):
  # Check if the number is less than 2
  if num < 2:
      return False

  # Check if the number is divisible
  for i in range(2, num):
      if num % i == 0:
          # since number is not divisible, it's not prime
          return False

  # If no divisors are found, the number is prime
  return True

# Input an integer from user
number = int(input("Enter a number to check if it's prime: "))

# Call the function and print the result
if is_prime(number):
  print(number, ", is a prime number.")
else:
  print(number, ", is not a prime number.")
  
time.sleep(15)