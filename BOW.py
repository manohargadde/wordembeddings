from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Sample data
sentences = [
	"The quick brown fox jumped over the lazy dog.",
	"She sells seashells by the seashore.",
	"Peter Piper picked a peck of pickled peppers."
]
# Initialize CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the data
X = vectorizer.fit_transform(sentences)

# Convert to DataFrame for better readability
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

print(df)
