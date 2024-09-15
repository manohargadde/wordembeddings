# Term Frequency without Normalisation. Example below
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Sample data
sentences = [
	"The quick brown fox jumped over the lazy dog.",
	"She sells seashells by the seashore.",
	"Peter Piper picked a peck of pickled peppers."
]

# Initialize TfidfVectorizer with no IDF normalization
vectorizer = TfidfVectorizer(use_idf=False, norm=None)

# Fit and transform the data
X = vectorizer.fit_transform(sentences)

# Convert to DataFrame
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

print(df)




# Term Frequency with Normalisation

from collections import Counter
import pandas as pd

# Sample data
sentences = [
	"The quick brown fox jumped over the lazy dog.",
	"She sells seashells by the seashore.",
	"Peter Piper picked a peck of pickled peppers."
]

# Tokenize and compute term frequency
def compute_term_frequency(sentences):
    tf_data = []
    for sentence in sentences:
        words = sentence.lower().split()
        word_count = Counter(words)
        total_words = len(words)
        tf = {word: count / total_words for word, count in word_count.items()}
        tf_data.append(tf)
    return tf_data

# Compute Term Frequency
tf_data = compute_term_frequency(sentences)

# Create a DataFrame
df = pd.DataFrame(tf_data).fillna(0)

print(df)
