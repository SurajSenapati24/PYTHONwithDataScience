def unique_pairs(words):
    result = set()
    
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 4 and len(words[j]) >= 4:
                if not set(words[i]) & set(words[j]):
                    result.add(tuple(sorted([words[i], words[j]])))
    
    return result
words = ["apple", "dogs", "cat", "bird", "fish", "zebra", "lion"]
print(unique_pairs(words))
