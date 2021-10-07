alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
'''
def encrypt(text_value,shift_number): # func take 2 param
    cipher_text="" # empty string for the text enter
    for letter in text_value: # loop start here, if you enter hello, this will take h,e,l,l,o like this
        position=alphabet.index(letter) # this will tell the index value of each letter you use, so h index value 7
        new_position=position + shift_number # add shift number you enter, 7(h index) + 5 shift numb=12
        new_letter=alphabet[new_position] # 12
        cipher_text += new_letter # h replace this to m

    print(f'the encoded text in {cipher_text}')


def decrypt(text_value, shift_number): # func take 2 param
    plain_text="" # arg use as plain text as empty string
    for letter in text_value: # loop start here
        position=alphabet.index(letter) # index value for alphabet you use
        new_position=position - shift_number # this will reduce index value (12-5)
        plain_text+= alphabet[new_position] # this is the new position in letter
    print(f'The decode text is {plain_text}') # f string to print plain text

if direction=="encode": # if you choose encode run below
    encrypt(text_value=text, shift_number=shift)
elif direction== "decode":
    decrypt(text_value=text, shift_number=shift)

'''

def caser(start_text,shift_amount, cipher_direction): # here using 3 param
    end_text=""
    if cipher_direction == "decode": # if condition
        shift_amount *= -1 # 5 *-1 = -5 bcz in decode we're reducing char value
    for letter in start_text: # for loop start here, if use hello then loop in each value
        position = alphabet.index(letter) # alphabet you choose get me the index value
        new_position= position + shift_amount # add the index value with the shiftnumber you enter
        end_text += alphabet[new_position] # this will be my new letter.
    print(f'the {cipher_direction}d text is {end_text}')

caser(start_text=text, shift_amount=shift,cipher_direction=direction) # calling with the keywarg....







    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"


    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 