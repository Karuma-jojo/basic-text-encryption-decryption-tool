# Vigenere demonstration: A = 0, B = 1, ..., Z = 25.
# Non-English-letter characters stay unchanged and do not use a key letter.


def _transform(text, keyword, direction):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"

    if not keyword:
        raise ValueError("Enter a keyword containing English letters A-Z only.")

    for character in keyword:
        if character not in uppercase and character not in lowercase:
            raise ValueError("The keyword must contain English letters A-Z only.")

    keyword = keyword.lower()
    result = ""
    key_position = 0

    for character in text:
        if character in uppercase:
            alphabet = uppercase
        elif character in lowercase:
            alphabet = lowercase
        else:
            result = result + character
            continue

        position = alphabet.index(character)
        shift = lowercase.index(keyword[key_position])
        new_position = (position + direction * shift) % 26
        result = result + alphabet[new_position]

        key_position = (key_position + 1) % len(keyword)

    return result


def encrypt(text, keyword):
    return _transform(text, keyword, 1)


def decrypt(text, keyword):
    return _transform(text, keyword, -1)
