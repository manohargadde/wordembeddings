# Sample data
sentences = [
	"The quick brown fox jumped over the lazy dog.",
	"She sells seashells by the seashore.",
	"Peter Piper picked a peck of pickled peppers."
]

# Initialize TfidfVectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the data
X = vectorizer.fit_transform(sentences)

# Convert to DataFrame for better readability
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

print(df)
