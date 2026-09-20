import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):

    pos = np.arange(seq_len)[:, None]
    i = np.arange(0, d_model, 2)

    angle = pos / (base ** (i / d_model))

    pe = np.zeros((seq_len, d_model))

    pe[:, 0::2] = np.sin(angle)
    pe[:, 1::2] = np.cos(angle[:, :pe[:, 1::2].shape[1]])

    return pe