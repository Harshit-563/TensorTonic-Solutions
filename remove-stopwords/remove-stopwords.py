def remove_stopwords(tokens: list, stopwords: list) -> list:
    """
    Returns a list of tokens.
    """
    a = [x for x in tokens if x not in stopwords] 
    return a