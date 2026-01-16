def vowel_count(text):
    vowel = "aeiou"

    count = {v : 0 for v in vowel}
    
    for char in text.lower():
        if char in count:
            count[char] += 1
    
    return count

text = input("Enter a text to count its vowels.\n")
print("Number of vowels in this text are: ")
print(vowel_count(text))