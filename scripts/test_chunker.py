from ingestion.chunker import chunk_text

sample_text = """
Artificial intelligence is the simulation of human intelligence processes 
by machines, especially computer systems. These processes include learning, 
reasoning, and self-correction. Particular applications of AI include expert 
systems, natural language processing, speech recognition and machine vision.
Machine learning is a method of data analysis that automates analytical model 
building. It is based on the idea that systems can learn from data, identify 
patterns and make decisions with minimal human intervention. Deep learning is 
part of a broader family of machine learning methods based on artificial neural 
networks with representation learning.
""" * 10

chunks = chunk_text(sample_text)

print(f"Total chunks: {len(chunks)}")
print(f"\nFirst chunk:\n{chunks[0]}")
print(f"\nSecond chunk:\n{chunks[1]}")
print(f"\nLast chunk:\n{chunks[-1]}")
print(f"\nChunk sizes: {[len(c.split()) for c in chunks]}")