""" Hackathon - Level 6 """

def encrypt(text,s): 
    result = ""
    
    for i in range(0,len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 


text = "pxisb"
s = 3
print ("Text  : " + text) 
print ("Shift : " + str(s)) 
print ("Cipher: " + encrypt(text,s))
    
