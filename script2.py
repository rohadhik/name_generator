import random, string

vowel = 'aeiouy'
consonent ='bcdfghjklmnpqrstvwxz'
letter = string.ascii_lowercase

input_letter_1 = input("Enter the first letter with vowels 'v': and enter the second letter with consonent 'c': and enter the third letter with any letter 'c': ")
input_letter_2 = input("Enter the first letter with vowels 'v': and enter the second letter with consonent 'c': and enter the third letter with any letter 'c': ")
input_letter_3 = input("Enter the first letter with vowels 'v': and enter the second letter with consonent 'c': and enter the third letter with any letter 'c': ")

#print (input_letter_1+input_letter_2+input_letter_3)

def generator():
    if input_letter_1 =='v':
        letter_1 = random.choice(vowel)
    elif input_letter_1=='c':
        letter_1= random.choice(consonent)
    elif input_letter_1=='l':
        letter_1= random.choice(letter)
    else:
        letter_1= input_letter_1

    if input_letter_2=='v':
        letter_2= random.choice(vowel)
    elif input_letter_2=='c':
        letter_2= random.choice(consonent)
    elif input_letter_2=='l':
        letter_2= random.choice(letter)
    else:
        letter_2 = input_letter_2


    if input_letter_3 =='v':
        letter_3 = random.choice(vowel)
    elif input_letter_3=='c':
        letter_3 = random.choice(consonent)
    elif input_letter_3=='l':
        letter_3 = random.choice(letter)
    else:
        letter_3 = input_letter_3

    name = letter_1 + letter_2 + letter_3
    return (name)

print (generator())
