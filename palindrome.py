# def is_palindrome(string):
#     return string[::-1].casefold() == string.casefold()
#
#
# word = input('Enter a string: ')
# if is_palindrome(word):
#     print(f'{word} is palindrome')
# else:
#     print(f'{word} is not palindrome')

def palindrome_sentence(sentence):
    string = ""
    for character in sentence:
        if character.isalnum():
            string += character

    return string[::-1].casefold() == string.casefold()


word = input('Enter a string: ')
if palindrome_sentence(word):
    print(f'{word} is palindrome')
else:
    print(f'{word} is not palindrome')
