from gensim.models import FastText
from gensim.utils import simple_preprocess

# Sample data
sentences = [
	"The quick brown fox jumped over the lazy dog.",
	"She sells seashells by the seashore.",
	"Peter Piper picked a peck of pickled peppers."
]

# Preprocess sentences: tokenization and lowercasing
processed_sentences = [simple_preprocess(sentence) for sentence in sentences]

# Train Word2Vec model
model = FastText(sentences=processed_sentences, vector_size=50, window=3, min_count=1, sg=0)
#vector_size=50: Number of dimensions for the word vectors.
#window=3: Maximum distance between the current and predicted word within a sentence.
#min_count=1: Ignores all words with a total frequency lower than this.
#sg=0: Uses Continuous Bag of Words (CBOW) model. Use sg=1 for Skip-gram model.

# Retrieve word vectors
words = list(model.wv.index_to_key)
word_vectors = {word: model.wv[word] for word in words}
#model.wv.index_to_key: List of words in the model's vocabulary.
#model.wv[word]: Vector for a specific word.

# Print word vectors
for word, vector in word_vectors.items():
    print(f"Word: {word}")
    print(f"Vector: {vector}\n")
