import string

def shift(char, shift_value):
    alphabet = string.ascii_uppercase
    idx = alphabet.index(char)
    return alphabet[(idx + shift_value) % 26]

def decrypt(ciphertext, shift_value):
    plaintext = ""
    for char in ciphertext:
        if char in string.ascii_uppercase:
            plaintext += shift(char, -shift_value)
        else:
            plaintext += char
    return plaintext

def correlation_of_frequency(ciphertext):
    alphabet = string.ascii_uppercase
    reference_frequency = {'A': 0.082, 'B': 0.015, 'C': 0.028, 'D': 0.043, 'E': 0.127,
                           'F': 0.022, 'G': 0.020, 'H': 0.061, 'I': 0.070, 'J': 0.002,
                           'K': 0.008, 'L': 0.040, 'M': 0.024, 'N': 0.067, 'O': 0.075,
                           'P': 0.019, 'Q': 0.001, 'R': 0.060, 'S': 0.063, 'T': 0.091,
                           'U': 0.028, 'V': 0.010, 'W': 0.023, 'X': 0.001, 'Y': 0.020, 'Z': 0.001}
    frequency = {char: 0 for char in alphabet}
    for char in ciphertext:
        if char in alphabet:
            frequency[char] += 1
        #print(frequency[char])
    for char in frequency:
        frequency[char] /= len(ciphertext)
        print(char , ": " , frequency[char])
    max_correlation = -1
    best_shift = 0
    for shift_value in range(1, 26):
        correlation = 0
        for char in alphabet:
            correlation += frequency[shift(char, shift_value)] * reference_frequency[char]
        if correlation > max_correlation:
            max_correlation = correlation
            best_shift = shift_value
    return best_shift

ciphertext = "IT STY XYZRGQJ TAJW XTRJYMNSL GJMNSI DTZ"
shift_value = correlation_of_frequency(ciphertext)
plaintext = decrypt(ciphertext, shift_value)
print("Plaintext:", plaintext)
