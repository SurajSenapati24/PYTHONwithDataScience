"""Write a program to find the number of occurrences of each vowel present in a given string, and also
 print the vowels."""
vowels="aeiou"
st=input("Enter a string: ")
st=st.lower()
d={}
for i in st:
    if i in vowels:
        d[i]=st.count(i)
print(d)