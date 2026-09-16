def text_chunking(tokens: list, chunk_size: int, overlap: int) -> list:
    """
    Returns fixed-size token chunks with the requested overlap.
    """
    # Write code here
    chunks = []
    step = chunk_size - overlap
    for i in range(0, len(tokens)-overlap, step):
        if i < len(tokens):
            chunks.append(tokens[i:i+chunk_size])
        
    return chunks