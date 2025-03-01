sentence = input("enter a sentence please: ")

word_count = {}

list_words = sentence.split()

for i in list_words:
    if i in word_count:
        word_count[i] +=1

    else:
        word_count[i] = 1    
print(word_count)