
# Exercise 1:
letter = input('Enter The Letter :').lower()
vowels = ['a', 'e', 'i', 'o', 'u']
if letter in vowels:
    print('This is a vowel.')

else:
    print('This is not a vowel.')

# Exercise 2:

number = int(input('Enter Your Number :'))

if 1000 <= number <= 2000:
    print('This number is in between 1000 and 2000.')
elif number >= 2000:
    print('This number is higher than 2000.')
else:
    print('This number is lower than 1000.')

# Exercise 3:
first_number = int(input('Enter Your first_Number :'))
second_number = int(input('Enter Your second_Number :'))
third_number = int(input('Enter Your third_Number :'))
sum = first_number + second_number + third_number
if first_number == second_number == third_number:
    print("These numbers are the same!")
    print("The sum of these number is :", sum)
    print("Multiplied by 4 this becomes", first_number * 4)
else:
    print(sum)

# Exercise 4:
first_number = int(input('Enter Your first_Number :'))
second_number = int(input('Enter Your second_Number :'))
third_number = int(input('Enter Your third_Number :'))

if first_number > second_number and first_number > third_number:
    print(f"first_number is : {first_number}")
elif second_number > first_number and second_number > third_number:
    print(f"second_number is : {second_number}")
else:
    print(f"third_number is : {third_number}")

# Exercise 5:
gross_salary = int(input('Enter Your Income :'))

if gross_salary <= 67000:
    taxes = (gross_salary * 24) // 100
    net_salary = gross_salary - taxes
    print(f'Your income after taxes is {net_salary}')

elif 67000 < gross_salary <= 97000:
    taxes = (gross_salary * 31) // 100
    net_salary = gross_salary - taxes
    print(f'Your income after taxes is {net_salary}')
else:
    taxes = (gross_salary * 34) // 100
    net_salary = gross_salary - taxes
    print(f'Your income after taxes is {net_salary}')

# Exercise 6:
word = input('Enter a word:')
length = len(word)
if length == 1:
    print(word * 6)
elif length == 2:
    print(word[1] + word[0])
elif length == 3:
    print(word[-1] + word[:2])
elif length == 4:
    print(word[::-1])
elif length == 5:
    print(*word, sep='t')

# Exercise 7:
import sys

answer_1 = 4
answer_2 = 2
answer_3 = 81

print('What is 2 * 2 ?')
user_answer_1 = int(input('Enter Your Gues:'))
if user_answer_1 == answer_1:
    print('That is correct!')
else:
    print('That is false !You failed')
    sys.exit()

print('What is 6 * 3 ?')
user_answer_2 = int(input('Enter Your Gues:'))
if user_answer_2 == answer_2:
    print('That is also correct!')
else:
    print('That is false !You failed')
    sys.exit()

print('What is 9 * 9 ?')
user_answer_3 = int(input('Enter Your Gues:'))
if user_answer_3 == answer_3:
    print('Correct! You Win !!')
else:
    print('That is false !You failed')
    sys.exit()