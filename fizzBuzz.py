import modules

modules.clearer()

print("Enter a interger value below:")
num = int(input())

if (num % 3 == 0) and (num % 5 == 0):
    print('FizzBuzz')
elif (num % 3 == 0):
    print('Fizz')
elif (num % 5 == 0):
    print('Buzz')
else:
    print('Not divisible by either 3 or 5!!')
