from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_length = len(alphabet)


def caesar(direction,plain_text, shift_amount):
  cipher_text = ""
  if direction == 'decode':
    shift_amount *=-1

  for letter in plain_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift_amount

      if direction == "encode":
            if new_position > alphabet_length:
              new_position-=alphabet_length
      else:
            if new_position < 0:
              new_position+=alphabet_length
        
      cipher_text += alphabet[new_position]
    else:
      cipher_text += '*'
  print(f"With the direction {direction} the message is: {cipher_text}")

rerun = True
print(logo)
while rerun:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))


  # if the shift > alphabet length
  while shift > alphabet_length:
    shift -=alphabet_length

  caesar(direction=direction, plain_text=text, shift_amount=shift)

  rerun = input("Do you want to re-run the program?").lower()

  if rerun == "no":
    end_of_game = False
  else:
    print("Goodbye")
