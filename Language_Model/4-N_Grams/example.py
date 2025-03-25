import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sentence = "I am learning AI"
tokens = word_tokenize(sentence)
bigrams = list(ngrams(tokens, 2)) # Bigram

print(bigrams)