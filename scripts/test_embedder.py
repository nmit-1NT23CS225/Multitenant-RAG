from ingestion.embedder import embed_chunks, embed_query

sample_chunks = [
    "The liability clause states that damages are capped at $10,000.",
    "Employees are entitled to 20 days of paid leave annually.",
    "The notice period for termination is 30 days."
]

print("Embedding 3 chunks...")
embeddings = embed_chunks(sample_chunks)

print(f"\nNumber of embeddings: {len(embeddings)}")
print(f"Dimensions per embedding: {len(embeddings[0])}")
print(f"First 5 values of first embedding: {embeddings[0][:5]}")

print("\nEmbedding a query...")
query_embedding = embed_query("What is the notice period?")
print(f"Query embedding dimensions: {len(query_embedding)}")
print(f"First 5 values: {query_embedding[:5]}")