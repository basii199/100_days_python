alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def start_cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != 'encode' and direction != 'decode':
        print("Invalid input -", direction)
        start_cipher()
        return

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    # TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
    # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
    #  by the shift amount and print the decrypted text.
    # TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
    #  Use the value of the user chosen 'direction' variable to determine which functionality to use.

    def encrypt(original_text, shift_amount):
        cipher_text = ""
        for letter in original_text:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {cipher_text}")



    def decrypt(original_text, shift_amount):
        decrypted = ''
        for letter in original_text:
            letter_index = alphabet.index(letter)
            decrypted_letter = alphabet[(letter_index - shift_amount)]
            decrypted += decrypted_letter
        print(decrypted)

    def caesar(direction, original_text, shift_amount):
        cipher_text = ''
        for letter in original_text:
            if letter not in alphabet:
                cipher_text += letter
                continue
            letter_index = alphabet.index(letter)
            if direction == 'encode':
                cipher_letter = alphabet[(letter_index + shift_amount)%len(alphabet)]
            else:
                cipher_letter = alphabet[(letter_index - shift_amount)]
            cipher_text += cipher_letter
        print(cipher_text)

    caesar(direction,text, shift)

    restart_cipher = input('Do you want to go again. (yes or no)\n')
    if restart_cipher == 'yes':
        start_cipher()
        return
    else:
        return

    # decrypt(original_text=text, shift_amount=shift)


start_cipher()