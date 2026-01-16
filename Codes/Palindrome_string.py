word = input("Enter a string to check if its palindrome or not.\n")
if (word.lower() == word[::-1].lower()):
    print("It's a palindrome string.")
else:
    print("It is not a palindrome string.")