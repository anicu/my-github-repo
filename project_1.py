'''
author = Anna Carnogurska
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# 1. Greet or welcome the user to the app
print('-'*40)
print('Welcome to the app. Please log in: ')

# 2. & 3. Ask the user for entering username and password and check whether the password and username entered are among those registered.
registered_users = {'bob':'123', 'ann':'pass123', 'mike':'password123', 'liz':'pass123'}
registration_unsuccess = True

while registration_unsuccess:
    username = input('USERNAME: ')
    password = input('PASSWORD: ')
    if username in registered_users and password == registered_users[username]:
        registration_unsuccess = False
    else:
        print('Registration was not successful. Please enter your username and password again.')
print('-'*40)

# 4. Ask the user to select among the three texts stored in the variable TEXTS.
text_choice = input('''We have 3 texts to be analyzed.
Enter a number btw. 1 and 3 to select: ''')
while not text_choice.isnumeric() or not 0 < int(text_choice) < len(TEXTS) + 1:
    text_choice = input('Wrong selection. Try again.')
chosen_text = TEXTS[int(text_choice) - 1]
print('-'*40)

# 5. Calculate the following statistics for the selected text:
for char in '.,':
    chosen_text=chosen_text.replace(char,' ')
word_list = chosen_text.split()

# number of words in total
print(f'There are {len(word_list)} words in the selected text.')

# number of words starting with capital letter
capital_letter_words = 0
for i in word_list:
    if i[0].isupper():
        capital_letter_words += 1
print(f'There are {capital_letter_words} titlecase words.')

# number of uppercase words
uppercase_words = 0
for i in word_list:
    if i.isupper():
        uppercase_words += 1
print(f'There are {uppercase_words} uppercase words.')

# number of lowercase words
lowercase_words = 0
for i in word_list:
    if i.islower():
        lowercase_words += 1
print(f'There are {lowercase_words} lowercase words.')

# number of numeric-only words (e.g. 100, not 100N)
numeric_words = 0
for i in word_list:
    if i.isnumeric():
        numeric_words += 1
print(f'There are {numeric_words} numeric strings.')
print('-'*40)

# 6. Create a bar chart depicting the frequencies of word lengths in the text.
max_length = max([len(i) for i in word_list])
min_length = min([len(i) for i in word_list])

for i in range(min_length, max_length + 1):
    bar_chart = 0
    for j in word_list:
        if len(j) == i:
            bar_chart += 1
    if bar_chart != 0:
        print(i, '*' * bar_chart, bar_chart)
print('-'*40)

# 7. Calculate the sum of all the numeric "words" in the given text.
sum_numeric_words = 0.0
for i in word_list:
    if i.isnumeric():
        sum_numeric_words = + float(i)
print(f'If we summed all the numbers in this text we would get: {sum_numeric_words}')
print('-'*40)