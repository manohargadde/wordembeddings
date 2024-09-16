from transformers import BertTokenizer, BertModel
import torch

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
# Loads the BERT tokenizer. The 'bert-base-uncased' model is a smaller variant of BERT trained on uncased English text.
model = BertModel.from_pretrained('bert-base-uncased')
#Loads the pre-trained BERT model.

# Example text
text = "The quick brown fox jumps over the lazy dog."

# Tokenize input text
#Tokenizes the input text and converts it into PyTorch tensors. This is needed for feeding the input into the model.
inputs = tokenizer(text, return_tensors='pt')

# Forward pass through BERT model
with torch.no_grad():
    #Passes the tokenized input through the BERT model to obtain embeddings.
    outputs = model(**inputs)

# Get the embeddings for the first token in the sentence
# outputs['last_hidden_state'] contains embeddings for all tokens in the input sequence. The shape of this tensor is (batch_size, sequence_length, hidden_size).
last_hidden_state = outputs.last_hidden_state
print(f"Shape of last_hidden_state: {last_hidden_state.shape}")

# Print embeddings for the first token ([CLS] token). Extracts the embedding for the [CLS] token, which is often used for classification tasks.
cls_embedding = last_hidden_state[0][0]
print(f"Embedding for [CLS] token: {cls_embedding}")

# Example: Print embeddings for each token
# convert_ids_to_tokens - Converts token IDs back to token strings for better readability.
tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
for token, embedding in zip(tokens, last_hidden_state[0]):
    print(f"Token: {token}, Embedding: {embedding}")
