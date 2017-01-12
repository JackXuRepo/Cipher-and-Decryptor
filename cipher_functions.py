# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:
# card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
#process_message([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26], 'HNXYOSSPZBAZWIRJBILLBYWBCECMQTZWEJNRMGDXQEBYZJQTQDQXASDURUQTFAF', 'd')

def clean_message(old_message):
    '''(str) -> str
    This function takes in a line of text/message, and removes any characters
    that is not a letter. It then converts all lowercase letters to uppercase.
    REQ: len(old_message) > 0

    >>> clean_message('Black Friday!!! $249.99 items at 50% off #DoneDeal')
    'BLACKFRIDAYITEMSATOFFDONEDEAL'
    '''
    # Initialize and create a variable to store the new formatted message
    new_message = ""
    # Check each character in the message
    for character in old_message:
        # If character is a letter convert it to uppercase and add it to
        # new_message
        if(character.isalpha()):
            new_message += character.upper()
    return new_message


def encrypt_letter(letter, key_value):
    '''(str, int) -> str
    This function applies encryption an already uppercase letter, using a
    keystream value to generate a new encrypted letter.
    REQ: letter.isupper() == True
    REQ: len(letter) == 1
    REQ: (key_value > 0) and (key_value < modulo_value)
    
    >>> encrypt_letter('L', 12)
    'X'
    >>> encrypt_letter('L', 15)
    'A'
    >>> encrypt_letter('L', 14)
    'Z'
    '''
    # Store the modulo value in a variable
    modulo_value = 26
    # Hold ASCII value in which the uppercase characters start
    start_value = 65

    # convert the letter character into an ASCII value
    letter_ASCII = ord(letter)
    # convert from ASCII value to a letter value
    letter_value = letter_ASCII - start_value

    # calculate the letter's value for the encrypted letter
    encrypted_value = letter_value + key_value
    # if the encrypted letter's value exceeds or is equal to the modulo value
    # change encrypted_value to be the amount that it exceeds in respect to
    # the module value.
    if (encrypted_value >= modulo_value):
        encrypted_value = encrypted_value - modulo_value

    # convert the encryoted letter's value to an ASCII value
    encrypted_ASCII = encrypted_value + start_value
    # obtain the encrypted letter
    encrypted_letter = chr(encrypted_ASCII)
    return encrypted_letter    



def decrypt_letter(encrypted_letter, key_value):
    '''(str, int) -> str
    This function applies decryption an already u encrypted uppercase letter, 
    using a keystream value to decrypt a letter.
    REQ: encrypted_letter.isupper() == True
    REQ: len(encrypted_letter) == 1
    REQ: (key_value > 0) and (key_value < modulo_value)

    >>> decrypt_letter('X', 12)
    'L'
    >>> decrypt_letter('I', 8)
    'A'
    >>> decrypt_letter('M', 14)
    'Y'
    '''
    # Store the modulo value in a variable
    modulo_value = 26
    # Hold ASCII value in which the uppercase characters start
    start_value = 65

    # convert the letter character into an ASCII value
    encrypted_ASCII = ord(encrypted_letter)
    # convert from ASCII value to a letter value
    encrypted_value = encrypted_ASCII - start_value

    # Obtain the letter value of the decrypted letter and convert it to the
    # decrypted letter
    letter_value = encrypted_value - key_value
    if(letter_value < 0):
        letter_value = letter_value + modulo_value

    letter_ASCII = letter_value + start_value
    letter = chr(letter_ASCII)
    return letter

    
def swap_cards(card_deck, index):
    deck_size = len(card_deck)
    value_at_index = card_deck[index]

    if((index + 1) > (deck_size - 1)):
        card_deck[index] = card_deck[0]
        card_deck[0] = value_at_index
    else:
        next_value = card_deck[index + 1]
        card_deck[index + 1] = value_at_index
        card_deck[index] = next_value



def move_joker_1(card_deck):
    joker_1_index = card_deck.index(JOKER1)
    swap_cards(card_deck, joker_1_index)

def move_joker_2(card_deck):
    joker_2_index = card_deck.index(JOKER2)
    swap_cards(card_deck, joker_2_index)
    joker_2_index = card_deck.index(JOKER2)
    swap_cards(card_deck, joker_2_index)
    
    

def triple_cut(card_deck):
    joker_1_index = card_deck.index(JOKER1)
    joker_2_index = card_deck.index(JOKER2)
    
    both_jokers = [joker_1_index, joker_2_index]
    both_jokers.sort()
    #print(both_jokers)

    min_joker_index = both_jokers[0]
    max_joker_index = both_jokers[1]
    
    top_group = card_deck[:min_joker_index]
    middle_group = card_deck[min_joker_index : (max_joker_index + 1)]
    bottom_group = card_deck[(max_joker_index + 1 ):]
    #print(top_group)
    #print(middle_group)
    #print(bottom_group)
    
    shuffled_deck = bottom_group + middle_group + top_group
    card_deck[:] = shuffled_deck[:]
    #print(card_deck)


def insert_top_to_bottom(card_deck):
    value_at_bottom = card_deck[len(card_deck) - 1]
    top_deck_size = value_at_bottom 
    
    if(value_at_bottom == JOKER2):
        top_deck_size = JOKER1

    top_deck = card_deck[:top_deck_size]
    rest_deck = card_deck[top_deck_size:]
    rest_deck.remove(value_at_bottom)
    modified_deck = rest_deck + top_deck
    modified_deck.append(value_at_bottom)
    card_deck[:] = modified_deck[:]
    #print(card_deck)

def get_card_at_top_index(card_deck):
    value_at_top = card_deck[0]

    if(value_at_top == JOKER2):
        value_at_top = JOKER1 

    return card_deck[value_at_top]
    
def get_next_value(card_deck):
    move_joker_1(card_deck)
    move_joker_2(card_deck)
    triple_cut(card_deck)
    insert_top_to_bottom(card_deck)
    keystream = get_card_at_top_index(card_deck)
    return keystream

def get_keystream_value(card_deck):
    keystream = 9001
    modulus_value = 26
    while (keystream > modulus_value):
        keystream = get_next_value(card_deck)
    return keystream


def process_message(card_deck, message, encrypt_or_decrypt):
    message = clean_message(message)
    new_message = ''
    encrypt = 'e'
    decrypt = 'd'
    for letter in message:
        keystream = get_keystream_value(card_deck)
        if (encrypt_or_decrypt == encrypt):
            new_letter = encrypt_letter(letter, keystream)
        elif (encrypt_or_decrypt == decrypt):
            new_letter = decrypt_letter(letter, keystream)
        new_message += new_letter
    return new_message

def process_messages(card_deck, messages, encrypt_or_decrypt):
    processed_messages = []
    for message in messages:
        new_message = process_message(card_deck, message, encrypt_or_decrypt)
        processed_messages.append(new_message)
    return processed_messages

def read_messages(file_handler):
    file_handler = open(file_handler, "r")
    all_lines = file_handler.readlines()
    file_handler.close()
    message_list = []

    for line in all_lines:
        line = line.strip('\n')
        message_list.append(line)
    return message_list

def read_deck(file_handler):
    file_handler = open(file_handler, "r")
    deck_str = file_handler.read()
    file_handler.close()
    card_deck = []
    deck_str = deck_str.split()

    for card in deck_str:
        card_deck.append(int(card))
    return card_deck

def main():
    MODE = 'e'
    card_deck = read_deck("deck2.txt")
    messages = read_messages("MSG_FILENAME.txt")
    processed_messages = process_messages(card_deck, messages, MODE)
    for message in processed_messages:
        print(message)