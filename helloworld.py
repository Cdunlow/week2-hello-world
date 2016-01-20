# Charles Dunlow

import sys #allows sys commands

print('Hello World!') #greets the world in english
print('Choose a language and I will greet you in that language!') #ask the user to choose a language from a list i provided
print('1 for English') #prints out 1 for english
print('2 for French') #prints out 2 for french
print('3 for Spanish')   #prints out 3 for spanish
chosenLanguage = input()   #will recognize what the user inputed
if chosenLanguage == '1':   #will print in english if chosen
   print('Hello world!')
if chosenLanguage == '2':
   print('Bonjour le monde!')   #will print in french if chosen
if chosenLanguage == '3':   #will print in spanish if chosen
   print('¡Hola Mundo!')
while True:      #is used to exit the program
    print(' Type Q to exit the program.')    #prints out statement for user to acknowledge
    response = input()   #recognizes what user inputed
    if response == 'Q':   #makes sure the user only entered "Q" otherwie ask user again for correct response
        sys.exit()   #exits program completley
