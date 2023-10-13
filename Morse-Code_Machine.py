# Translate letters in an input string to morse code

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
shouldContinue = True

def encrypt():
    coded_message = ''
    for char in message_to_encrypt:
        if char != ' ':
            coded_char = MORSE_CODE_DICT[char]
            coded_message += coded_char
        else:
            coded_message += ' '
    print(f'Here\'s your Morse code: {coded_message}')

while shouldContinue:
    print("Hello! Welcome to my Morse code machine:)")
    message_to_encrypt = input('What would you like to encrypt into morse code? ').upper()
    encrypt()
        
    play_again = input("Would you like to use the machine again? y/n ").lower()
    if play_again == 'n':
        print("Thanks for trying the program!")
        shouldContinue = False
    