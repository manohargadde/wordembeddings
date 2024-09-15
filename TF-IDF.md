# TF-IDF (Term Frequency - Inverse Document Frequency)

TF-IDF is a statistical measure used in Natural Language Processing (NLP) to evaluate the importance of a word in a document relative to a collection of documents (corpus). It’s an enhancement of the simple Bag of Words (BoW) model by weighting words based on their importance across the entire corpus. TF-IDF helps highlight words that are frequent in a document but not too common across all documents, thus making them more meaningful.

## Components of TF-IDF:

1. **Term Frequency (TF)**: Measures how often a word appears in a specific document.
2. **Inverse Document Frequency (IDF)**: Measures how important a word is by looking at how often it appears across all documents in the corpus. The more documents the word appears in, the lower its importance.
3. **TF-IDF**: The final score for each word is the product of its TF and IDF scores.

## Example:

Let’s take three simple documents:
- Doc1: "I love NLP."
- Doc2: "NLP is great."
- Doc3: "I love learning NLP."

### Step 1: Tokenize Documents

First, break each document into words:
- Doc1: ["I", "love", "NLP"]
- Doc2: ["NLP", "is", "great"]
- Doc3: ["I", "love", "learning", "NLP"]

### Step 2: Calculate Term Frequency (TF)
For each word in each document, calculate the term frequency.

### Step 3: Calculate Inverse Document Frequency (IDF)

Now calculate the IDF for each word across the 3 documents.

### Step 4: Calculate TF-IDF

Now, compute the TF-IDF score for each word in each document.

As seen in this example, words like “NLP” get a score of zero because they appear in every document, while words like "learning" and "great" receive higher scores due to their relative rarity across the corpus.

## Where TF-IDF Works Well:

1. **Document Ranking**: TF-IDF is frequently used by search engines to rank documents by relevance to a search query. Words that appear frequently in a specific document but not in many others will have a higher TF-IDF score, indicating that document is more relevant.
2. **Keyword Extraction**: TF-IDF can be used to extract important words from a document by identifying terms that appear frequently in the document but not across the entire corpus.
3. **Text Classification**: In tasks like sentiment analysis or spam detection, TF-IDF can improve classification models by focusing on distinctive words rather than common words (like “the” or “is”).
4. **Filtering Stopwords**: Since common words (stopwords) like "is" and "the" tend to have low IDF scores, they are naturally down-weighted, reducing their importance in the document representation.

## Where TF-IDF Doesn’t Work Well:

1. **Ignores Word Order**: TF-IDF, like Bag of Words, does not capture word order or context. So, phrases like "good movie" and "movie good" are treated the same, even though they have different meanings.
2. **No Semantic Information**: TF-IDF treats words as independent units and doesn't capture semantic relationships. Words like "great" and "excellent" are treated as distinct, even though they have similar meanings.
3. **Contextual Limitations**: It struggles with understanding negation or complex sentence structures. For example, "not bad" might have a positive sentiment, but TF-IDF will treat "bad" as a negative term without understanding the negation.
4. **Sparse Representations**: TF-IDF creates high-dimensional, sparse vectors, which can be inefficient for large datasets or corpora with large vocabularies. While useful for simple text classification or search tasks, this high dimensionality can be problematic for deeper NLP tasks.

## Alternatives to TF-IDF:

- **Word Embeddings (Word2Vec, GloVe)**: These capture semantic meaning and relationships between words by mapping them to dense vectors, addressing the limitation of context and word meaning.
- **BERT (Bidirectional Encoder Representations from Transformers)**: A state-of-the-art model that considers the entire sentence context and captures deeper semantic relationships, useful for tasks like question-answering or text summarization.

## Summary:

TF-IDF is an effective, simple way to represent text, especially for document ranking, keyword extraction, and basic classification tasks. However, it struggles with capturing context, word semantics, and is less efficient in high-dimensional data spaces compared to modern methods like word embeddings or transformers.
