######### APPROACH 1 ############
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import numpy as np

# Sample data
documents = [
    "The quick brown fox jumps over the lazy dog",
    "The dog barked at the cat",
    "The cat and the dog played",
    "The quick brown fox"
]

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

# Apply LSA (TruncatedSVD) to the TF-IDF matrix
# Performs dimensionality reduction using SVD. The n_components parameter specifies the number of dimensions to reduce to (e.g., topics or latent dimensions)
lsa = TruncatedSVD(n_components=2)  # Number of topics or components 
X_lsa = lsa.fit_transform(X)

# Print the shape of the LSA matrix
print(f"Shape of LSA matrix: {X_lsa.shape}")

# Display the transformed documents
for i, doc in enumerate(X_lsa):
    print(f"Document {i}: {doc}")


######### APPROACH 2 ############


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np

# Sample data
documents = [
    "The quick brown fox jumps over the lazy dog",
    "The dog barked at the cat",
    "The cat and the dog played",
    "The quick brown fox"
]

# Create a CountVectorizer
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

# Apply LDA
# Performs topic modeling. The n_components parameter specifies the number of topics.
lda = LatentDirichletAllocation(n_components=2, random_state=0)
X_lda = lda.fit_transform(X)

# Print the shape of the LDA matrix
print(f"Shape of LDA matrix: {X_lda.shape}")

# Display the topic distribution for each document
for i, doc in enumerate(X_lda):
    print(f"Document {i}: {doc}")
