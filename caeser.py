def encrypt(text, shift):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    shift = shift % 26

    for character in text:
        if character in uppercase:
            alphabet = uppercase
        elif character in lowercase:
            alphabet = lowercase
        else:
            result = result + character
            continue

        position = alphabet.index(character)
        new_position = position + shift

        if new_position >= 26:
            new_position = new_position - 26

        result = result + alphabet[new_position]

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)