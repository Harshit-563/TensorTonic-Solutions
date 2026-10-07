def item_cf_predict(user_ratings: list, item_similarities: list, target: int) -> float:
    """
    Returns the similarity-weighted rating prediction.
    """
    weighted_sum = 0.0
    similarity_sum = 0.0
    for i in range(len(user_ratings)):
        if(i!=target and user_ratings[i] != 0 and item_similarities[i] > 0):
            weighted_sum += user_ratings[i] * item_similarities[i]
            similarity_sum += item_similarities[i]
            
    if (similarity_sum == 0.0) :
        return 0
    return weighted_sum/similarity_sum    
        
    