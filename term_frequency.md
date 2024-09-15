# Term Frequency (TF)

Term Frequency (TF) is a measure used in text mining and information retrieval to quantify the importance of a word in a document relative to the number of times it appears in that document. It's an extension of the Bag of Words (BoW) model, providing more nuanced weighting based on frequency.

## Definition:

The Term Frequency of a word w in a document d is defined as:

$$
TF(w, d) = \frac{\text{Number of times word } w \text{ appears in document } d}{\text{Total number of words in document } d}
$$

This normalizes the count of a word in the document by the document's total length, making it easier to compare across documents of different sizes.

## Example:
Let's take a simple document as an example:
- Document 1: "Data science is fun. Data science is challenging."

### Step 1: Tokenize the Document

We first break down the document into individual words:
- ["Data", "science", "is", "fun", "Data", "science", "is", "challenging"]

### Step 2: Calculate Term Frequency

Now, calculate the frequency of each word and divide by the total number of words (8 in this case):

| Word         | Count | Term Frequency (TF) |
|--------------|-------|---------------------|
| Data         | 2     | 2/8 = 0.25          |
| science      | 2     | 2/8 = 0.25          |
| is           | 2     | 2/8 = 0.25          |
| fun          | 1     | 1/8 = 0.125         |
| challenging  | 1     | 1/8 = 0.125         |

## Where TF Works Well:
- **Document Ranking**: In search engines, TF can help rank documents based on the relevance of certain keywords. If a word appears frequently in a document, that document may be more relevant to the search query.
- **Basic Text Classification**: TF can be useful in classification tasks where the frequency of specific words is important, such as sentiment analysis, where more occurrences of certain positive or negative words affect the sentiment score.
- **Spam Detection**: High frequency of spam-related words (like "free" or "win") can indicate that a document is spam.

## Where TF Doesn’t Work Well:
- **Ignoring Word Importance Across Documents**: TF only considers word frequency in a single document and ignores the overall importance of a word across a larger corpus. For example, common words like "is" or "the" will get high TF scores, even though they are not useful for differentiating documents. This issue is addressed by Inverse Document Frequency (IDF), which down-weights common words.
- **Word Semantics**: TF doesn't capture the meaning of words. It only counts occurrences without considering context, synonyms, or polysemy (words with multiple meanings).
- **Position and Structure**: TF doesn’t account for where the word appears or its relationship with other words. It treats all words as independent of each other, so important phrases or word sequences are not captured.

## Example of When TF Falls Short:
Consider a document that has a high frequency of stopwords (common words like "the," "is," "and"). TF will give these words a high score, which may not be desirable in contexts where these words don't convey much meaning or distinction.

In summary, Term Frequency (TF) is useful for capturing the importance of a word within a document but has limitations in understanding global importance, meaning, or context. To address these limitations, it is often combined with Inverse Document Frequency (IDF), forming the widely-used TF-IDF model.
