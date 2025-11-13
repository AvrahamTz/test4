def caesar_cipher(text:str,offset:int):
    encrypt = ""
    alpahbeth=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    lower_text = text.lower()
    for letter in lower_text:
        for i in range(len(alpahbeth)):
            if letter == alpahbeth[i]:
                encrypt += alpahbeth[(i+offset)%25]
    return encrypt

def reverse_caesar_cipher(text:str,offset:int):
    decrypt = ""
    alpahbeth=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    lower_text = text.lower()
    for letter in lower_text:
        for i in range(len(alpahbeth)):
            if letter == alpahbeth[i]:
                decrypt += alpahbeth[(i-offset)]
    return decrypt

def fence_cipher(text:str):
    convert=""
    temp=""
    fence = text.replace(' ',"")
    for i in range(len(fence)):
        if i %2 == 0:
            convert+= fence[i]
        else:
            temp += fence[i] 
    convert += temp
    return convert           
def reverse_fence_cipher(text:str):
    first_half = text[:len(text)//2]
    second_half = text[len(text)//2:]
    original = ""
    for i in range(len(first_half)):
        original += first_half[i]
        original += second_half[i]
    return original

     
