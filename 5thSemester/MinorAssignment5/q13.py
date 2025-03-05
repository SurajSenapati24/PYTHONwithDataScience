def unique_words(words):
    unique = set(word.lower() for word in words)
    for word in sorted(unique):
        print(word)

words = ["This", "is", "a", "test"]
unique_words(words)
