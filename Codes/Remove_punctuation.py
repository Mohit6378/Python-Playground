import string
def remove_punctuation(text):
    #create a translation table.
    table = str.maketrans('', '', string.punctuation)
    return text.translate(table)

text = input("Enter a text.\n")
new_text = remove_punctuation(text)
print("Original text : ", text)
print("Text after removing punctuation : ", new_text)