import nltk,re
from nltk.corpus import words, names
en_letters = "abcdefghijklmnopqrstuvwxyz"
def encrypt(text ,numeric):
    """
    """
    chars=text.split()
    new_chars=[]
    for word in chars:
        encryptd_text=""
        for i in word:
            if i.lower() != i and i.lower() in en_letters:
                number=(en_letters.index(i.lower())+numeric) % 26
                encryptd_text+=(en_letters[number].upper())
            elif i.lower() == i and i.lower() in en_letters:
                number=(en_letters.index(i)+numeric) % 26
                encryptd_text+=(en_letters[number])
            else:
                encryptd_text+=i
        new_chars.append(encryptd_text)
    return " ".join(new_chars)

print(encrypt('Hello This is Abdullah',25))

def decrypt(text ,numeric):
    return encrypt(text , -numeric)

print(decrypt('Hs vzr sgd adrs ne shldr, hs vzr sgd vnqrs ne shldr',25))

nltk.download("words",quiet=True)
nltk.download("names",quiet=True)
word_list = words.words()
name_list = names.words()

def count_words(text):
    words = text.split()
    count = 0
    for candidate_word in words:
        word = re.sub(r'[^A-Za-z]+','',candidate_word)
        if word.lower() in word_list or word in name_list:
            count +=1
    return count

def crack(text):
    for key in range(0,27):
        new_text = decrypt(text,key)
        count = count_words(new_text)
        percentage = int(count / len(text.split()) * 100)

        if percentage > 90:
            return(new_text)
