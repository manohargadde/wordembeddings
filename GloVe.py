import gensim
import numpy as np

# Load pre-trained GloVe vectors
def load_glove_vectors(glove_file):
    # Create a dictionary to hold word vectors
    word_vectors = {}
    with open(glove_file, 'r', encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            vector = np.array(values[1:], dtype='float32')
            word_vectors[word] = vector
    return word_vectors

# Example usage
#You can download pre-trained GloVe vectors from GloVe's official website. https://nlp.stanford.edu/projects/glove/
#For example, glove.6B.zip contains vectors of various dimensions (50d, 100d, 200d, 300d).
glove_file = 'glove.6B.50d.txt'  # Replace with the path to your GloVe file
word_vectors = load_glove_vectors(glove_file)

# Print vector for a specific word
word = 'cat'
if word in word_vectors:
    print(f"Vector for '{word}':\n{word_vectors[word]}")
else:
    print(f"Word '{word}' not found in GloVe vectors.")
