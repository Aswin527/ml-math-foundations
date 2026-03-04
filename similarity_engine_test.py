from similarity_engine import find_most_similar 

dataset = {
    "movie1": [1, 1, 0, 1],
    "movie2": [0, 1, 1, 0],
    "movie3": [1, 1, 1, 1]
}

query = [1, 0, 1, 1]

result = find_most_similar(query, dataset)

print(result)