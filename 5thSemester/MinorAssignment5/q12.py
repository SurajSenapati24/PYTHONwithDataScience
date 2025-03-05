def count_duplicates(sentence):
    words = sentence.lower().split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    duplicates = {word: count for word, count in word_count.items() if count > 1}
    
    if duplicates:
        print("Duplicate words and their counts:")
        for word, count in duplicates.items():
            print(f"{word}: {count}")
    else:
        print("No duplicate words found.")

sentence = "This is a test sentence and this is a test"
count_duplicates(sentence)
