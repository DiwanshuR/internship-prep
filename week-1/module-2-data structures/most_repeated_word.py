sentence = input("Enter a sentence: ")
words_list = sentence.split()
word_count = {}
for word in words_list:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}: {count}")

# max evaluates each key of dict based on corresponsing value retrieved from dict.get(key)
most_repeated_word = max(word_count, key=word_count.get)
print(f"Most repeated word: {most_repeated_word}")