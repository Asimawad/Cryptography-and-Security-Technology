# A function to repeat the key to the desierd msg length

def vigenereCipherKey (msg , key):
    rem =len(msg) % len(key)
    reminder =list (key)
    repeted_key = list(key * (len(msg) // len(key)))
    repeted_key.extend(reminder[:rem])
    return "".join(repeted_key)
    
    
# this code is to  Implement the vigenere Cipher using English language 

# depends on two parameter first the Key and the message i.e plaintext

# look Up Table 
letters = [chr(x) for x in range(97,123)]

# First : input the Key

key = input("Enter the key for Vigenere Cipher :\n ").lower()
plainText = input ("Enter the message you want to encrypt :\n").replace(" ", "").lower()

# Second : Create the full length Key 
full_key = vigenereCipherKey(plainText,key)

# Third : cipherText
cipherText = []
for i in range(len(full_key)):
    distance = (letters.index(plainText[i]) + letters.index(full_key[i])) %26
    cipherText.append(letters [distance])

    
#The Final Result
print("The encripted Message :\n")
print("".join(cipherText).upper())

