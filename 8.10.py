#zacharyblackwell

user_word = str(input())

def remove(user_word):
    return user_word.replace(" ", "")

length = len(user_word)
word_forward = remove(user_word)[:length + 1]
word_backwards = remove(user_word)[length::-1]

if word_forward == word_backwards:
    print(user_word, 'is a palindrome')
else:
    print(user_word, 'is not a palindrome')











