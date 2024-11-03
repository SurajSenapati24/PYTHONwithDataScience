def vowel_indices(s):
    vowels=[]
    count=0
    for i in s:
        if i.lower() in "aeiou":
            vowels.append(count)
            count+=1
        else:
            count+=1
    print(f"The vowel indices in the string is: {vowels}")
user=input("Enter a string: ")
vowel_indices(user)   