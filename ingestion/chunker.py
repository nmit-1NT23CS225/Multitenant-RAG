from typing import List


def chunk_text(text: str,chunk_size: int=400,overlap: int=50)-> List[str]:
    """
    Split text into overlapping chunks of approximately chunk_size characters.
    
    Args:
        text: raw text to split
        chunk_size: target size of each chunk in characters
        overlap: number of characters to overlap between chunks
    
    Returns:
        list of text chunks
    """
    if not text or not text.strip():
        return []
    words=text.split()
    chunks=[]
    start=0
     
    while start<len(words):
        end=start+chunk_size
        chunk=" ".join(words[start:end])
        chunks.append(chunk)
        start+=chunk_size-overlap
    return chunks