
def alphabet_position(letter):
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    position = 0
    if letter in (alphabet_lower):
        for char in alphabet_lower:
            if letter == char:
                return (position)
            else:
                position += 1
    elif letter in (alphabet_upper):
        for char in alphabet_upper:
            if letter == char:
                return (position)
            else:
                position += 1 
                
def rotate_character(char, rot):
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if char not in alphabet_lower+alphabet_upper: #return any non letters as is
        return (char)
    else:
        rotated_index = alphabet_position(char)+rot #calculate rotated index
        if rotated_index < 26:
            reduced_rotated_index = rotated_index
        elif rotated_index >= 26:
            reduced_rotated_index = (rotated_index % 26) #simplify rotated index over 26
        if char in (alphabet_lower):
            return (alphabet_lower[reduced_rotated_index])
        elif char in (alphabet_upper):
            return (alphabet_upper[reduced_rotated_index])

def encrypt(text,rot):
    encrypted_text = ""
    for x in text:
        new_char = rotate_character(x,rot)
        encrypted_text += new_char
    return encrypted_text
  
    
