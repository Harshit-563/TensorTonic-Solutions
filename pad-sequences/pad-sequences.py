import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    N = len(seqs)
    L = max_len if max_len is not None else (max((len(seq) for seq in seqs), default=0))
    
    # Initialize with pad_value
    arr = np.full((N, L), pad_value, dtype=np.int64)
    
    # Copy sequences into padded array
    for i, seq in enumerate(seqs):
        length = min(len(seq), L)
        arr[i, :length] = seq[:length]
    
    return arr