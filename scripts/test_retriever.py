from retrieval.retriever import retrieve_chunks

if __name__ == "__main__":
    
    queries = [
        "What is artificial intelligence?",
        "How does machine learning work?",
        "What is deep learning?",
    ]
    
    for query in queries:
        print(f"\n{'='*60}")
        print(f"Query: {query}")
        print(f"{'='*60}")
        
        results = retrieve_chunks(
            tenant_id="org_a",
            query=query,
            top_k=3
        )
        
        for i, result in enumerate(results, 1):
            print(f"\nResult {i} (similarity: {result['similarity']})")
            print(f"  Doc: {result['doc_id']}")
            print(f"  Preview: {result['chunk_text'][:100]}...")