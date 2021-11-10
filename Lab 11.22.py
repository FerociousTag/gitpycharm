#Zachary Blackwell 1941472

word_list = []

word_list = input()
#splits the input into indiviual words
each_word = word_list.split()

for word in each_word:
    # counts the number of times the word is typed
    occurence = each_word.count(word)
    print(word, occurence)