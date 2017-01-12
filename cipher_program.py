import cipher_functions
def main():
    MODE = 'e'
    card_deck = read_deck("deck2.txt")
    messages = read_messages("MSG_FILENAME.txt")
    processed_messages = process_messages(card_deck, messages, MODE)
    for message in processed_messages:
        print(message)