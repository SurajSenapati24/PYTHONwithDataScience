def count_words_and_vowels(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Count words
        words = content.split()
        word_count = len(words)
        
        # Count vowels
        vowels = set("aeiouAEIOU")
        vowel_count = sum(1 for char in content if char in vowels)
        
        # Display the results
        print(f"Number of words: {word_count}")
        print(f"Number of vowels: {vowel_count}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
count_words_and_vowels('file1.txt')  # Replace 'file1.txt' with your file path
