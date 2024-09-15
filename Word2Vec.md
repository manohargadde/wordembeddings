# Word2Vec Overview

Word2Vec is a popular method for learning word embeddings (vector representations of words) based on their context in a corpus. Introduced by researchers at Google, it converts words into vectors such that words with similar meanings are placed closer together in the vector space.

## How Word2Vec Works

### Training with Context Windows

- **CBOW Example**: In the sentence "The cat sat on the mat", Word2Vec might use "the cat" and "on the mat" to predict "sat".
- **Skip-Gram Example**: Using "sat" as the target word, it would predict the surrounding context words "the," "cat," "on," and "mat".

### Vector Space Representation

After training, each word is represented as a vector (e.g., 300-dimensional). Words that share similar contexts have vectors that are close to each other in the vector space.

### Word Arithmetic

Word2Vec captures analogies through vector arithmetic, for example:
- `king - man + woman = queen`

## Strengths of Word2Vec

1. **Captures Semantic Relationships**: It is effective in identifying synonyms, antonyms, and analogies.
2. **Efficient with Large Datasets**: Can be trained on large text corpora.
3. **Domain Adaptability**: Can be trained on domain-specific text to capture relevant word relationships.

## Applications

- **Semantic Similarity Tasks**: Identifying relationships between words based on meanings.
- **Recommendation Systems**: Using embeddings to recommend items by treating items as words.
- **NLP Tasks**: Useful in sentiment analysis, machine translation, and text classification.

## Limitations

1. **Out-of-Vocabulary Words**: Cannot handle words not seen during training.
2. **No Sense Disambiguation**: Cannot differentiate between words with multiple meanings.
3. **Contextual Dependence**: Captures context only within a fixed window.
4. **Static Embeddings**: Word vectors do not adapt to different contexts.

## Conclusion

While Word2Vec is a powerful technique for learning word representations, its limitations are addressed by newer models like BERT, which consider the full sentence context.

