from sentence_transformers import SentenceTransformers
from sklearn.metrics.pairwise import cosine_similarity

# load embedding model
model = SentenceTransformers('all-MiniLM-L6-V2')

#documents
documents = [
    "Artificial intelligence is transforming the world.",
    "Machine learning is a subset of AI",
    "Football is a popular sport",
    "Deep learning uses neural network"
]

#convert documents embeddings.
doc_embedding = model.encode(documents)

#Query
query = "What is machine learning?"

query_embedding = model.encode([query])

# compute similarity
similarities = cosine_similarity(query_embedding, doc_embedding)

# find best match
best_index = similarities.argmax()

print("Best Match:",documents[best_index])
