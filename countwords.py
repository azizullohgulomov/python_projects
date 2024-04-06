def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = "This is a sample sentence."
print("Word count:", count_words(sentence))