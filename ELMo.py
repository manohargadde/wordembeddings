import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

# Load pre-trained ELMo model from TensorFlow Hub
elmo = hub.load("https://tfhub.dev/google/elmo/3")

# Example sentences
sentences = ["The quick brown fox jumps over the lazy dog",
             "The dog barked at the cat"]

# Define a function to get ELMo embeddings
def get_elmo_embeddings(sentences):
    #elmo.signatures- Retrieves the embeddings for the input sentences
    embeddings = elmo.signatures['default'](tf.constant(sentences))
    # embeddings['elmo'] - Contains the embeddings for the sentences.
    return embeddings['elmo']

# Get ELMo embeddings
embeddings = get_elmo_embeddings(sentences)

# Convert embeddings to NumPy arrays
elmo_embeddings = [np.array(embedding) for embedding in embeddings.numpy()]

# Print embeddings for the first sentence
print(f"ELMo embeddings for the first sentence:")
print(elmo_embeddings[0])
