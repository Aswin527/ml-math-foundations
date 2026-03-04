from vector import cosine_similarity

def find_similar(query_vector, dataset):
    
    best_score = -1
    best_item = None

    for name, vector in dataset.items():
        score = cosine_similarity(query_vector, vector)

        if score > best_score:
            best_score = score
            best_item = name

    return best_item,best_score

