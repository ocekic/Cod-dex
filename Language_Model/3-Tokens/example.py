import nltk
nltk.download('punkt_tab')

sample_text = 'I am learning Generative AI'
tokens = nltk.word_tokenize(sample_text.lower())

print('Tokens:', tokens)